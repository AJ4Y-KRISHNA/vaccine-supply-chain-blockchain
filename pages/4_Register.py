import streamlit as st
from pathlib import Path
from ethereum_connector import register_batch

def load_css():
    css_path = Path(__file__).parent.parent / "styles" / "style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.markdown("""
<div class="title">
📦 Register Vaccine Batch
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

batch_id = st.text_input("Batch ID")
vaccine = st.text_input("Vaccine Name")
manufacturer = st.text_input("Manufacturer")

register = st.button("Register Batch")

if register:
    try:
        result = register_batch(batch_id,vaccine,manufacturer)
        st.success(result["message"])
    except Exception as e:
        st.error(str(e))

st.markdown('</div>', unsafe_allow_html=True)