Chest X-Ray Pneumonia Detection

A Deep Learning Web App for Pneumonia Classification using FastAPI

Overview

This project detects Pneumonia from Chest X-Ray images using a Deep Learning Sequential model.
The model is saved as .keras file and the app uses FastAPI to provide a simple web interface.
Users can upload an image and get real-time predictions directly from the browser.

Features

✅ Deep Learning model trained on Chest X-Ray dataset
✅ FastAPI web app for real-time predictions
✅ Simple user-friendly interface (index.html)
✅ Binary classification: Pneumonia / Normal
✅ Easy to run, beginner-friendly


Technologies Used

Python
TensorFlow / Keras
FastAPI
Jinja2 Templates
HTML / Tailwind CSS


Project Structure

chest-xray-pneumonia-detection/
│
├── code/
│    └── chest_xray_project.ipynb
│
├── model/
│    └── chest_xray_model.keras
│
├── templates/
│    └── index.html
│
├── app.py
├── requirements.txt
└── README.md

1️⃣Navigate to the project folder

cd chest-xray-pneumonia-detection


2️⃣Installation & Run Guide
   Clone the repository

 git clone https://github.com/AzeemAIDev/chest-xray-pneumonia-detection.git

3️⃣pip install -r requirements.txt

4️⃣ Run the FastAPI app


5️⃣Open the Web Interface

* After running the app, open the browser and go to


 Model Information

* Model Type: Sequential Deep Learning Model

* Task: Binary Classification (Pneumonia / Normal)

* Saved As: chest_xray_model.keras

 Author

* Muhammad Azeem
* Machine Learning Engineer & AI Learner
* GitHub: AzeemAIDev
