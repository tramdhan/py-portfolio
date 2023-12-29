import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("assets/images/photo.png")

with col2:
    st.title("Trevor Ramdhan")
    content = """
        Hi, I'm Trevor Ramdhan, a full-stack Node-js, Python developer.
    """
    st.info(content)

content2 = """
Below is a list of projects and apps I have developed.
"""

st.write(content2)

#  col sizes, with 0.5 space between the data cols
col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data/data.csv", sep=";")

#  first 0 to 10 items
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("assets/images/" + row["image"])
        st.write(f"[Source Code]({row["url"]})")

#  second set, from 10 to 20 items
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("assets/images/" + row["image"])
        st.write(f"[Source Code]({row["url"]})")