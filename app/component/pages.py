import streamlit as st

class Pages:
  def __init__(self):
    ...

  def page(self):
    st.page_link("pages/Stock.py", label="Stock", icon="1️⃣")
    st.page_link("pages/Counter.py", label="Counter", icon="2️⃣")
    # st.page_link("http://www.google.com", label="Google", icon="🌎")
