import streamlit as st
import pickle
from PIL import Image

def main():
    st.title(':rainbow[Lung Cancer Prediction]')
    img = Image.open('download lungs.jpeg')
    st.image(img,width=600)
    age = st.text_input('Enter Your Age:')
    smoke = st.text_input('Average number of cigerates in a day:', )
    area = st.text_input('Enter the air quality in your area:')
    alcohol = st.text_input('Enter average alcohol consumption in a day:')
    features = [age,smoke,area,alcohol]
    model = pickle.load(open('Model_lung_cancer.sav','rb'))
    scale = pickle.load(open('scaler_lung_cancer.sav','rb'))
    pred = st.button('Predict')
    if pred:
        result = model.predict(scale.transform([features]))
        if result==0:
            st.write('Person will not suffer lung cancer')
        else:
            st.write('Person will suffer lung cancer')

main()