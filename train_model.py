import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

# Load dataset
df = pd.read_csv("data/flood.csv")
# If you are using CSV instead, use:
# df = pd.read_csv("data/flood.csv")

# Features and target
X = df.drop("flood", axis=1)
y = df["flood"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save model and scaler
joblib.dump(model, "models/flood_model.joblib")
joblib.dump(scaler, "models/scaler.joblib")

print("Model and scaler saved successfully!")