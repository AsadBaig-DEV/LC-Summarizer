import streamlit as st
import os
from dotenv import load_dotenv
from setting import setting_page
from news_summarizer import news_summarizer_page
from url_summarizer import url_summarizer_page

load_dotenv()

st.set_page_config(page_title="LangChain Summarizer", layout="wide")

if "api_key" not in st.session_state:
    st.session_state.openai_api_key = os.getenv("OPENAI_API_KEY")
    st.session_state.serper_api_key = os.getenv("SERPER_API_KEY")
    st.session_state.num_results = 5

# st.title("LangChain AI Summarizer")

st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Choose a page:",
    ["News Summarizer","URL Summarizer", "Settings"],
    index=0,
)

if menu == "News Summarizer":
    news_summarizer_page()
elif menu == "URL Summarizer":
    url_summarizer_page()
elif menu == "Settings":
    setting_page()