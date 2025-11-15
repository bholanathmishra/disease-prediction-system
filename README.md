📘 Disease Prediction System Using Machine Learning

This project is a symptom-based disease prediction system built with machine learning.
Users can enter their symptoms, and the model predicts the most likely disease along with basic precautions.
It aims to help with early awareness and faster decision-making, especially in situations where medical guidance is not immediately available.

🔍 Overview

Healthcare professionals often deal with overlapping symptoms that make diagnosis difficult.
This project uses a structured dataset of common diseases and their associated symptoms to train a machine learning model.
The prediction engine is integrated into a simple web interface built with Streamlit.

The goal is to make a tool that is easy to use and provides quick, informative predictions.

🎯 Features

Predicts diseases based on multiple symptom inputs

Machine learning model trained on structured medical data

Clean and simple web interface using Streamlit

Shows possible precautions for the predicted disease

Lightweight, fast, and easy to deploy

🧠 Machine Learning Workflow
1. Dataset

Two datasets were used:

DiseaseAndSymptoms.csv – contains diseases and their associated symptoms

Disease precaution.csv – contains precaution details for each disease

2. Preprocessing

Handling missing values

Normalizing symptom names

Converting categorical values using label encoding

Building feature vectors for each disease

3. Model

Random Forest Classifier

Chosen due to high accuracy and strong performance on categorical/structured data

Achieved strong results during testing

4. Evaluation

Used standard metrics:

Accuracy

Precision

Recall

F1-Score

🧩 Tech Stack

Frontend / UI

Streamlit

Machine Learning

Python

Pandas

NumPy

Scikit-learn

Development Tools

VS Code

Git & GitHub

Virtual Environment (venv)

🚀 Running the Project Locally
1. Clone the repository
git clone https://github.com/bholanathmishra/disease-prediction-system.git

2. Navigate into the project
cd disease-prediction-system

3. Activate virtual environment
.\env\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

5. Run the app
streamlit run app.py

📸 Screenshots (optional)

You can add screenshots of your UI here, for example:

![Home Page](static/images/home.png)

📁 Project Structure
├── app.py
├── DiseaseAndSymptoms.csv
├── Disease precaution.csv
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
├── requirements.txt
└── README.md

📚 Future Enhancements

Add multiple disease suggestions

Include severity level predictions

Deploy to Streamlit Cloud

Add multilingual support

Improve dataset quality

Add model explainability (feature importance)

👤 Author

Bholanath Mishra
Major Project – Disease Prediction System Using Machine Learning
GitHub: https://github.com/bholanathmishra

📝 License

This project is for educational purposes.
Feel free to use or modify it for learning and academic work.
