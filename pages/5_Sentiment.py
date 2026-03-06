import streamlit as st
from pathlib import Path
from sentiment_module import analyze_sentiment

def load_css():
    css_path = Path(__file__).parent.parent / "styles" / "style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.markdown("""
<div class="title">
🧠 Vaccine Sentiment Analysis
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

text = st.text_area("Enter public opinion or feedback")

analyze = st.button("Analyze Sentiment")

if analyze:
    result = analyze_sentiment(text)

    if result == "Positive":
        st.success("Positive Sentiment 😊")

    elif result == "Negative":
        st.error("Negative Sentiment ⚠")

    else:
        st.info("Neutral Sentiment")

st.markdown('</div>', unsafe_allow_html=True)