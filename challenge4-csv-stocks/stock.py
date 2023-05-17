import csv

def calculate_average_return(filename):
    # Dictionary to store daily returns for each stock
    stock_returns = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # Skip header row
        next(reader)  

        for row in reader:
            # Extracting stock name
            stock_name = row[0]
            # Extracting close price
            close_price = float(row[1])
            # Extracting previous close price
            prev_close_price = float(row[2])
            # Calculating daily return
            daily_return = (close_price - prev_close_price) / prev_close_price

            # Adding daily return to existing stock
            if stock_name in stock_returns:
                stock_returns[stock_name].append(daily_return)

            # Creating new list with daily return for the stock
            else:
                stock_returns[stock_name] = [daily_return]

    # Creating dictionary to store average returns for each stock
    average_returns = {}
    for stock_name, returns in stock_returns.items():
        # Calculate average return
        average_returns[stock_name] = sum(returns) / len(returns)

    # Sorting and get top 10 stocks
    top_stocks = sorted(average_returns.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_stocks

# Main program
# csv file to use 
filename = 'stocks2.csv'
# Calculating top performing stocks
top_stocks = calculate_average_return(filename)

# Print stock and average return
print("Top 10 Performing Stocks:")
for stock, avg_return in top_stocks:
    print(f"{stock}: {avg_return}")
