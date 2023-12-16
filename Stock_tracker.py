import yfinance as yf
import streamlit as st 
import pandas as pd 

st.write(""" 
# Simple Stock Price *App*


Shown are the stock closing price and volume of     !
""")
# Defining the ticker symbol
tick_symbol = 'GOOGL'
# Get data on this tracker
ticker_data = yf.Ticker(tick_symbol)
# Get the historical prices for this ticker
tickerDf = ticker_data.history(period='id',start ='2020-12-31', end='2023-12-31')
# Open high low close volume dividends stock splits

st.write("""
## Closing Price""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price""")
st.line_chart(tickerDf.Volume)