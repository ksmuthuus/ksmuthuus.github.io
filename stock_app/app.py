from flask import Flask, render_template
from flask_frozen import Freezer
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import os

app = Flask(__name__)
freezer = Freezer(app)

@app.route('/')
def home():
    # Define the stock ticker symbols
    ticker_symbols = ['DRREDDY.NS', 'CDSL.NS', 'NATCOPHARM.NS']

    # Initialize lists to store data for plotting
    tickers = []
    fifty_two_week_lows = []
    current_prices = []
    fifty_two_week_highs = []

    # Loop through each ticker symbol and fetch the required data
    for ticker_symbol in ticker_symbols:
        # Fetch the stock data
        stock_data = yf.Ticker(ticker_symbol)
        
        # Get the current stock price
        current_price = stock_data.info['currentPrice']
        
        # Get the 52-week low and high
        fifty_two_week_low = stock_data.info['fiftyTwoWeekLow']
        fifty_two_week_high = stock_data.info['fiftyTwoWeekHigh']
        
        # Append the data to the lists
        tickers.append(ticker_symbol)
        fifty_two_week_lows.append(fifty_two_week_low)
        current_prices.append(current_price)
        fifty_two_week_highs.append(fifty_two_week_high)

    # Set the positions and width for the bars
    pos = np.arange(len(tickers))
    bar_width = 0.4

    # Create a bar chart
    plt.figure(figsize=(12, 6))

    # Plot the bars for each ticker
    for i in range(len(tickers)):
        plt.bar(pos[i], fifty_two_week_highs[i] - fifty_two_week_lows[i], bar_width, bottom=fifty_two_week_lows[i], label=f'{tickers[i]}')
        plt.scatter(pos[i], current_prices[i], color='black', zorder=5)  # Add a point for the current price
        
        # Annotate the values on the bars
        plt.text(pos[i], fifty_two_week_lows[i], f'{fifty_two_week_lows[i]:.2f}', ha='center', va='bottom', color='blue')
        plt.text(pos[i], current_prices[i], f'{current_prices[i]:.2f}', ha='center', va='bottom', color='black')
        plt.text(pos[i], fifty_two_week_highs[i], f'{fifty_two_week_highs[i]:.2f}', ha='center', va='bottom', color='green')

    # Add labels and title
    plt.xlabel('Ticker Symbol')
    plt.ylabel('Price (INR)')
    plt.title('52-Week Low, Current Price, and 52-Week High for Each Ticker')
    plt.xticks(pos, tickers)
    plt.legend()
    plt.grid(True)

    # Save the plot as an image
    if not os.path.exists('static'):
        os.makedirs('static')
    plt.savefig('static/plot.png')
    plt.close()

    return render_template('index.html')

if __name__ == '__main__':
     freezer.freeze()
    # app.run(debug=True)