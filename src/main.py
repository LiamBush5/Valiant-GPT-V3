from streamlit_oauth import OAuth2Component
import re
import streamlit as st
from bs4 import BeautifulSoup
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from streamlit_chat import message
# from langsmith import traceable
import openai
from config import *
from vector_store import vector_store



if 'buffer_memory' not in st.session_state:
   st.session_state.buffer_memory = ConversationBufferWindowMemory(
       k=3, return_messages=True)


def remove_html_tags(text):
   soup = BeautifulSoup(text, "html.parser")
   cleaned_text = soup.get_text()
   return cleaned_text

def clean_text(text):
   cleaned_text = text.strip().strip("[]")
   cleaned_text = cleaned_text.replace("\n\n", "\n")
   cleaned_text = re.sub('<.*?>', '', cleaned_text)
   return cleaned_text


# @traceable
def generate_response(topic, chat_history):
    client = openai.Client(api_key=OPENAI_API_KEY)
    docs = vector_store.similarity_search(
        topic,  # our search query
        k=12  # return 8 most relevant docs
    )

    # Remove a doc if it has already been used
    used_sources = []
    sources = []
    for doc in docs:
        cleaned_doc_content = clean_text(doc.page_content)
        if cleaned_doc_content not in used_sources:
            used_sources.append(cleaned_doc_content)
            sources.append(doc)

    context = " ".join([doc.page_content for doc in sources])

    # create a single input
    input = {'topic': topic, 'context': context, 'chat_history': chat_history}
    output = client.chat.completions.create(
        messages=[
            {"role": "system", "content": script_template2.format(**input)},
            {"role": "user", "content": topic}
        ],
        model="gpt-4-turbo-2024-04-09",
        temperature=0.25,
        max_tokens=4096
    )
    formatted_text = clean_text(output.choices[0].message.content)

    sources_list = []
    sources_text = ""
    source_count = 0

    for i, source in enumerate(sources):
        cleaned_source = clean_text(source.page_content)
        source_count += 1
        sources_list.append(
            f"Source {source_count}:\n{cleaned_source}\n---------------------------------------------------------------------------")

        # Join all the cleaned sources into one string
        sources_text = "".join(sources_list)

    a = sources_text
    result = f"{formatted_text}\n\nSources:\n`{a}`"
    st.session_state.buffer_memory.save_context(
        {"input": str(topic)}, {"output": str(formatted_text)})

    # Also save the interaction in Streamlit's session state
    st.session_state['history'] = {"input": str(
        topic), "output": str(formatted_text)}
    return result

script_template2 = PromptTemplate(
    template="""
    You are a chatbot trained on Valiant Solutions' reusable content library. Use the chat history, sources, and topic to answer your questions, ensuring your responses are accurate and no data is made up. Disregard the history if it's not relevant to the current topic below.

    History: {chat_history}
    Sources: {context}
    Topic: {topic}
    """,
    input_variables=["chat_history", "context", "topic"]
)

oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZE_URL, TOKEN_URL,
                        REFRESH_TOKEN_URL, REVOKE_TOKEN_URL)

def main():
    st.title("Valiant GPT Chatbot")

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Placeholder for chat history
    chat_placeholder = st.empty()

    user_input = st.text_input(
        "Please type your question here", key="user_query")
    if st.button("Submit"):
        with st.spinner("Generating response..."):
            response = generate_response(user_input, st.session_state['chat_history'])
            st.session_state['chat_history'].append(
                 {'user': user_input, 'ai': response})

    # Display chat history in the placeholder
    st.markdown("### Chat History")
    for chat in reversed(st.session_state['chat_history']):
        message(f"**You:** {chat['user']}", is_user=True)
        message(f"**AI:** {chat['ai']}", is_user=False)

if __name__ == "__main__":
    main()
