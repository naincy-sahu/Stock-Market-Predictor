import joblib

model = joblib.load("models/saved_model.pkl")

prediction = model.predict([[150]])

print(prediction)print("Predicting Stock Price...")