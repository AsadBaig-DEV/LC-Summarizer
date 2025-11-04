import streamlit as st
import os

def setting_page():
    """
    Setting page Web App.
    """
    st.title("App Settings")
    st.write("Manage API keys or configuration values here.")

    with st.form("settings_form"):
        openai_current_key = st.session_state.openai_api_key
        serper_current_key = st.session_state.serper_api_key
        openai_key_display = (
            openai_current_key[:6] + "..." + openai_current_key[-4:]
            if openai_current_key and len(openai_current_key) > 10
            else "(not set)"
        )

        serper_key_display = (
            serper_current_key[:6] + "..." + serper_current_key[-4:]
            if serper_current_key and len(serper_current_key) > 10
            else "(not set)"
        )

        st.write(f"**Current OpenAI API Key:** {openai_key_display}")

        new_openai_key = st.text_input(
            "Enter temporary OpenAI API Key:",
            type="password",
            placeholder="sk-xxxx...",
        )

        st.write(f"**Current Serper API Key:** {serper_key_display}")
        new_serper_key = st.text_input(
            "Enter temporary Serper API Key:",
            type="password",
            placeholder="xxxx...",
        )
        
        submitted = st.form_submit_button("Save Key")

        if submitted:
            if new_openai_key.strip():
                st.session_state.openai_api_key = new_openai_key.strip()
                st.success("✅ Temporary OpenAI API Key saved in memory.")
            elif new_serper_key.strip():
                st.session_state.serper_api_key = new_serper_key.strip()
                st.success("✅ Temporary Serper API Key saved in memory.")
            else:
                st.warning("⚠️ No key entered. Using .env key as default.")
                st.session_state.api_key = os.getenv("OPENAI_API_KEY", "")

    st.caption("ℹ️ Temporary keys reset when app reloads.")