import streamlit as st
from youtube_analyzer import build_youtube_agent
import pandas as pd

st.set_page_config(
    page_title="You-Tube Video Analyzer",
    layout="centered"
)

st.title("📹 AI Youtube Video Analyzer")

@st.cache_resource
def get_agent():
    return build_youtube_agent()   

agent = get_agent()

# input box
video_url = st.text_input("Enter YouTube video link")
button = st.button("Analyze Video")

if video_url and button:
    with st.spinner("Analyzing Video..."):
        response = agent.run(
            f"Analyze this Video: {video_url}"
        )

    st.markdown("## 📊 Analysis Report of Video")
    st.markdown(response.content)