from flask import Flask, request, render_template, send_file
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Load the model and scaler
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def category():
    return render_template('contact.html')

@app.route('/features')
def work():
    return render_template('features.html')

@app.route('/predict_file', methods=['POST'])
def predict_file():
    file = request.files.get('file')
    if not file or file.filename == '':
        return "No file uploaded", 400

    try:
        data = pd.read_csv(file)
        features = data.drop('Class', axis=1, errors='ignore')
        features_scaled = scaler.transform(features)
        predictions = model.predict(features_scaled)
    except Exception as e:
        return f"Error processing file: {str(e)}", 500

    results = pd.DataFrame({'Prediction': predictions})

    try:
        # Generate graph
        fraud_count = results['Prediction'].value_counts()
        fig, ax = plt.subplots()
        fraud_count.plot(kind='bar', ax=ax)
        ax.set_title('Fraudulent vs Non-Fraudulent Transactions')
        ax.set_xlabel('Class')
        ax.set_ylabel('Count')

        # Save plot to a bytes object
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    except Exception as e:
        return f"Error generating plot: {str(e)}", 500

    return render_template('results.html', tables=[results.to_html()], plot_url=plot_url)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
