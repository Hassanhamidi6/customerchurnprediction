from flask import Flask, render_template, jsonify, request
import joblib
import pandas as pd

# Load Model
model = joblib.load(r"artifacts\data_ingestion\model.pkl")

# Define feature column names (same as training data)
FEATURE_COLUMNS = ['CreditScore', 'Gender', 'Age', 'Tenure', 'Balance', 'HasCrCard']

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    labels = ['Present', 'Not Present']
    response = request.json
    
    # Extract input features
    data = {
        "CreditScore": [response['CreditScore']],
        "Gender": [0 if response['Gender'] == "Female" else 1],
        "Age": [response['Age']],
        "Tenure": [response['Tenure']],
        "Balance": [response['Balance']],
        "HasCrCard": [response['HasCrCard']]
    }
    
    # Convert to DataFrame with column names
    input_df = pd.DataFrame(data, columns=FEATURE_COLUMNS)
    
    # Predict
    prediction = model.predict(input_df)[0]
    
    return jsonify({"prediction": labels[int(prediction)]})

if __name__ == "__main__":
    app.run()
