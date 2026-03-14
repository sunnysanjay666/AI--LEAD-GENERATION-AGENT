import streamlit as st
import pandas as pd

st.title("AI Lead Generation Dashboard")

df = pd.read_csv("leads.csv")

st.write("Lead Data")
st.dataframe(df)