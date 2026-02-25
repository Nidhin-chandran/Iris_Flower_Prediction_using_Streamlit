import streamlit as st
import pickle
from PIL import Image

def view():
    st.title(':rainbow[Iris Species Checking]')
    img = Image.open('iris_download.jpeg')
    st.image(img,width=600)
    sepal_len = st.text_input('Enter Sepal Length:',key='sepal_len')

    sepal_wid = st.text_input('Enter Sepal Width:',key='sepal_wid')

    petal_len = st.text_input('Enter Petal Length:',key='petal_len')

    petal_wid = st.text_input('Enter petal Width:',key='petal_wid')

    features = [sepal_wid,sepal_wid,petal_wid,petal_len]
    model = pickle.load(open('Knn_model_of_iris (1)','rb'))
    scale = pickle.load(open('Knn_scale_of_iris1','rb'))
    pred = st.button('Check🔍')
    clear = st.button('Clear🧹')
    if pred:
        output = model.predict(scale.transform([features]))
        if output=='Iris-setosa':
            st.write('This species is Iris-setosa')
        elif output=='Iris-versicolor':
            st.write('This species is Iris-versicolor')
        else:
            st.write('This species is Iris-virginica')
    if clear:
        st.session_state.sepal_len=''
        st.session_state.sepal_wid=''
        st.session_state.petal_len=''
        st.session_state.petal_wid=''

view()