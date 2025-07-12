# 🧪 Smart Ingredient Watchdog

An intelligent system to detect and analyze food product ingredients using OCR and NLP, helping users identify harmful or restricted ingredients in packaged foods.

---

## 📌 Table of Contents

- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## ✅ About

The **Smart Ingredient Watchdog** helps health-conscious consumers scan food product labels and automatically flag any ingredients that are harmful, restricted, or allergenic based on an internal database.  
It uses:
- **OCR (Tesseract)** to extract text from images of ingredient lists.
- **NLP** to process and match ingredient keywords.
- **ML model** to predict if an ingredient might be risky.
- **Streamlit web app** to provide an easy-to-use interface.

---

## ✨ Features

- 📷 Upload an image of any food product’s ingredient list.
- 🔍 Extract and parse text using OCR.
- 🧠 Classify and highlight harmful/restricted ingredients.
- 📊 Shows safe/unsafe summary and suggestions.
- ☁️ Deployed on Streamlit Cloud for easy access.

---

## ⚙️ Tech Stack

| Area              | Tech Used                                       |
|-------------------|-------------------------------------------------|
| Programming       | Python                                          |
| OCR               | Tesseract OCR                                   |
| NLP               | spaCy, scikit-learn                             |
| ML Model          | XGBoost / custom classifier                     |
| Web Framework     | Streamlit                                       |
| Deployment        | Streamlit Cloud / Heroku / AWS EC2              |

---

## 🚀 Demo

🔗 [Add a link to your deployed Streamlit app]

📷 Add screenshots or GIF of the app in action!

---

## 🛠️ Installation

```bash
# Clone this repo
git clone https://github.com/yourusername/smart-ingredient-watchdog.git
cd smart-ingredient-watchdog

# Create virtual env & activate
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

---

## 🧩 Usage

1. Upload an image of an ingredient list (product packaging).
2. The app extracts text using Tesseract.
3. NLP pipeline matches ingredients to the internal database.
4. Unsafe ingredients are flagged and highlighted.
5. The user gets a final summary with risk level.

---

## 📂 Project Structure

```
smart-ingredient-watchdog/
│
├── data/                 # Ingredient database, samples
├── models/               # Trained vectorizer, classifier
├── app.py                # Main Streamlit app
├── utils.py              # Helper functions (OCR, NLP)
├── requirements.txt      # Python dependencies
└── README.md             # Project README
```

---

## 🔭 Future Improvements

- Add support for multi-language ingredient lists.
- Expand ingredient risk database.
- Allow user profiles & ingredient preferences.
- Build mobile app version.
- Integrate barcode scanner.

---

## 🤝 Contributing

Pull requests are welcome!
1. Fork the repo
2. Create your branch: `git checkout -b feature/awesome-feature`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature/awesome-feature`
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for details.

---

**Developed with ❤️ by [Anand Kumar]**
