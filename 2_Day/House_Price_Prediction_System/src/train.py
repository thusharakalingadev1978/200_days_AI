import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# Load dataset
df = pd.read_csv("data/house_prices.csv")


# Features
X = df[
    [
        "area",
        "bedrooms",
        "bathrooms",
        "age"
    ]
]


# Target
y = df["price"]


# Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = LinearRegression()


# Train model
model.fit(X_train, y_train)


# Predictions
predictions = model.predict(X_test)


# Evaluation
mae = mean_absolute_error(
    y_test,
    predictions
)

mse = mean_squared_error(
    y_test,
    predictions
)

rmse = mse ** 0.5

r2 = r2_score(
    y_test,
    predictions
)


# Results
print("========== MODEL ==========")

print("\nActual Prices:")
print(y_test.values)

print("\nPredicted Prices:")
print(predictions)


print("\n========== METRICS ==========")

print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)
print("R2  :", r2)


print("\n========== MODEL PARAMETERS ==========")

print("Intercept:")
print(model.intercept_)

print("\nCoefficients:")
print(model.coef_)


results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions
})

print("\n========== COMPARISON ==========")
print(results)

new_house = pd.DataFrame({
    "area": [1600],
    "bedrooms": [3],
    "bathrooms": [2],
    "age": [5]
})

predicted_price = model.predict(new_house)

print("\nNew House Prediction:")
print(predicted_price[0])


joblib.dump(
    model,
    "models/house_price_model.pkl"
)







