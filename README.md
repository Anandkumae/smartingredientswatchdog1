Smartingredientswatchdog
🥫 Smart Ingredient Watchdog
Smart Ingredient Watchdog is a Streamlit web app that scans food product labels, extracts ingredients using OCR, analyzes them with NLP, and predicts whether each ingredient is Safe or Harmful using a trained machine learning model.

📌 Features
✅ Upload a product label image (JPEG, PNG)

✅ Automatically extract text from the image using Tesseract OCR

✅ Detect ingredients with spaCy NLP

✅ Predict ingredient safety with an XGBoost classifier

✅ Label ingredients as:

0 → ✅ Safe
1 → ⚠️ Harmful
✅ Display clear, separate lists for Safe and Harmful ingredients

📂 Project Structure
smartingredientswatchdog/
 ├── app.py
 ├── model.pkl
 ├── vectorizer.pkl
 ├── requirements.txt
 ├── README.md
