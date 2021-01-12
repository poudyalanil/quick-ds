import yfinance as yf
import streamlit as st  # to create interactive web application
import pandas as pd

st.write(
    """
# Simple Stock Price App
Shown are the stock closing price and volume of Apple!
"""
)
# Stock price of apple
ticker_symbol = 'AAPL'

ticker_data = yf.Ticker(ticker_symbol)

# starting from 2010
ticker_DF = ticker_data.history(
    period='1d', start='2010-5-31', end='2020-5-31')
st.write('''

# Closing Price
''')
st.line_chart(ticker_DF.Close)

st.write('''

# Volume Price
''')

st.line_chart(ticker_DF.Volume)
