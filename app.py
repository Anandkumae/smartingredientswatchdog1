import streamlit as st
import pytesseract
import cv2
import numpy as np
import pickle
import spacy
import subprocess
from sklearn.feature_extraction.text import CountVectorizer
from xgboost import XGBClassifier
from PIL import Image

# ✅ 1️⃣ Load spaCy model with fallback — OK
def get_nlp():
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
        return spacy.load("en_core_web_sm")

nlp = get_nlp()

# ✅ 2️⃣ This is only valid for LOCAL Windows — NOT for Streamlit Cloud!
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ⚠️ On Streamlit Cloud, the Tesseract binary is NOT installed.
# So `pytesseract` will fail unless you use a custom backend that works in pure Python.
# Streamlit Cloud does NOT allow `apt-get install tesseract-ocr` anymore.

# ✅ 3️⃣ Load your models and vectorizer — OK
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# ✅ 4️⃣ Streamlit UI
st.title("Smart Ingredient Watchdog")

uploaded_file = st.file_uploader("Upload Product Label Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Label', use_column_width=True)

    # ✅ 5️⃣ OCR — this works LOCALLY only if Tesseract is installed
    image_np = np.array(image)
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    st.write("**Extracted Text:**")
    st.write(text)

    # ✅ 6️⃣ NLP
    doc = nlp(text.lower())
    ingredients = list(set([token.text for token in doc if token.is_alpha]))
    st.write("**Detected Ingredients:**")
    st.write(ingredients)

    # ✅ 7️⃣ Prediction
    X_new = vectorizer.transform(ingredients)
    preds = model.predict(X_new)

    results = [(ingredient, int(label)) for ingredient, label in zip(ingredients, preds)]

    st.write("**Ingredient Safety Labels:**")
    for ingredient, label in results:
        st.write(f"{'✅' if label == 0 else '⚠️'} **{ingredient}** → Label: {label} ({'Safe' if label == 0 else 'Harmful'})")

    safe_ingredients = [ingredient for ingredient, label in results if label == 0]
    harmful_ingredients = [ingredient for ingredient, label in results if label == 1]

    st.write("### ✅ Safe Ingredients:")
    st.write(safe_ingredients if safe_ingredients else "None detected.")

    st.write("### ⚠️ Harmful Ingredients:")
    st.write(harmful_ingredients if harmful_ingredients else "None detected.")





