import streamlit as st

st.set_page_config(page_title="LangChain Summarizer", layout="wide")

st.title("LangChain AI Summarizer")

st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Choose a page:",
    ["News Summarizer", "Settings"],
    index=0,
)

if menu == "News Summarizer":
    st.header("NEWS Summarizer")
    st.write("This page will fetch and summarize news from the past week using OpenAI and Serper APIs.")
else:
    st.header("Settings")
    st.write("You are on the settings page.")