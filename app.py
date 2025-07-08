import streamlit as st
import pytesseract
import cv2
import numpy as np
import spacy
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from xgboost import XGBClassifier
from PIL import Image

# Load NLP model
nlp = spacy.load("en_core_web_sm")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load trained models and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.title("Smart Ingredient Watchdog")

uploaded_file = st.file_uploader("Upload Product Label Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Label', use_column_width=True)

    # OCR
    image_np = np.array(image)
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    st.write("**Extracted Text:**")
    st.write(text)

    # NLP
    doc = nlp(text.lower())
    ingredients = list(set([token.text for token in doc if token.is_alpha]))
    st.write("**Detected Ingredients:**")
    st.write(ingredients)

    # Prediction
    X_new = vectorizer.transform(ingredients)
    preds = model.predict(X_new)

    # Combine with labels: 0 = Safe, 1 = Harmful
    results = [(ingredient, int(label)) for ingredient, label in zip(ingredients, preds)]

    st.write("**Ingredient Safety Labels:**")
    for ingredient, label in results:
        st.write(f"{'✅' if label == 0 else '⚠️'} **{ingredient}** → Label: {label} ({'Safe' if label == 0 else 'Harmful'})")

    # Separate safe and harmful ingredients
    safe_ingredients = [ingredient for ingredient, label in results if label == 0]
    harmful_ingredients = [ingredient for ingredient, label in results if label == 1]

    st.write("### ✅ Safe Ingredients:")
    if safe_ingredients:
        st.write(safe_ingredients)
    else:
        st.write("None detected.")

    st.write("### ⚠️ Harmful Ingredients:")
    if harmful_ingredients:
        st.write(harmful_ingredients)
    else:
        st.write("None detected.")





