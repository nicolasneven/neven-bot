import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

prices = client.get_all_tickers()

for price in prices:
    print(price)

# candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile = open('btc5min-2020-2021.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2020", "22 Feb, 2021")

for candle in candlesticks:
    print(candle)
    candlestick_writer.writerow(candle)

print(len(candlesticks))
csvfile.close()
