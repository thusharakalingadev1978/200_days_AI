
import sys
from pathlib import Path
from sklearn.model_selection import train_test_split
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pandas as pd
from src.config import HOUSE_PRICE_DATA

df = pd.read_csv(HOUSE_PRICE_DATA)

print(df)
X = df[["area", "bedrooms", "bathrooms", "age"]]

y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



print("\nFeatures:")
print(X)

print("\nTarget:")
print(y)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))