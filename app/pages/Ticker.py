import streamlit as st
from component.stock_infomation import StockInFomation
from component.stock import Stock
from component.textbox import TextBox
import pandas as pd
import altair as alt
from vega_datasets import data
from rich import print as rprint


def main():
  st.header("Stock information")
  if "ticker" not in st.session_state:
    st.session_state.ticker = None
  ticker = st.text_input(label="Enter a stock ticker", type="default", placeholder="")
  if ticker is not None and ticker != "":
    stock = Stock(ticker)
    data = stock.get_info()

    if data.get('error') is not None:
      st.error("Stock ticker not found")
    else:
      StockInFomation(data.get("data")).render()

if __name__ == "__main__":
  main()
