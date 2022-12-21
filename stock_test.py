import csv

with open('GOOG.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=',')
    for row in my_reader:
        print(row)

print('-----------------------')

import csv
with open('GOOG.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

print('----------------------')



import csv
def read_prices(tickers):
    d = {}
    for ticker in tickers:
        with open(ticker + '.csv') as f:
            for date, price, _ in csv.reader(f):
                d.setdefault(ticker, {})[date] = float(price)
    return d

