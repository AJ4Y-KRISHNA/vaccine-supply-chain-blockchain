import streamlit as st
import pandas as pd

st.title("Vaccine Supply Chain Analytics")

data = {
    "Manufacturer": [
        "Serum Institute",
        "Bharat Biotech",
        "Pfizer",
        "Moderna"
    ],
    "Batches": [45, 30, 15, 10]
}

df = pd.DataFrame(data)

st.subheader("Batches by Manufacturer")

st.bar_chart(df.set_index("Manufacturer"))

st.subheader("Distribution Share")

st.dataframe(df)