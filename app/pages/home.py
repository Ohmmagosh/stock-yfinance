import streamlit as st
from component.stock import Stock
from component.textbox import TextBox
import pandas as pd
import altair as alt
from vega_datasets import data


stock_default = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]


def click_me(stock: str):
  print(stock)
  # st.session_state["stock"] = stock

@st.cache_data
def get_data():
    source = data.stocks()
    source = source[source.date.gt("2024-01-01")]
    return source

def get_chart(data):
    print(f'data ${data}')
    hover = alt.selection_single(
        fields=["Datetime"],
        nearest=True,
        on="mouseover",
        empty="none",
    )
    lines = (
        alt.Chart(data, title="Evolution of stock prices")
        .mark_line()
        .encode(
            x="Datetime",
            y="Close",
            color=alt.value("green"),
          )
        )

    # Draw points on the line, and highlight based on selection
    # points = lines.transform_filter(hover).mark_circle(size=65)

    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(data)
        .mark_rule()
        .encode(
            x="yearmonthdate(date)",
            y="Close",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("Datetime", title="Date"),
                alt.Tooltip("Close", title="Price (USD)"),
            ],
        )
        .add_selection(hover)
    )
    return (lines + tooltips).interactive()

def get_thirty_usd_thb_per_month(yield_rate):
  thirthy_usd_per_month = round((36000 / yield_rate), 2)
  thirthy_usd_per_month_format = "{:,.2f}".format(thirthy_usd_per_month)
  thb_per_month = round(thirthy_usd_per_month * 36.22, 2)
  thb_per_month_format = "{:,.2f}".format(thb_per_month)
  return thirthy_usd_per_month_format, thb_per_month_format


def main():
  st.header("Stock information")
  ticker = st.text_input("Enter a stock ticker")
  s_name = None
  if ticker:
    s_name = ticker
  elif st.session_state.get("stock"):
    s_name = st.session_state.get("stock")
  if s_name:
    stock = Stock(s_name)
    info = stock.get_info()
    TextBox("Company Name", info.get('longName')).render()
    TextBox("Website", info.get('website')).render()
    TextBox("Country", info.get('country')).render()
    TextBox("Sector", info.get('sector')).render()
    TextBox("Industry", info.get('industry')).render()
    TextBox("Current Price", f"{info['currentPrice']} $").render()
    TextBox("Market Cap", f"{info['marketCap']:,} $").render()
    TextBox("Book Value", f"{info['bookValue']} $").render()
    if info.get('dividendRate') is not None:
      dividend = info.get('dividendRate')
    else:
      dividend = "0"
    yield_rate = round(float(info['dividendYield'] * 100), 2)
    TextBox("Forward Dividend & Yield", f"{dividend:,} % / ( {yield_rate} % )").render()
    TextBox("Full Time Employees", f"{info['fullTimeEmployees']:,}").render()
    TextBox("Bussiness Summary", info['longBusinessSummary']).render(use_markdown=True)
    forward_thirty_usd_per_month, forward_thb_per_month = get_thirty_usd_thb_per_month(dividend)
    yield_thirthy_usd_per_month_format, yield_thb_per_month_format = get_thirty_usd_thb_per_month(yield_rate)
    TextBox("Forward Dividend: Cost Dividend 30 usd/thb per month", f'{forward_thirty_usd_per_month} / {forward_thb_per_month}   (1 usd per 36.22 thb)').render()
    TextBox("Yield: Cost Dividend 30 usd/thb per month", f'{yield_thirthy_usd_per_month_format} / {yield_thb_per_month_format}   (1 usd per 36.22 thb)').render()





if __name__ == "__main__":
  main()
