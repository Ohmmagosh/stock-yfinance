import streamlit as st

class Pages:
  def __init__(self):
    ...

  def page(self):
    st.page_link("pages/home.py", label="Stock", icon="1️⃣")
    # st.page_link("pages/home2.py", label="Page 2", icon="2️⃣")
    st.page_link("http://www.google.com", label="Google", icon="🌎")
