import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json,csv
import dotenv
import os

dotenv.load_dotenv()
alpha_vantage_key = os.getenv("otavapi")
url = f"https://www.alphavantage.co/query"
stock_name = input("Enter the stock name: ")
data = {
    "function": "TIME_SERIES_DAILY",
    "symbol": stock_name,
    "outputsize": "full",
    "datatype": "csv",
    "apikey": alpha_vantage_key
}
try:
    open(f"{stock_name}.csv", "r")
except FileNotFoundError:
    response = requests.get(url, params=data)
    csv_file = open(f"{stock_name}.csv", "w")
    temp = list(response.text.split("\n"))
    temp.reverse()
    csv_file.write(temp[-1])
    csv_file.writelines(temp[:len(temp)-1][5244:])
    csv_file.close()
    print("Data fetched and saved to file")
df = pd.read_csv(f"{stock_name}.csv")

df.sort_values('timestamp', inplace=True)
# Prepare the data
stock_data = df.dropna()
X = np.arange(len(stock_data)).reshape(-1, 1)
y = stock_data['close'].values

# Train-test split
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2, shuffle=False)

# Linear regression model
linear_model = sklearn.linear_model.LinearRegression()
linear_model.fit(X_train, y_train)

# Predict future prices with linear model
y_linear_pred = linear_model.predict(X_test)

# # Polynomial regression model
poly_features = sklearn.preprocessing.PolynomialFeatures(degree=4)
X_poly_train = poly_features.fit_transform(X_train)
X_poly_test = poly_features.transform(X_test)
poly_model = sklearn.linear_model.LinearRegression()
poly_model.fit(X_poly_train, y_train)
y_poly_pred = poly_model.predict(X_poly_test)

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(stock_data.index, stock_data['close'], label='Actual Prices')
plt.plot(stock_data.index[len(X_train):], y_linear_pred, label='Linear Predicted Prices', linestyle='--')
plt.plot(stock_data.index[len(X_train):], y_poly_pred, label='Polynomial Predicted Prices', linestyle='--')

# Overlay the regression line on the entire data
full_X = np.arange(len(stock_data)).reshape(-1, 1)
full_y_linear_pred = linear_model.predict(full_X)
full_X_poly = poly_features.transform(full_X)
full_y_poly_pred = poly_model.predict(full_X_poly)
plt.plot(stock_data.index, full_y_linear_pred, label='Linear Regression Line', color='red', linestyle='-.')
plt.plot(stock_data.index, full_y_poly_pred, label='Polynomial Regression Line', color='green', linestyle='-.')

plt.title(f'{stock_name} Stock Prices Prediction')
plt.xlabel('Date')
plt.ylabel('Price USD')
plt.legend()
plt.show()

