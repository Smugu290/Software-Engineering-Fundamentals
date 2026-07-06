import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# -----------------------------
# Sample Training Data
# -----------------------------
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 92, 95, 98],
    "Score": [35, 40, 45, 50, 60, 68, 75, 82, 90, 96]
}

df = pd.DataFrame(data)

# Features and target
X = df[["Study_Hours", "Attendance"]]
y = df["Score"]

model = LinearRegression()
model.fit(X, y)

st.title("Student Score Prediction")
st.write("Enter student details below:")

study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=80
)

if st.button("Predict Score"):
    prediction = model.predict([[study_hours, attendance]])
    st.success(f"Predicted Score: {prediction[0]:.2f}")
