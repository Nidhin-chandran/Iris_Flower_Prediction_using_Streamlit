import streamlit as st
import pickle as pk
from PIL import Image

model = pk.load(open('KNN_MODEL_PREDICTION','rb'))
scale = pk.load(open('scale_MODEL_PREDICTION','rb'))


def show():
    st.title(':red[Heart Failure🫀]')
    img = Image.open('istockphoto-1448453929-612x612.jpg')
    st.image(img,width=800)
    age =st.number_input('Enter your age:',value=None)
    aname=st.selectbox('Do you have anaemia:',['No','Yes'])
    if aname == 'No':
        aname =0
    else:
        aname= 1
    creat = st.number_input('Enter your creatinine level:',value=None)

    diab = st.selectbox('Do you have diabetes:',['No','Yes'])
    if diab == 'No':
        diab = 0
    else:
        diab= 1
    ej_fr = st.number_input('Enter your ejection fraction value:',value=None)

    high_blood_pre= st.selectbox('Do yoy have high blood pressure:',['Yes','No'])
    if high_blood_pre =='Yes':
        high_blood_pre=1
    else:
        high_blood_pre=0
    plat = st.number_input('Enter your platelet count:',value=None)
    ser_creat = st.number_input('Enter your serum creatinine value:',value=None)
    sodium = st.number_input('Enter your serum sodium count:',value=None)

    sex = st.selectbox('Enter your gender:',['Male','Female'])
    if sex == 'Male':
        sex=1
    else:
        sex=0
    smoking = st.selectbox('Do you smoke:',['No','Yes'])
    if  smoking == 'No':
        smoking=0
    else:
        smoking=1
    follow_up = st.number_input('Follow up period:',value=None)

    feature=[age,aname,creat,diab,ej_fr,high_blood_pre,plat,ser_creat,sodium,sex,smoking,follow_up]

    if st.button('Check🔍'):
        result = model.predict(scale.transform([feature]))
        if result == 1:
            st.markdown("## 🚨 Result: Heart Failure Detected")
        else:
            st.markdown("## 🎉 Result: Heart is Healthy")
show()