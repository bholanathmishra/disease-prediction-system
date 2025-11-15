import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Disease Prediction System", layout="wide")

# ================= Load Data ==================
disease_data = pd.read_csv("DiseaseAndSymptoms.csv")
precaution_data = pd.read_csv("Disease precaution.csv")

disease_data.fillna("", inplace=True)
precaution_data.fillna("", inplace=True)

symptom_cols = [c for c in disease_data.columns if "Symptom" in c]
all_symptoms = sorted(list({s.strip() for col in symptom_cols for s in disease_data[col].unique() if isinstance(s, str) and s.strip() != ""}))

# ================= Helper Functions ==================

def extract_symptoms(row):
    temp = []
    for col in symptom_cols:
        if isinstance(row[col], str) and row[col].strip() != "":
            temp.append(row[col].strip())
    return temp

def disease_similarity(user, disease_sym):
    return len(set(user).intersection(set(disease_sym)))

def best_match(user_sym_list):
    best = None
    high = -1
    for _, row in disease_data.iterrows():
        ds = extract_symptoms(row)
        score = disease_similarity(user_sym_list, ds)
        if score > high:
            high = score
            best = row["Disease"]
    return best

def fetch_precautions(dis):
    res = precaution_data[precaution_data["Disease"] == dis]
    if res.empty:
        return []
    r = res.iloc[0]
    return [r[f"Precaution_{i}"] for i in range(1,5) if f"Precaution_{i}" in r and isinstance(r[f"Precaution_{i}"], str) and r[f"Precaution_{i}"].strip() != ""]

# ================= UI Functions ==================

def draw_header():
    st.markdown(
        """
        <div style='background-color:#4e8cff;padding:25px;border-radius:12px'>
            <h1 style='text-align:center;color:white;font-size:44px;margin-bottom:0px'>🩺 Disease Prediction System</h1>
            <p style='text-align:center;color:white;font-size:18px;margin-top:0px'>Professional AI Health Tool</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)

def draw_sidebar():
    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Go to", ["Home", "Predict Disease", "Statistics", "About", "Developer"])
    return choice

# ================= Pages ========================

def home_page():
    st.markdown("## Welcome to Disease Prediction System")
    st.markdown(
        """
        Predict possible diseases based on symptoms and patient information.

        """
    )
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Core Features")
    col1, col2, col3 = st.columns(3)
    col1.success("✔ Patient Form")
    col2.info("✔ AI Prediction")
    col3.warning("✔ Precaution Guidance")
    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("Quick Stats")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Diseases", len(disease_data["Disease"].unique()))
    c2.metric("Total Symptoms", len(all_symptoms))
    c3.metric("Precaution Records", len(precaution_data))
    c4.metric("Prediction Accuracy", "Simulated 95%")

def extended_patient_form():
    st.subheader("Patient Information Form")
    with st.form("patient_form"):
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        weight = st.number_input("Weight (kg)", min_value=1, max_value=300)
        height = st.number_input("Height (cm)", min_value=30, max_value=250)
        blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
        medical_history = st.text_area("Medical History / Past Diseases")
        allergies = st.text_area("Known Allergies")
        medications = st.text_area("Current Medications")
        lifestyle = st.text_area("Lifestyle / Habits")
        family_history = st.text_area("Family Medical History")
        emergency_contact = st.text_input("Emergency Contact Number")
        symptoms = st.multiselect("Select Symptoms (1–2 recommended)", all_symptoms, max_selections=2)

        submitted = st.form_submit_button("Submit & Predict")
    return submitted, name, age, gender, weight, height, blood_group, medical_history, allergies, medications, lifestyle, family_history, emergency_contact, symptoms

def predict_page():
    submitted, name, age, gender, weight, height, blood_group, medical_history, allergies, medications, lifestyle, family_history, emergency_contact, symptoms = extended_patient_form()
    st.markdown("<br>", unsafe_allow_html=True)
    if submitted:
        if not symptoms:
            st.warning("Please select at least one symptom.")
            return
        with st.spinner("Analyzing symptoms..."):
            time.sleep(1)
            disease = best_match(symptoms)
            precautions = fetch_precautions(disease)
        st.success(f"### Predicted Disease: {disease}")
        if precautions:
            st.info("### Recommended Precautions:")
            for p in precautions:
                st.write(f"- {p}")
        else:
            st.warning("No precautions available.")

        st.markdown("### Patient Summary")
        st.write(f"- Name: {name}")
        st.write(f"- Age: {age}")
        st.write(f"- Gender: {gender}")
        st.write(f"- Weight: {weight} kg")
        st.write(f"- Height: {height} cm")
        st.write(f"- Blood Group: {blood_group}")
        st.write(f"- Medical History: {medical_history}")
        st.write(f"- Allergies: {allergies}")
        st.write(f"- Medications: {medications}")
        st.write(f"- Lifestyle: {lifestyle}")
        st.write(f"- Family History: {family_history}")
        st.write(f"- Emergency Contact: {emergency_contact}")

        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("Selected Symptoms")
        for s in symptoms:
            st.write(f"- {s}")

def statistics_page():
    st.subheader("Statistics & Charts")
    disease_counts = disease_data["Disease"].value_counts().head(50)
    st.bar_chart(disease_counts)

    symptom_counts = {}
    for col in symptom_cols:
        for s in disease_data[col]:
            if s != "" and isinstance(s, str):
                symptom_counts[s] = symptom_counts.get(s,0)+1
    top_symptoms = dict(sorted(symptom_counts.items(), key=lambda x: x[1], reverse=True)[:50])
    st.line_chart(pd.DataFrame(top_symptoms.values(), index=top_symptoms.keys()))

def about_page():
    st.markdown("## About This Project")
    st.markdown(
        """
        This is a professional AI-powered disease prediction system.
        
        """
    )

def developer_page():
    st.markdown("## Developer Info")
    st.markdown(
        """
        Name: BHOLANATH MISHRA
        Role: Full Stack PYTHON Developer
        Experience: 1 years
        LinkedIn: https://www.linkedin.com/in/bholanath-mishra
        GitHub: https://github.com/bholanath
        """
    )

# ================== Main ======================

draw_header()
page_choice = draw_sidebar()

if page_choice == "Home":
    home_page()
elif page_choice == "Predict Disease":
    predict_page()
elif page_choice == "Statistics":
    statistics_page()
elif page_choice == "About":
    about_page()
elif page_choice == "Developer":
    developer_page()
