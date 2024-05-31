import pickle
import streamlit as st
import numpy as np

# Membaca model
diabetes_model = pickle.load(open('decision_tree.sav', 'rb'))

# Judul web
st.title('Sistem Prediksi Penyakit Diabetes')

# Deskripsi web
st.write("""
Aplikasi ini berbasis Machine Learning dengan menggunakan model ensemble yang telah dilatih pada kumpulan data diabetes. Aplikasi ini dapat memprediksi apakah seseorang terkena diabetes atau tidak, berdasarkan nilai **Glucose, BMI, dan Usia**.

**Cara menggunakan aplikasi:**

1. Masukkan nilai Glucose dan BMI Anda.
2. Klik tombol "Prediksi".
3. Aplikasi akan menampilkan hasil prediksi, apakah Anda terkena diabetes atau tidak.
""")
# Input untuk nilai-nilai variabel
# Membagi kolom
col1, col2 = st.columns(2)

with col1:
    Glucose = st.number_input('Input nilai Glucose (mg/dL)', value=None, key='Glucose')

with col2:
    BMI = st.number_input('Input nilai BMI (kg/m^2)', value=None, key='BMI')

# Code untuk prediksi
diabetes_diagnosis = ''

# Tombol untuk prediksi
if st.button('Prediksi'):
    try:
        # Mengonversi input ke tipe numerik
        data_input = np.array([[Glucose, BMI]])

        # Prediksi menggunakan model
        diabetes_prediction = diabetes_model.predict(data_input)

        # Menampilkan hasil prediksi
        if diabetes_prediction[0] == 0:
            diabetes_diagnosis = 'Pasien Tidak Terkena Diabetes'
            color = 'green'
        else:
            diabetes_diagnosis = 'Pasien Terkena Diabetes'
            color = 'red'

        # Menampilkan prediksi dengan warna latar belakang yang sesuai dan border yang lebih berjarak
        st.markdown(
            f'<div style="background-color:{color}; padding: 10px; border-radius: 5px; margin-bottom: 10px;"><b>{diabetes_diagnosis}</b></div>',
            unsafe_allow_html=True)

    except ValueError:
        st.error('Pastikan semua input adalah angka.')
    except Exception as e:
        st.error(f'Terjadi kesalahan: {e}')
