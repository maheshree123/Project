import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("volunteers_ml.csv")

# Features
X = df[["Hours", "Attendance"]]

# Target
y = df["Participate"]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(
    y_test,
    predictions
)

print("\n===== NayePankh ML Dashboard =====")
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Example Prediction
hours = 14
attendance = 82

new_data = pd.DataFrame(
    [[hours, attendance]],
    columns=["Hours", "Attendance"]
)

result = model.predict(new_data)

if result[0] == 1:
    print(
        "\nPrediction: Volunteer is likely to participate."
    )
else:
    print(
        "\nPrediction: Volunteer is unlikely to participate."
    )