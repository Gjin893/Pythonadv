import pandas as pd
import streamlit as st

df = pd.DataFrame({
    'Name ':['Alice', 'Bob', 'Charlie'],
    'Age':[24, 22,27],
    'City':['Los Angelos', 'New York', 'Oklahoma']
})

st.write(df)