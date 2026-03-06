import streamlit as st
from pathlib import Path
from ethereum_connector import get_batch

def load_css():
    css_path = Path(__file__).parent.parent / "styles" / "style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.markdown("""
<div class="title">
🚚 Vaccine Batch Tracking
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

batch_id = st.text_input("Enter Batch ID")

track = st.button("Track Batch")

if track:
    try:
        data = get_batch(batch_id)

        st.markdown(f"""
        <div class="success-box">
        <b>Batch ID:</b> {data["batchId"]}<br>
        <b>Vaccine:</b> {data["vaccineName"]}<br>
        <b>Manufacturer:</b> {data["manufacturer"]}<br>
        <b>Current Holder:</b> {data["currentHolder"]}
        </div>
        """,unsafe_allow_html=True)

        st.subheader("Supply Chain Flow")

        flow = [
            data["manufacturer"],
            "Distributor",
            data["currentHolder"]
        ]

        st.write(" ➜ ".join(flow))

    except Exception as e:
        st.error(str(e))

st.markdown('</div>', unsafe_allow_html=True)