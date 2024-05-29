import yfinance as yf
from datetime import datetime
from rich import inspect as insp, print as rprint

class Stock:
  def __init__(self, name: str):
    self.name = name.upper()

  def tranform_infomation(self, data):
    ret ={}
    if data.get('trailingPegRatio') is not None or data.get('quoteType') == 'ETF' or data.get('quoteType') == 'EQUITY':
      ret = {
        "data": data,
        "error": None
      }
    else:
      ret =  {
        "data": None,
        "error": "Stock ticker not found"
      }
    return ret

  def get_info(self)->dict:
    ticker = yf.Ticker(self.name)
    info = ticker.info
    return self.tranform_infomation(info)

  def get_balance_sheet(self):
    return self.ticker.balance_sheet

  def get_price(self, period="1d", interval="15m"):
    return self.ticker.history(period=period, interval=interval)
