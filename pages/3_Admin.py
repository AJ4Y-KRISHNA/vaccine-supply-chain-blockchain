import streamlit as st
from pathlib import Path

# Load CSS
def load_css():
    css_path = Path(__file__).parent.parent / "styles" / "style.css"
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.markdown("""
<div class="title">
⚙ Admin Control Panel
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("👤 Admin Management")

admin_name = st.text_input("Admin Name")
admin_role = st.selectbox("Role", ["Super Admin","Supply Manager","Distributor Manager"])

create_admin = st.button("Create Admin")

if create_admin:
    st.success("Admin account created successfully")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📊 System Status")

col1,col2,col3 = st.columns(3)

with col1:
    st.metric("Active Users","15")

with col2:
    st.metric("Total Batches","120")

with col3:
    st.metric("Blockchain Status","Connected")

st.markdown('</div>', unsafe_allow_html=True)