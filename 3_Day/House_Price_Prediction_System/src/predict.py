import joblib
import pandas as pd


# Load trained model
model = joblib.load(
    "models/house_price_model.pkl"
)


# New house
new_house = pd.DataFrame({
    "area": [1600],
    "bedrooms": [3],
    "bathrooms": [2],
    "age": [5]
})


# Prediction
prediction = model.predict(new_house)


print("Predicted House Price:")
print(prediction[0])