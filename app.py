import streamlit as st
import pickle, re

st.title("📄 Resume Category Predictor")
st.write("Upload or paste resume text to predict job category")

model = pickle.load(open("resume_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

resume_text = st.text_area("Paste resume text here:")

if st.button("Predict Category"):
    text = re.sub(r'[^a-zA-Z\s]', '', resume_text.lower())
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    st.success(f"Predicted Category: **{pred}** 🎯")
