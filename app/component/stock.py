import yfinance as yf
from datetime import datetime

class Stock:
  def __init__(self, name):
    self.ticker = yf.Ticker(name)

  def get_info(self):
    return self.ticker.info

  def get_balance_sheet(self):
    return self.ticker.balance_sheet

  def get_price(self, period="1d", interval="15m"):
    return self.ticker.history(period=period, interval=interval)
