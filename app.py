import streamlit as st
import pandas as pd
import numpy as np
import pickle

Sex = {
"Male" : 0,"Female" : 1,"Others" : 2,}

Cabin={"Nan":0,"C85":1,"C123":2,"B42":3,}
Embarked={"S":0,"C":1,"Q":2,}

Age={"0-10":0,"10-17":1,"18-30":2,"31-45":3,"46-60":4,"60 above":5,}
model=pickle.load(open('lin_model.pkl',"rb"))

def predict(PassengerId,Survived,Pclass,Sex,Age,Ticket,Fare,Cabin,Embarked):
    """function to accept the values"""
    PassengerId=int(input('Enter passengerid value'))
    Survived=int(input('Enter survived value'))
    Pclass=int(input('Enter pclass value'))
    Sex=int(input('Enter Sex value'))
    Age=float(input('Enter age value'))
    Ticket=int(input('Enter Ticket value'))
    Fare=float(input('Enter Fare value'))
    Cabin=int(input('Enter cabin value'))
    Embarked=int(input('Enter Embarked value'))

    selected_sex=Sex[sex]
    selected_cabin=Cabin[cabin]
    selected_embarked=Embarked[embarked]
    selected_age=Age[age]
    user_input=np.array([[PassengerId,Survived,Pclass,selected_sex,selected_age,Ticket,Fare,selected_cabin,selected_embarked]])
    res=model.predict(user_input) [0].round(2)
    return res
if _name=="__main_":
    st.header("Ticket booking")
    col1,col2=st.columns([2,1])
    PassengerId= col1.slider("Passenger Id",max_value=1000,min_value=1)
    Survived= col1.slider("Survived",max_value=10,min_value=1)
    Pclass=col1.selectbox("Pclass",list(Pclass.keys()))
    Sex=col1.selectbox("Select sex",list(Sex.keys()))
    Age=col1.selectbox("Select age",list(Age.keys()))
    Ticket=col1.slider("Select Ticket ",max_value=10000,min_value=20000)
    Fare=col1.slider("Select Fare",max_value=100.0,min_value=1.0)
    Cabin=selectbox("Select cabin",list(Cabin.keys()))
    Embarked=selectbox("Select Embarked",list(Embarked.keys()))
    res=predict(PassengerId,Survived,Pclass,Sex,Age,Ticket,Fare,Cabin,Embarked)
    submit_button=st.button("Predict")
    if submit_button:
        larger_text=f"<h2 style='color:green;'>The predicted price is : {res} Lakhs</h2>"
        st.markdown(larger_text,unsafe_allow_html=True)
        st.write(res)