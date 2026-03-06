import streamlit as st
from pathlib import Path
import pandas as pd
from ethereum_connector import register_batch, transfer_batch, get_batch


# Load CSS
def load_css():
    css_path = Path(__file__).parent.parent / "styles" / "style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()


# Dashboard Title
st.markdown(
    """
    <div class="title">
    💉 Vaccine Supply Chain Dashboard
    </div>
    """,
    unsafe_allow_html=True
)


# Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Batches", "120")

with col2:
    st.metric("Manufacturers", "5")

with col3:
    st.metric("Distributors", "12")

with col4:
    st.metric("Hospitals", "30")


# Input Form Card
st.markdown('<div class="card">', unsafe_allow_html=True)

batch_id = st.text_input("📦 Batch ID")
vaccine_name = st.text_input("💉 Vaccine Name")
manufacturer = st.text_input("🏭 Manufacturer")
transfer_to = st.text_input("🚚 Transfer To")

col1,col2,col3 = st.columns(3)

with col1:
    register = st.button("Register Batch")

with col2:
    transfer = st.button("Transfer Batch")

with col3:
    get_details = st.button("Get Batch Details")

st.markdown('</div>', unsafe_allow_html=True)


# Register Batch
if register:
    try:
        result = register_batch(batch_id, vaccine_name, manufacturer)
        st.success(result["message"])
    except Exception as e:
        st.error(str(e))


# Transfer Batch
if transfer:
    try:
        result = transfer_batch(batch_id, transfer_to)
        st.success(result["message"])
    except Exception as e:
        st.error(str(e))


# Get Batch
if get_details:
    try:
        data = get_batch(batch_id)

        st.markdown(
            f"""
            <div class="success-box">
            <b>Batch ID:</b> {data["batchId"]}<br>
            <b>Vaccine:</b> {data["vaccineName"]}<br>
            <b>Manufacturer:</b> {data["manufacturer"]}<br>
            <b>Current Holder:</b> {data["currentHolder"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(str(e))


# Transaction Table
st.subheader("📜 Transaction History")

data = {
    "BatchID":["B9001","B9002","B9003"],
    "Vaccine":["Covishield","Covaxin","Pfizer"],
    "Manufacturer":["Serum Institute","Bharat Biotech","Pfizer"],
    "Current Holder":["Kerala Distributor","Delhi Distributor","Mumbai Hospital"]
}

df = pd.DataFrame(data)

st.dataframe(df,use_container_width=True)