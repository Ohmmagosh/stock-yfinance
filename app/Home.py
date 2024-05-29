import streamlit as st
from component.app import App

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

def main():
    App("Stock Price App").run()

if __name__ == "__main__":
    main()

