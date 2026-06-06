import streamlit as st
import pandas as pd
import numpy as np
st.write("Hello, World!")

"""
# My first app
Here's our first attempt at using data to create a table:
"""
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)

# Ví dụ
dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

# VD
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

# VD
dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

# Bai tap
data = {
    "Name":["John",'Jane',"Doe"],
    "Age":[30,25,35],
    "City":["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
df.to_csv("output.csv", index=False)
df_read = pd.read_csv("output.csv")
df

# mấy thông tin/bài khác trong main_page.py