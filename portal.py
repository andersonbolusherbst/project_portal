import streamlit as st
import pandas as pd
import numpy as np
import requests
import config
import datetime as dt
from iex import IEXStock


st.markdown('<style>h1{color: #03a9f4;text-shadow: 1px 1.5px 2px black;}h2{color: #03a9f4;text-shadow: 0.4px 0.4px 1px black;}div > p > a{border: solid 1.5px;border-radius: 2px;padding: 5px;text-decoration: none;font-weight: 500;}div > p > a:hover{background-color: #4fc3f7;color: black;text-decoration: none;}</style>', unsafe_allow_html=True)
st.title("HAB LABS Project Portal")
st.write("Explore the projects on this dashboard to learn more about our services and the applications of Machine Learning and Data Science")
st.info('"Classification"  :arrow_right:  predicting a label. "Regression" :arrow_right: predicting a quantity')

option = st.sidebar.selectbox("Please select a project type", ('Start Here','Machine Learning - Prediction', 'Machine Learning - Classification','API Integration', 'Data Analysis'))

st.header("You are viewing: "+option)

if option == "Start Here":
    
    st.markdown(' :arrow_left: __Use the side bar to navigate this portal__')
    st.image('chatbot.jpg')
   

if option == "Machine Learning - Prediction":
    
    project_info = {"Project Name":" Boston 1970s House Price Prediction","Project Type":"Machine Learning - Prediction","Machine Learning Model": "Regression","Machine Learning description":"Regression models can be used to predcit and forecast based on historical data. Various models can be used for linear, non-linear and logistic relationships. Independant variables (explanatory variables) and used to predict the dependant variable (explained or response variable","Applications":"Marketing, Operations, Logistics, Finance"}
    my_dict = project_info
    df = pd.DataFrame(list(my_dict.items()),columns = ['Label','Description']) 
    project_link ='[GENERATE PROJECT](https://share.streamlit.io/andersonbolusherbst/house_price_prediction/main/boston.py)'
    st.table(df)
    
    st.markdown(project_link, unsafe_allow_html=True) #root > div:nth-child(1) > div > div > div > div > section.main.css-1v3fvcr.eknhn3m1 > div > div:nth-child(1) > div:nth-child(6) > div > div > p > a
    

if option == "Machine Learning - Classification":
    
    project_info = {"Project Name":" Predicting Subscription Service Cancellations","Project Type":"Machine Learning - Classification","Machine Learning Model": "Decision Tree","Machine Learning description":"Decision Tree models can be used to place dependant variables into groups or categories based on their characteristics/features, in this case - 'cancel' or 'don't cancel' the subscription. There are a variety of classification models that are best suited for different applications and data sets, such as Random Forest, KNN and Support Vector Machine","Applications":"Marketing, Operations, Logistics, Finance"}
    my_dict = project_info
    df = pd.DataFrame(list(my_dict.items()),columns = ['Label','Description'])
    
    project_link ='[GENERATE PROJECT](https://share.streamlit.io/andersonbolusherbst/churn/main/churn.py)'
    st.table(df)
    st.info('"Classification" is about predicting a label and "Regression" is about predicting a quantity')
    
    
  

if option == "API Integration":
    
    if option == 'API Integration':
        st.write("This is live data coming to you from another database. We do this using API's and can connect multiple API's for you, bringing everything you need to one place!")
        st.subheader("_Check out the side bar for options under 'Select Information'!_")
        st.markdown("____________")
        
        screen = st.sidebar.selectbox("Select Information",("Stock Overview", "Price Data", "Social Media Mentions"))
        symbol = st.sidebar.text_input("Symbol", value="NFLX")
        st.title("Asset: "+ symbol)

        
        st.header(screen)
        st.subheader("Put your favorite stock ticker in the sidebar! ~ e.g) _AAPL_, _AMZN_, _GOOGL_")
        st.markdown("____________")
        st.sidebar.markdown(":innocent: Scroll down to see the output!")
        
        
        
    
        if screen == "Stock Overview":
            stock = IEXStock(config.IEX_API_TOKEN, symbol)
            ##logo = stock.get_logo()

            #company_info = stock.get_company_info()

            url = f"https://cloud.iexapis.com/stable/stock/{symbol}/logo?token={config.IEX_API_TOKEN}"
            p = requests.get(url)
            logo = p.json()


            col1, col2 = st.columns([1,1])

            url = f"https://cloud.iexapis.com/stable/stock/{symbol}/company?token={config.IEX_API_TOKEN}"
            p = requests.get(url)
            response_json = p.json()
           #st.write(response_json)

            with col1:
                st.image(logo['url'])
                st.subheader("Description")
                st.write(response_json['description'])


            with col2:
                st.subheader(response_json['companyName'])
                st.write("Industry: " + response_json['industry'])
                st.write("CEO: "+ response_json['CEO'])
                st.write("Country: "+ response_json['country'])
                st.subheader("Website")
                st.write(response_json['website'])


        if screen == "Price Data":
            st.image(f"https://charts2.finviz.com/chart.ashx?t={symbol}")
            url = f"https://cloud.iexapis.com/stable/stock/{symbol}/stats?token={config.IEX_API_TOKEN}"
            m = requests.get(url)
            data = m.json()
            st.write("Market Cap: ",data['marketcap'] )
            st.write("52 week high: ", data['week52high'])
            st.write("52 week low: ", data['week52low'])
            st.write("Shares outstanding: ",data['sharesOutstanding'])
            st.write("200 day moving average: ", data['day200MovingAvg'])
            st.write("50 day moving average: ", data['day50MovingAvg'])
            st.write("P/E ratio: ", data['peRatio'])
            st.write("Beta: ", data['beta'])
            st.write("Next earnings:  ", data['nextEarningsDate'])
            st.write("Next dividend: ", data['nextDividendDate'])
            st.write("Dividend yield: ", data['dividendYield'])

        if screen == "Social Media Mentions":

            #symbol = st.sidebar.text_input("Symbol", value='NFLX', max_chars=5)
            #st.subheader('stocktwits')
            #gets most recent mentions of symbol
            #st.image(f"https://charts2.finviz.com/chart.ashx?t={symbol}")
            r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")
            data = r.json()
            st.subheader("Connect to social platforms and retrieve the data available. Below are posts from 'Stocktwits' mentioning the selected stock in the sidebar")

            #printing body, datetime and person of mention
            for message in data['messages']:
                st.write(message['body'])
                st.write(message['created_at'])
                st.write(message['user']['username'])
                st.image(message['user']['avatar_url'])

    
if option == "Data Analysis":
    st.subheader("data analysis project will be added soon")
    

if option == "Automation":
    st.subheader("data analysis project will be added soon")
    

