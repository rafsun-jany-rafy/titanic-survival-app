# 🚢 Titanic Survival Prediction App

A Machine Learning web application that predicts whether a passenger would survive the Titanic disaster based on passenger details such as age, sex, class, fare, and embarkation port.

---

## 🌐 Live Demo

[Click Here to Open the App](https://titanic-disaster-survival-app.streamlit.app/)

---

## 📌 Project Overview

This project uses a trained Machine Learning model to predict Titanic passenger survival probability. The application takes user inputs through a web interface and returns a prediction instantly.

The model was trained using the famous Titanic dataset from Kaggle.

---

## 🧠 Features

- Predict Titanic passenger survival
- User-friendly web interface
- Real-time prediction
- Machine Learning powered
- Data preprocessing and categorical encoding
- Lightweight and easy to deploy

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

## 📂 Project Structure

```bash
├── app.py
├── model.pkl
├── titanic.ipynb
├── requirements.txt
├── README.md
├── LICENSE
└── Titanic-Dataset.csv
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/titanic-survival-app.git
cd titanic-survival-app
```



### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application



### Streamlit

```bash
streamlit run app.py
```

---

## 📊 Input Features

The model uses the following passenger information:

- Passenger Class (Pclass)
- Sex
- Age
- Number of Siblings/Spouses Aboard
- Number of Parents/Children Aboard
- Fare
- Embarked Port

---

## 🔄 Categorical Encoding

Example encoding used in the project:

```python
sex_encoded = 1 if sex == 'Female' else 0

embarked_encoded = {
    'S = Southampton': 0,
    'C = Cherbourg': 1,
    'Q = Queenstown': 2,
}[embarked]
```

---

## 🎯 Model Performance

- Accuracy: 85%
- Algorithm Used: *RandomForestRegressor*


---

## 🌐 Deployment

This project can be deployed on:

- Render
- Railway
- Hugging Face Spaces
- Heroku

---

## 📸 Screenshots

<img width="1912" height="870" alt="1Screenshot 2026-05-11 160258" src="https://github.com/user-attachments/assets/1bfbcc0d-7c4a-4f90-b97c-d9353ac74ff6" />
<img width="1907" height="867" alt="2Screenshot 2026-05-11 160403" src="https://github.com/user-attachments/assets/1eee3db1-0f79-4ff9-8978-5b1b426ef99b" />


---

## 📁 Dataset

Dataset used:

Titanic Dataset from Kaggle  
https://www.kaggle.com/datasets/yasserh/titanic-dataset

---

## 👨‍💻 Author

GitHub: https://github.com/rafsun-jany-rafy

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
