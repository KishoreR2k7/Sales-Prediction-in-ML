# 📊 Sales Prediction App

This project predicts **sales (in thousands)** based on advertising spend across three channels: **TV, Radio, and Social Media**.  
It is built with **Python (Scikit-Learn, Ridge Regression)** and deployed as an interactive web app using **Streamlit**.

---

## 🚀 Features
- Upload or input advertising spend values
- Predict sales instantly
- Interactive Streamlit UI
- Pre-trained **Ridge Regression** model
- Scaled inputs using **StandardScaler**

---

## 📂 Project Files
├── advertising_linear_150.csv # Dataset
├── model.pkl # Trained ML model
├── scaler.pkl # Feature scaler
├── app.py # Streamlit application
├── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/sales-prediction-app.git
cd sales-prediction-app
2. Create Virtual Environment (Optional but Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the App
bash
Copy
Edit
streamlit run app.py
📊 Model Training Workflow
Data Preprocessing

Checked for null values & duplicates

Outlier detection using boxplots

Correlation analysis with heatmap

Feature Scaling

Applied StandardScaler to ensure balanced feature input

Model

Used Ridge Regression for robust linear modeling

Split dataset into 80% training & 20% testing

Model Saving

Saved trained model & scaler using pickle

Example code:

python
Copy
Edit
import pickle, numpy as np

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Predict sales for sample input
features = np.array([[94, 40, 23]])
features_scaled = scaler.transform(features)
prediction = model.predict(features_scaled)
print(f"Predicted Sales: {prediction[0]:.2f}k")
🌐 Live Demo
https://salesprediction12.streamlit.app/

<img width="1916" height="930" alt="Screenshot 2025-08-25 001016" src="https://github.com/user-attachments/assets/f492c090-ebde-499b-ac69-22a48e40d106" />

📸 App Preview
Enter TV Spend, Radio Spend, Social Media Spend

Click Predict Sales

Get predicted sales instantly

(Add a screenshot here if available)

🛠️ Tech Stack
Python 3

Pandas, NumPy – Data handling

Seaborn, Matplotlib – Visualization

Scikit-Learn – Ridge Regression & Scaling

Streamlit – Web App

Pickle – Model persistence

🤝 Contributing
Contributions are welcome!
Feel free to fork this repo and submit pull requests to improve the app.
