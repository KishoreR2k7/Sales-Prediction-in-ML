# 📊 Sales Prediction App

A machine learning web application that predicts **sales (in thousands)** based on advertising spend across **TV, Radio, and Social Media** channels.  
Built with **Scikit-Learn (Ridge Regression)** and deployed using **Streamlit**.

---

## ✨ Key Features
- Predicts sales based on advertising spend inputs
- Interactive **Streamlit UI**
- Pre-trained **Ridge Regression** model
- Scaled inputs using **StandardScaler**
- Fast and lightweight deployment

---

## 📂 Repository Structure


├── advertising_linear_150.csv # Dataset
├── model.pkl # Trained Ridge Regression model
├── scaler.pkl # StandardScaler for features
├── app.py # Streamlit application
├── requirements.txt # Project dependencies
└── README.md # Documentation



## ⚙️ Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/your-username/sales-prediction-app.git
cd sales-prediction-app
2. (Optional) Create Virtual Environment 
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the Application
```

streamlit run app.py
🧠 Model Workflow
Data Preprocessing

Checked missing values & duplicates

Outlier detection with boxplots

Correlation analysis with heatmap

Feature Engineering

Scaled features using StandardScaler

Model Training

Algorithm: Ridge Regression

Split: 80% training / 20% testing

Model Saving

Stored trained model (model.pkl) and scaler (scaler.pkl) with pickle

Example usage:
```
python
import pickle, numpy as np

# Load model & scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Sample input: [TV Spend, Radio Spend, Social Media Spend]
features = np.array([[94, 40, 23]])
features_scaled = scaler.transform(features)

# Predict
prediction = model.predict(features_scaled)
print(f"Predicted Sales: {prediction[0]:.2f}k")

```
🌐 Live Demo
<p align="center">
  <a href="https://salesprediction12.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/🚀%20Launch%20App-Streamlit-brightgreen?style=for-the-badge&logo=streamlit" alt="Launch App">
  </a>
</p>

---📸 App Preview

(Replace the placeholder with your actual screenshot — e.g., assets/app_preview.png if added to repo)

🛠️ Tech Stack
Python 3.9+

NumPy, Pandas → Data Processing

Seaborn, Matplotlib → Visualization

Scikit-Learn → ML Model (Ridge Regression)

Streamlit → Web App Deployment

Pickle → Model Persistence

🤝 Contributing
Contributions are welcome! 🚀
If you’d like to improve this project, fork the repo, create a feature branch, and submit a pull request.
