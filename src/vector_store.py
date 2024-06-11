from pinecone import Pinecone
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from config import *
index_name = 'rcl'


pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(index_name)
# print(index.describe_index_stats())

# Setup for Embeddings
embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002",
    openai_api_key=OPENAI_API_KEY
)

# Pinecone Vector Store
text_field = "text"
vector_store = PineconeVectorStore(
    index, embeddings, text_field
)
