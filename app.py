import streamlit as st
from database import verify_user

st.set_page_config(page_title="VaccineChain", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

def login(username, password):
    user = verify_user(username, password)

    if user:
        st.session_state.logged_in = True
        st.session_state.role = user["role"]
    else:
        st.error("Invalid Credentials")

if not st.session_state.logged_in:
    st.title("🔐 VaccineChain Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        login(username, password)

    st.stop()

st.title("💉 VaccineChain Platform")
st.success(f"Logged in as: {st.session_state.role.upper()}")

if st.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.role = None
    st.rerun()

st.markdown("---")
st.write("Use sidebar to navigate.")