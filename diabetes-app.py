import pickle
import numpy as np
import streamlit as st

# Load the trained model
with open('random_forest_model.sav', 'rb') as model_file:
    diabetes_model = pickle.load(model_file)

# Title of the web app
st.title('Sistem Prediksi Penyakit Diabetes')

# Description of the web app
st.write("""
Aplikasi ini berbasis Machine Learning dengan menggunakan model yang telah dilatih pada kumpulan data diabetes. Aplikasi ini dapat memprediksi apakah seseorang terkena diabetes atau tidak, berdasarkan nilai **Glucose dan BMI**.

**Cara menggunakan aplikasi:**

1. Masukkan nilai Glucose dan BMI Anda.
2. Klik tombol "Prediksi".
3. Aplikasi akan menampilkan hasil prediksi, apakah Anda terkena diabetes atau tidak, serta akurasi prediksi dari data tersebut.
""")

# Input for the variables
col1, col2 = st.columns(2)

with col1:
    Glucose = st.number_input('Input nilai Glucose (mg/dL)', value=0, step=1, key='Glucose')

with col2:
    BMI = st.number_input('Input nilai BMI (kg/m^2)', value=0.0, step=0.1, key='BMI')

# Code for prediction
diabetes_diagnosis = ''

# Button for prediction
if st.button('Prediksi'):
    try:
        if Glucose is None or BMI is None:
            raise ValueError("Masukkan nilai untuk kedua input.")

        # Convert input to numeric type
        Glucose_float = float(Glucose)
        BMI_float = float(BMI)
        data_input = np.array([[Glucose_float, BMI_float]])
        
        # Prediction using the model
        diabetes_prediction = diabetes_model.predict(data_input)
        st.write(f"Model prediction: {diabetes_prediction}")  # Debugging line

        # Display the prediction result
        if diabetes_prediction[0] == 0:
            diabetes_diagnosis = 'Pasien Tidak Terkena Diabetes'
            color = 'green'
        else:
            diabetes_diagnosis = 'Pasien Terkena Diabetes'
            color = 'red'

        # Display prediction with appropriate background color
        st.markdown(
            f'<div style="background-color:{color}; padding: 10px; border-radius: 5px; margin-bottom: 10px;"><b>{diabetes_diagnosis}</b></div>',
            unsafe_allow_html=True)

    except ValueError as ve:
        st.error(str(ve))
    except Exception as e:
        st.error(f'Terjadi kesalahan: {e}')
