import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
import joblib
import sklearn

st.header("Analisis Prediksi Mahasiswa yang Drop Out")
st.markdown("Aplikasi ini dugunakan untuk menganalisis mahasiswa yang kemungkinan melakukan drop out untuk segera mendapatkan penanganan khusus")

st.subheader("Input data sesuai dengan kolom yang diminta")

# Input features
curricular_units_1st_sem_approved = st.number_input("Curricular Units 1st Sem Approved", min_value=0, max_value=100, value=0)
curricular_units_1st_sem_enrolled = st.number_input("Curricular Units 1st Sem Enrolled", min_value=0, max_value=100, value=0)
curricular_units_1st_sem_grade = st.number_input("Curricular Units 1st Sem Grade", min_value=0.0, max_value=20.0, value=0.0)
curricular_units_2nd_sem_approved = st.number_input("Curricular Units 2nd Sem Approved", min_value=0, max_value=100, value=0)
curricular_units_2nd_sem_enrolled = st.number_input("Curricular Units 2nd Sem Enrolled", min_value=0, max_value=100, value=0)
curricular_units_2nd_sem_grade = st.number_input("Curricular Units 2nd Sem Grade", min_value=0.0, max_value=20.0, value=0.0)
admission_grade = st.number_input("Admission Grade", min_value=0.0, max_value=200.0, value=0.0)
tuition_fees_up_to_date = st.selectbox("Tuition Fees Up to Date", options=['Yes', 'No'])
scholarship_holder = st.selectbox("Scholarship Holder", options=['Yes', 'No'])
displaced = st.selectbox("Displaced", options=['Yes', 'No'])
previous_qualification_grade = st.selectbox("Previous Qualification Grade", options=[1, 2, 3, 4, 5, 6, 9, 10, 19, 38, 39, 40, 42, 43])
application_mode = st.selectbox("Application Mode", options=[1, 2, 5, 7, 10, 15, 16, 17, 26, 27, 39, 42, 43, 44, 51, 53, 57])
gender = st.selectbox("Gender", options=["Male", "Female"])
debtor = st.selectbox("Debtor", options=['Yes', 'No'])
age_at_enrollment = st.number_input("Age at Enrollment", min_value=0, max_value=100, value=0)

# Membuat dataframe untuk input data
input_data = pd.DataFrame({
    'Curricular_units_2nd_sem_approved': [curricular_units_2nd_sem_approved],
    'Curricular_units_2nd_sem_grade': [curricular_units_2nd_sem_grade],
    'Curricular_units_1st_sem_approved': [curricular_units_1st_sem_approved],
    'Curricular_units_1st_sem_grade': [curricular_units_1st_sem_grade],
    'Tuition_fees_up_to_date': [1 if tuition_fees_up_to_date == 'Yes' else 0],
    'Scholarship_holder': [1 if scholarship_holder == 'Yes' else 0],
    'Curricular_units_2nd_sem_enrolled': [curricular_units_2nd_sem_enrolled],
    'Curricular_units_1st_sem_enrolled': [curricular_units_1st_sem_enrolled],
    'Admission_grade': [admission_grade],
    'Displaced': [1 if displaced == 'Yes' else 0],
    'Previous_qualification_grade': [previous_qualification_grade],
    'Application_mode': [application_mode],
    'Gender': [1 if gender == "Male" else 0],
    'Debtor': [1 if debtor == 'Yes' else 0],
    'Age_at_enrollment': [age_at_enrollment]
})

# Menampilkan input data 
st.subheader("Input Data")
st.write(input_data)
st.markdown("Pastikan data yang dimasukan sudah sesuai dengan kolom yang diminta")

# Load model dan melakukan prediksi
if st.button("Prediksi Drop Out"):
    try:
        model = joblib.load('model/rf_model.pkl')
        prediction = model.predict(input_data)
        st.subheader("Hasil Prediksi")
        if prediction[0] == 0:
            st.error("⚠️ The student is **likely to drop out**. Please take preventive action.")
        else:
            st.success("✅ The student is **likely to continue** their studies.")
    except Exception as e:
        st.error(f"Something went wrong: {e}")
