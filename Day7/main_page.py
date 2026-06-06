import streamlit as st
import pandas as pd

# Main page content
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

Billionare = pd.read_csv("Billionaires.csv", index_col=[0])
Billionare["Net Worth"] = Billionare["Net Worth"].apply(lambda x: x[1: -1])
Billionare["Net Worth"] = pd.to_numeric(Billionare["Net Worth"])
st.write(Billionare)