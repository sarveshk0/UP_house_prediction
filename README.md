# 🏠 Uttar Pradesh House Price Prediction App
You can see at-
https://up-house-prediction.onrender.com/
This project is a web-based machine learning app that predicts house prices in cities of Uttar Pradesh using a trained Ridge Regression model. It has a simple Flask backend and a Bootstrap-powered frontend.

---




---

## ⚙️ Requirements

Make sure Python is installed (recommended version: 3.8+).

Install dependencies in a virtual environment:


"python -m venv venv"
"venv\Scripts\activate"      # Windows
"source venv/bin/activate"  # macOS/Linux

"pip install -r requirements.txt"



If requirements.txt doesn't exist, install manually:

"pip install flask pandas numpy scikit-learn jupyter"




How to Start
🔢 1. Run the Jupyter Notebook
To view and run the data preprocessing or model training notebook:...
"jupyter notebook"
Then open notebook.ipynb in your browser and run the cells step by step.

🌐 2. Run the Flask App
Once the model is trained and saved (RidgeModel.pkl):


"python main.py"
App will start at:
http://127.0.0.1:5000/
Use the web form to enter the city, apartment details, and area to predict the price.


