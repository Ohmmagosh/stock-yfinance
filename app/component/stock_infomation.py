from pydantic import ValidationError
from component.textbox import TextBox
import streamlit as st
from models.models import StockData, LabelText
from rich import inspect as insp ,print as rprint

# if info.get('dividendRate') is not None:
#       dividend = info.get('dividendRate')
#     else:
#       dividend = "0"
#     yield_rate = round(float(info['dividendYield'] * 100), 2)
#     TextBox("Forward Dividend & Yield", f"{dividend:,} % / ( {yield_rate} % )").render()
#     TextBox("Full Time Employees", f"{info['fullTimeEmployees']:,}").render()
#     TextBox("Bussiness Summary", info['longBusinessSummary']).render(use_markdown=True)
#     forward_thirty_usd_per_month, forward_thb_per_month = get_thirty_usd_thb_per_month(dividend)
#     yield_thirthy_usd_per_month_format, yield_thb_per_month_format = get_thirty_usd_thb_per_month(yield_rate)
#     TextBox("Forward Dividend: Cost Dividend 30 usd/thb per month", f'{forward_thirty_usd_per_month} / {forward_thb_per_month}   (1 usd per 36.22 thb)').render()
#     TextBox("Yield: Cost Dividend 30 usd/thb per month", f'{yield_thirthy_usd_per_month_format} / {yield_thb_per_month_format}   (1 usd per 36.22 thb)').render()

class StockInFomation:
  def __init__(self, info: dict) -> None:
    self.data = self.set_data(info)

  def set_data(self, data: dict):
    try:
      data = StockData(
        name=LabelText(
          label="Company Name",
          dtype="str",
          value=data.get('longName')
          ),
        site_name=LabelText(
          label="Website",
          dtype="str",
          value=data.get('website')
          ),
        country=LabelText(
          label="Country",
          dtype="str",
          value=data.get('country')
          ),
        sector=LabelText(
          label="Sector",
          dtype="str",
          value=data.get('sector')
          ),
        industry=LabelText(
          label="Industry",
          dtype="str",
          value=data.get('industry')
          ),
        current_price=LabelText(
          label="Current Price",
          dtype="float",
          value=data.get('currentPrice'),
          prefix="c"
          ),
        market_cap=LabelText(
          label="Market Cap",
          dtype="int",
          value=data.get('marketCap') ,
          prefix="c"
          ),
        book_value=LabelText(
          label="Book Value",
          dtype="float",
          value=data.get('bookValue') ,
          prefix="c"
          ),
        dividend_rate=LabelText(
          label="Dividend Rate",
          dtype="float",
          value=data.get('dividendRate') ,
          prefix="p"
          ),
        dividend_yield=LabelText(
          label="Dividend Yield",
          dtype="float",
          value=data.get('dividendYield'),
          prefix="p"
          ),
        quote_type=LabelText(
          label="Quote Type",
          dtype="str",
          value=data.get('quoteType')
          ),
        full_time_employees=LabelText(
          label="Full Time Employees",
          dtype="int",
          value=data.get('fullTimeEmployees')
          ),
        yield_etf=LabelText(
          label="Yield",
          dtype="float",
          value='{:,.2f}'.format(data.get('yield') * 100) if data.get('yield') is not None else None,
          prefix="p"
          ),
      )
      # rprint(data.dict())
      return data
    except ValidationError as e:
      rprint(repr(e.errors()[0]['type']))

  def set_forward_dividend(self):
    pass
    # dividendRate = self.get_infomation(self.data, 'dividendRate')



  def get_thirty_usd_thb_per_month(self,yield_rate):
    thirthy_usd_per_month = round((36000 / yield_rate), 2)
    thirthy_usd_per_month_format = "{:,.2f}".format(thirthy_usd_per_month)
    thb_per_month = round(thirthy_usd_per_month * 36.22, 2)
    thb_per_month_format = "{:,.2f}".format(thb_per_month)
    return thirthy_usd_per_month_format, thb_per_month_format

  def render(self):
    for key, value in self.data.dict().items():
      if value["value"] is not None and value["value"] is not None:
        match value["dtype"]:
          case "str":
            TextBox(value["label"], value["value"]).render()
          case "int":
            val = '{:,}'.format(int(value["value"]))
            match value["prefix"]:
              case "c":
                TextBox(value["label"], f"{val} $").render()
              case "p":
                TextBox(value["label"], f"{val} %").render()
              case None:
                TextBox(value["label"], f"{val}").render()
          case "float":
            val = '{:,.2f}'.format(float(value["value"]))
            match value["prefix"]:
              case "c":
                TextBox(value["label"], f"{val} $").render()
              case "p":
                TextBox(value["label"], f"{val} %").render()
              case None:
                TextBox(value["label"], f"{val}").render()
      else:
        pass
