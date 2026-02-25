import streamlit as st
import pickle as pk
from PIL import Image
import numpy as np

def show():
    st.title(':red[Diabetes Checking]')
    img = Image.open('diabetes-.jpg')
    st.image(img,width=700)
    preg = st.text_input('Enter your number of Pregnancies:')
    glu = st.text_input('Enter Glucose level:')
    Blpr = st.text_input('Enter Blood pressure count:')
    sktk= st.text_input('Enter your Skin thinkness:')
    insulin = st.text_input('Enter Insulin count:')
    BMI = st.text_input('Enter BMI count:')
    diab = st.text_input('Enter your Daibetes value:')
    age = st.text_input('Enter your age:')

    features = [preg,glu,Blpr,sktk,insulin,BMI,diab,age]

    model = pk.load(open('scaled_model_for_diab','rb'))
    scale = pk.load(open('scaled_model_for_diab','rb'))

    if st.button('Check'):
        features = np.array([[preg, glu, Blpr, sktk, insulin, BMI, diab, age]])
        scaled_features = scale.transform(features)
        result = model.predict(scaled_features)

        if result[0] == 0:
            st.success('You have no diabetes 🎉')
        else:
            st.error('You have diabetes 😓')

show()