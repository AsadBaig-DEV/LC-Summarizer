import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
import os

def url_summarizer_page():
    """News Summarizer Page"""
    st.title("URL Summarizer")
    st.write("Summarize webpage using LangChain and OpenAI.")