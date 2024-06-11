# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# load_dotenv()

# # API Keys and environment variables
# LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2")
# LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")

# PINECONE_API_ENV = os.getenv("PINECONE_API_ENV")
# PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# INDEX_NAME = os.getenv("INDEX_NAME")

# CLIENT_ID = os.getenv("CLIENT_ID")
# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# REDIRECT_URI = os.getenv("REDIRECT_URI")
# AUTHORIZE_URL = os.getenv("AUTHORIZE_URL")
# TOKEN_URL = os.getenv("TOKEN_URL")
# REFRESH_TOKEN_URL = os.getenv("REFRESH_TOKEN_URL")
# REVOKE_TOKEN_URL = os.getenv("REVOKE_TOKEN_URL")
# SCOPE = os.getenv("SCOPE")



import streamlit as st

LANGCHAIN_TRACING_V2 = st.secrets["LANGCHAIN_TRACING_V2"]
LANGCHAIN_API_KEY = st.secrets["LANGCHAIN_API_KEY"]

PINECONE_API_ENV = st.secrets["PINECONE_API_ENV"]
PINECONE_API_KEY = st.secrets["PINECONE_API_KEY"]
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
INDEX_NAME = st.secrets["INDEX_NAME"]

CLIENT_ID = st.secrets["CLIENT_ID"]
CLIENT_SECRET = st.secrets["CLIENT_SECRET"]
REDIRECT_URI = st.secrets["REDIRECT_URI"]
AUTHORIZE_URL = st.secrets["AUTHORIZE_URL"]
TOKEN_URL = st.secrets["TOKEN_URL"]
REFRESH_TOKEN_URL = st.secrets["REFRESH_TOKEN_URL"]
REVOKE_TOKEN_URL = st.secrets["REVOKE_TOKEN_URL"]
SCOPE = st.secrets["SCOPE"]
