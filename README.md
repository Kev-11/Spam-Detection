# 📱 Spam Detection using Machine Learning

This is a simple yet effective machine learning project that classifies SMS messages as **Spam** or **Ham (Not Spam)**. Built with Python and Streamlit, the app provides an intuitive interface where users can input a message and instantly get a prediction.

### 🔗 Live Demo
Check out the deployed app here 👉 [spam-detection-sms.streamlit.app](https://spam-detection-sms.streamlit.app)

---

## 🚀 Features

- Predict whether an SMS is Spam or Not Spam
- Clean and interactive Streamlit interface
- Uses a trained machine learning model (Multinomial Naive Bayes)
- Text preprocessing (lowercasing, punctuation removal, stopwords filtering, etc.)

---

## 🧠 Tech Stack

- Python  
- Streamlit  
- Scikit-learn  
- NLTK  
- Pandas  

---

## 📂 Project Structure

```
├── spam_detection_model.pkl     # Trained ML model
├── vectorizer.pkl               # Tfidf vectorizer used during training
├── app.py                       # Main Streamlit application
├── preprocessing.py             # Text preprocessing functions
├── requirements.txt             # List of dependencies
└── README.md                    # This file
```

---

## 🛠️ Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/Kev-11/Spam-Detection.git
cd Spam-Detection
pip install -r requirements.txt
streamlit run app.py
```

---

## ✍️ How it Works

1. Enter an SMS message into the input field.
2. The message is preprocessed and vectorized using the same TF-IDF vectorizer used during training.
3. The model (Multinomial Naive Bayes) predicts whether the message is spam or not.
4. The result is displayed in real-time.

---

## 📈 Model Performance

- Algorithm used: **Multinomial Naive Bayes**
- Accuracy: ~98% on test data
- Dataset: [SMS Spam Collection Dataset (UCI)](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection)

---

## 🤝 Contributing

Feel free to fork the repo, open issues, or submit PRs!

---

## 📬 Contact

If you have any questions or suggestions, feel free to reach out via GitHub.

---
