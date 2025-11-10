# 📄 Resume Category Predictor — Veridia Data Analytics Project

### 🚀 Objective
Veridia aims to improve **data-driven recruitment** decisions by analyzing and classifying resumes automatically.  
This project performs:
- Resume text extraction  
- Data cleaning & preprocessing  
- Exploratory Data Analysis (EDA)  
- Predictive modeling to **categorize resumes** into job sectors  
- A **Streamlit dashboard** for interactive prediction  

---

## 📊 Dataset
**Source:** [Kaggle Resume Dataset](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset)  
Additionally, a folder containing **category-wise PDF resumes** was used to extract text data programmatically using `pdfplumber`.


---

## ⚙️ Features Implemented
✅ Data Cleaning & Preprocessing  
✅ PDF Text Extraction (using `pdfplumber`)  
✅ Exploratory Data Analysis  
✅ TF–IDF Vectorization  
✅ Logistic Regression Classifier  
✅ Interactive Streamlit Web App  
✅ Category Prediction for Any Resume  

---

## 🧠 Tech Stack
| Component | Tool / Library |
|------------|----------------|
| Language | Python |
| Data Handling | Pandas, NumPy |
| NLP | NLTK, scikit-learn (TF-IDF) |
| Visualization | Matplotlib, Seaborn |
| Model | Logistic Regression |
| Web App | Streamlit |
| PDF Processing | pdfplumber |

---

## 📁 Project Structure
veridia_resume_analysis/
│
├── extract_pdfs.py # Extract text from category-wise PDFs
├── preprocess_train.py # Clean data, train model, save pickle files
├── app.py # Streamlit frontend
├── pdf_resume_data.csv # Generated dataset
├── resume_model.pkl # Saved trained model
├── vectorizer.pkl # TF-IDF vectorizer
├── requirements.txt
└── README.md



---

## 🧩 Model Overview
- **Vectorizer:** TF–IDF (Top 5000 features)
- **Model:** Logistic Regression (class-weight balanced)
- **Accuracy:** ~85–90% (depending on dataset quality)
- **Goal:** Predict the job category of a resume based on textual content.

---

## 📷 Screenshots

### 🧠 Streamlit Web App Interface
Below is the working demo of the resume predictor:

![Resume Predictor Screenshot](assets/app_screenshot.png)

> *(Replace this image path with your actual screenshot file — e.g., the one you uploaded earlier.)*

Example Output:

> **Predicted Category: AGRICULTURE 🌾**

![App Screenshot Example](assets/app_output.png)

---

## 🧰 How to Run Locally

### 1️⃣ Clone or Download the Repo
```bash
git clone https://github.com/sanjanasulakhe_23/veridia-resume-analysis.git
cd veridia-resume-analysis
2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Extract Data from PDFs
python extract_pdfs.py

4️⃣ Train and Save Model
python preprocess_train.py

5️⃣ Run the Streamlit App
streamlit run app.py


👩‍💻 Author

Sanjana Sulakhe
Data Science & Machine Learning Enthusiast
📧 sanjanasulakhe23@gmail.com

