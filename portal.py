import streamlit as st
import pandas as pd
import numpy as np



st.title("HAB LABS Project Portal")
st.write("Explore the projects on this dashboard to learn more about our services and the applications of Machine Learning and Data Science")

option = st.sidebar.selectbox("Please select a project type", ('Start Here','Machine Learning - Prediction', 'Machine Learning - Classification','API Integration', 'Data Analysis', 'Automation'))

st.header("You are viewing: " option)

if option == "Start Here":
    st.write("Use the side bar to navigate this portal")

if option == "Machine Learning - Prediction":
    st.subheader(option)
    project_info = {"Project Name":" Boston 1970s House Price Prediction","Project Type":"Machine Learning - Prediction","Machine Learning Model": "Regression","Machine Learning description":"Resgression models can be used to predcition and forecast based on historical data. Various models can be used for linear, non-linear and logistic relationships. Independant variables (explanatory variables) and used to predict the dependant variable (explained or response variable","Applications":"Marketing, Operations, Logistics, Finance"}
    st.write(project_info)
    project_link ='[GENERATE PROJECT](https://share.streamlit.io/andersonbolusherbst/house_price_prediction/main/boston.py)'
    st.markdown(project_link, unsafe_allow_html=True)
    

if option == "Machine Learning - Classification":
    st.subheader(option)
    project_info = {"Project Name":" Predicting Subscription Service Cancellations","Project Type":"Machine Learning - Classification","Machine Learning Model": "Decision Tree","Machine Learning description":"Decision Tree models can be used to placed dependant variables into groups or categories based on their characteristics/features, in this case - 'cancel' or 'don't cancel' the subscription. There are a variety of classification models that are best suited for different applications aand data sets, such as Random Forest, KNN and Support Vector Machine","Applications":"Marketing, Operations, Logistics, Finance"}
    st.write(project_info)
    project_link ='[GENERATE PROJECT](https://share.streamlit.io/andersonbolusherbst/churn/main/churn.py)'
    st.markdown(project_link, unsafe_allow_html=True)

if option == "API Integration":
    st.write("API Integration")
    
if option == "Data Analysis":
    st.write("Data Analysis")

if option == "Automation":
    st.write("Automation")

