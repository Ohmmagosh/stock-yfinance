import streamlit as st

class TextBox:
  '''
  TextBox class is a simple class that takes a header
  and a text and renders it in the app.
  '''
  def __init__(self, header, text):
      self.header = header
      self.text = text

  def render(self, use_markdown=False):
      st.subheader(self.header)
      if use_markdown:
          st.markdown(self.text)
      else:
        st.write(self.text)
