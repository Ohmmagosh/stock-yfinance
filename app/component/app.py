import streamlit as st
from component.stock import Stock
from component.pages import Pages
import time

class App:
  def __init__(self, name):
    self.name = name

  def run(self):
    Pages().page()


