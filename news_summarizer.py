import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
import os


def news_summarizer_page():
    """News Summarizer Page"""
    st.title("News Summarizer")
    st.write("Summarize news articles using LangChain and OpenAI.")

    query = st.text_input("Enter your news topic:")
    if st.button("Search & Summarize"):
        openai_api_key = st.session_state.openai_api_key or os.getenv("OPENAI_API_KEY")
        serper_api_key = st.session_state.serper_api_key or os.getenv("SERPER_API_KEY")

        if not openai_api_key or not serper_api_key:
            st.error("Please set your API keys in the Settings page or .env file.")
            return

        with st.spinner("Searching and summarizing..."):
            # Fetch top news results
            search = GoogleSerperAPIWrapper(
                type="news", tbs="qdr:w1", serper_api_key=serper_api_key
            )
            result_dict = search.results(query)

            if not result_dict.get("news"):
                st.warning("No news found.")
                return

            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3, api_key=openai_api_key)

            prompt = ChatPromptTemplate.from_template(
                "Summarize the following content in 150 words:\n\n{text}"
            )

            summarize_chain = (
                {"text": RunnablePassthrough()} 
                | prompt 
                | llm
            )

            for i, item in enumerate(result_dict["news"][:3]):
                st.markdown(f"### {i+1}. [{item['title']}]({item['link']})")

                loader = UnstructuredURLLoader(
                    urls=[item["link"]], ssl_verify=False,
                    headers={"User-Agent": "Mozilla/5.0"}
                )
                docs = loader.load()

                combined_text = "\n\n".join(d.page_content for d in docs)
                summary = summarize_chain.invoke({"text": combined_text})

                st.write(summary.content)
