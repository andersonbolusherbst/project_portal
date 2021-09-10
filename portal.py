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
with st.expander("New here? A Quick Primer on Machine Learning:"):
        st.info('Machine learning is about finding patterns in structured data and making predictions. These can be (and often are) predictions about what will happen in the future, such as a stock price forecast. But this is not the only way you’ll find the term “predictions” used in machine learning solutions. It also means predicting answers to questions like: “Is this customer likely to buy my product?”, "Is this a good location to open a physical store ?" or "What type of customer is most likely to cancel a subscription?" The latter kind of prediction isn’t a time-based prediction (looking into the future), but rather a prediction in terms of assigning a label to the new observation, based on patterns identified from historical observations.')
        st.info('"Classification"  :arrow_right:  predicting a label. "Regression" :arrow_right: predicting a quantity')
        st.info('When viewing these projects, think how the concepts of prediction can be applied to your business. This may be through forecasting numerical values or classifying products or customers into groups/categories')

option = st.sidebar.selectbox("Please select a project type", ('Start Here','Machine Learning - Prediction', 'Machine Learning -Churn Rate Classification','Machine Learning - Time Series Forecast','Machine Learning - Lead Scoring','API Integration', 'Data Analysis'))

st.header("You are viewing: "+option)

if option == "Start Here":

    st.markdown(' :arrow_left: __Use the side bar to navigate this portal__')
    


if option == "Machine Learning - Prediction":

    st.markdown(
               """
        | Label | Description |
        | --- | --- |
        | `Project Name` | Boston 1970s House Price Prediction |
        | `Project Type` | Machine Learning - Predict Boston House Prices in the 1970s |
        | `Machine Learning Model` | Regression |
        | `Machine Learning Description`| Regression models can be used to predict and forecast based off historical data. Independant variables (explanatory variables) are used to predict the dependant variable (explained or response variable). In this case characteristics of houses have been used to predict a houses final price|
        | `Applications` | Forecasting sales, costs and  customer signups. Predicting the price of a house given house features, predicting the impact of SAT/GRE scores on college admissions and determining the causal-effect relationship between advertising spend & revenue. |
             
        """
        ) 
    project_link ='[GENERATE PROJECT](https://share.streamlit.io/andersonbolusherbst/house_price_prediction/main/boston.py)'
    

    st.markdown(project_link, unsafe_allow_html=True)


if option == "Machine Learning - Churn Rate Classification":

    st.markdown(
           """
        | Label | Description |
        | --- | --- |
        | `Project Name` | Predicting Subscription Service Cancellations (Churn Rate) |
        | `Project Type` | Machine Learning - Classification (Churn Rate of Telco Communications) |
        | `Machine Learning Model` | Decision Tree |
        | `Machine Learning Description`| Decision Tree models can be used to place dependant variables into groups or categories based on their characteristics/features. In this case - 'cancel' or 'don't cancel' a subscription. There are a variety of classification models that are best suited for different applications and data sets, such as Random Forest, KNN and Support Vector Machine. In this case we employed a Light Gradient Boost Machine Learning Model.|
        | `Applications` | Customer segmentation, churn rate prediction, lead scoring, image recognition, borrower loan defaults and business risk management |
             
        """
        )

    project_link ='[GENERATE PROJECT](https://share.streamlit.io/andersonbolusherbst/churn/main/churn.py)'
    
    st.markdown(project_link, unsafe_allow_html=True)

if option == "Machine Learning - Time Series Forecast":

    st.markdown(
                        """
                    | Label | Description |
                    | --- | --- |
                    | `Project Name` | Predicting Stock Prices |
                    | `Project Type` | Machine Learning - Time Series Forecast (Forcasting Stock Prices) |
                    | `Machine Learning Model` | Facebook Prophet |
                    | `Machine Learning Description`| Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, daily seasonality and holiday effects. It works best with time series data that has strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend and typically handles outliers well.|
                    | `Applications` | Customer segmentation, churn rate prediction, lead scoring, image recognition, borrower loan defaults and business risk management |
                    
                    """
                    )

    project_link ='[GENERATE PROJECT](https://share.streamlit.io/andersonbolusherbst/stock_forecast/main/main.py)'
    
    st.markdown(project_link, unsafe_allow_html=True)
        
if option == "Machine Learning - Lead Scoring":

    st.markdown(
               """
        | Label | Description |
        | --- | --- |
        | `Project Name` | Lead scoring- Hiring assessment platform |
        | `Project Type` | Machine Learning - Predict probability of making a sale to each potential customer |
        | `Machine Learning Model` | Regression - Gradient boosting decision tree |
        | `Machine Learning Description`| Regression models can be used to predict and forecast based off historical data. Independant variables (explanatory variables) are used to predict the dependant variable (explained or response variable). In this case characteristics of leads have been used to predict the probability of converting the lead into a paying customer|
        | `Applications` | Forecasting sales, costs and  customer signups. Predicting the price of a house given house features, predicting the impact of SAT/GRE scores on college admissions and determining the causal-effect relationship between advertising spend & revenue. |
        """)

    project_link ='[GENERATE PROJECT](https://share.streamlit.io/andersonbolusherbst/leadscoring/main/streamlit.py)'
    
    st.markdown(project_link, unsafe_allow_html=True)




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
    st.subheader("data analysis description table to be added ")

    st.markdown(
               """
        | Label | Description |
        | --- | --- |
        | `Project Name` | Data Dashboard |
        | `Project Type` | Exploratory Data Analysis, Data Visualizations and Customer Segmentation |
        | `Skills Employed` | Python, Pandas, Seaborn, Matplotlib, Sweetviz and the Sklearn Machine Learning Library|
        | `Data Dashboard Description`| Exploratory data analysis is a way to better understand data. Data visualizations are typically more interpretable and easy to generate, so you can rapidly explore many different aspects of a dataset. The goal is to generate simple summaries of the data that inform your businesses marketing question(s). Customer Segmentation  enables a company to customize its relationships with the customers. Utilizing a KMeans machine learning algorithim to find similar characteristics in each customer's behaviour and needs, this algorithim then generalizes customers into groups to satisfy demands with various strategies. |
        | `Applications` | Uncover the underlying structure of a dataset. Exposes trends, patterns, and relationships with your comapany´s data that are not readily apparent |
        """)

    project_link ='[GENERATE PROJECT](https://share.streamlit.io/andersonbolusherbst/eda/main/eda.py)'
    
    st.markdown(project_link, unsafe_allow_html=True)







