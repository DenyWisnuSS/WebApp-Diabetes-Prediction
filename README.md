# Diabetes Prediction Web App

This repository contains a web application for predicting diabetes using machine learning. The app is built with **Streamlit** and allows users to input their health metrics to get a prediction of whether they are likely to have diabetes.

## Features

- **User Input**: Users can input their health data (e.g., BMI, age, glucose level, etc.) directly into the web interface.
- **Prediction**: The app predicts the likelihood of diabetes based on the user input using a trained machine learning model.
- **Model**: A pre-trained model using the [PIMA Indian Diabetes Dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database) is used for making predictions.

## Installation

To run this application locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DenyWisnuSS/WebApp-Diabetes-Prediction.git

2. **Navigate to the project directory**
   cd WebApp-Diabetes-Prediction

3. **Install the required dependencies**
   pip install -r requirements.txt
4. **Run the streamlit app**
   streamlit run app.py

## Project Structure

- app.py                   # Main application file
- SVC_model.sav            # Pre-trained machine learning model
- requirements.txt         # Required Python packages
- README.md                # Project documentation
- data
