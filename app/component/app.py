import streamlit as st
from component.stock import Stock
from component.pages import Pages
import time

class App:
  def __init__(self, name):
    self.name = name

  def run(self):
    with st.sidebar:
      with st.echo():
          st.write("This code will be printed to the sidebar.")

      with st.spinner("Loading..."):
          time.sleep(5)
      st.success("Done!")
      Pages().page()


