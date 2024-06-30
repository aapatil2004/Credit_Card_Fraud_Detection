# Credit Card Fraud Detection with Flask

Welcome to the Credit Card Fraud Detection project. This repository contains the code for a web application built using Flask to detect credit card fraud. The application uses machine learning models to analyze transactions and predict whether they are fraudulent or not.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model](#model)
- [Contributing](#contributing)

## Introduction

Credit card fraud detection is crucial in protecting consumers and financial institutions from financial losses. This project leverages machine learning algorithms to predict fraudulent transactions based on historical data.

## Features

- Predict whether a transaction is fraudulent or not using a pre-trained machine learning model.
- Simple and user-friendly web interface built with Flask.
- User registration and login functionality.
- Protected routes accessible only after logging in.
- CSRF protection enabled for all forms using Flask-WTF.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.7+
- pip (Python package installer)
- Virtualenv (optional)

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/credit-card-fraud-detection.git
    cd credit-card-fraud-detection
    ```

2. **Create and activate a virtual environment (optional):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. **Run the application:**

    ```bash
    python app.py
    ```

    The application will be available at `http://127.0.0.1:5000/`.

### Web Interface

1. Navigate to `http://127.0.0.1:5000/` in your web browser.
2. Register a new user or log in with existing credentials.
3. Enter the transaction details on the features page.
4. Click the "Predict" button to see if the transaction is fraudulent or not.

## Dataset

The dataset used for training the machine learning model is not included in this repository due to size constraints. You can download a credit card fraud detection dataset from [this Google Drive link](https://drive.google.com/drive/folders/1aFhESGez12FMUmDD2kbaBbGR5ewF5-yF).

## Model

The machine learning model used in this project is XGBoost. You can train your own model using the given dataset and update the application accordingly.

## Contributing

We welcome contributions! Please fork the repository and submit a pull request for any improvements or new features.

## License

This project is licensed under the MIT License.
