import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

st.sidebar.title("Simple Stock")
SYM = ["README","PFE","GOOGL","AAPL","MSFT","STG.AX"]
menu = st.sidebar.selectbox("Select a campany",(SYM))

if menu != "README":
    #get data on this ticker
    tickerData = yf.Ticker(menu)

    st.image(tickerData.info['logo_url'])
    st.header(tickerData.info['longName'])
    st.text(tickerData.info['longBusinessSummary'])

    # minus 12 month
    currentTimeDate = datetime.now() - relativedelta(months=12)
    s = st.sidebar.date_input("From", datetime.date(currentTimeDate))
    f = st.sidebar.date_input("To", datetime.date(datetime.now()))

    #get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start=s, end=f)
    # Open	High	Low	Close	Volume	Dividends	Stock Splits
    keys = ['Open','Close']
    df_price = pd.concat([tickerDf.Open, tickerDf.Close], axis=1, keys=keys)

    st.line_chart(df_price)

    st.bar_chart(tickerDf.Volume)

    st.subheader('Recommendations')
    tickerData.recommendations
    # tickerData.actions
    # tickerData.sustainability
else:

    # README page

    st.title("Welcome to Simple Stock")
    '''
    This is a simple application to display companies stock data. Getting financial data in Python is easy with libraries and several public APIs. Straker Translations is the ASX listed company and the stock data is available in public too.
    '''
    st.image('image.png')

    '''
    ### Getting Stock Data Using Python

    `yfinance` is a Python library to access the financial data available on Yahoo Finance.
    By using ticker function we pass the stock symbol for which we need to download the data. This example is working with Pfizer and the ticker for it is `PFE`.

    '''

    code = '''
    import yfinance as yf
    
    #get data on this ticker
    tickerData = yf.Ticker('PFE')
    tickerData.info
    tickerDf = tickerData.history(period='1d', start='2000-01-01', end='2022-01-01')
    '''

    st.code(code, language='python')

    '''
    ### Displaying Information Using Streamlit and Pandas

    `streamlit` is a Python library that makes it easy to create and share, custom web apps for machine learning and data science.
    
    `pandas`is a Python library that is widely used for data analysis and manipulation. It provides numerous functions and methods that expedite the data analysis and preprocessing steps.

    '''

    code = '''
    import streamlit as st
    import pandas as pd

    st.sidebar.title("Simple Stock")
    SYM = ["README","PFE","GOOGL","AAPL","MSFT","STG.AX"]
    st.sidebar.selectbox("Select a campany",(SYM))

    st.image(tickerData.info['logo_url'])
    st.header(tickerData.info['longName'])
    st.text(tickerData.info['longBusinessSummary'])

    keys = ['Open','Close']
    df_price = pd.concat([tickerDf.Open, tickerDf.Close], axis=1, keys=keys)
    st.line_chart(df_price)

    st.bar_chart(tickerDf.Volume)
    '''

    st.code(code, language='python')

    '''
    ### Containerise a Python Application

    The way to get the Python code running in a container is to pack it as a Docker image and then run a container based on it.

    To generate a Docker image we need to create a `Dockerfile` that contains instructions needed to build the image. 
    '''

    '''
    ##### Dockerfile
    '''
    code = '''
    FROM python:3.10

    # set the working directory in the container
    WORKDIR /code

    # copy the dependencies file to the working directory
    COPY requirements.txt .

    # install dependencies
    RUN pip install -r requirements.txt

    # expose app port
    EXPOSE $PORT

    # copy the content of the local src directory to the working directory
    COPY src/ .

    # command to run on container start
    CMD streamlit run --server.port $PORT app.py
    '''

    st.code(code, language='python')


    '''
    ### Build a Image and Run the Container

    The application folder structure should look like this.
    '''

    code = '''
    ├── Dockerfile
    ├── requirements.txt
    └── src
       ├── app.py
       └── image.png
    '''

    st.code(code, language='python')

    '''
    To build a Docker image, execute the docker build command from the application root.
    
    `docker build -t simple-stock .`
    
    With the Docker image in place, we can now run it by executing the docker run command. The -p option is used to expose the ports that are used for the image instance.

    `docker run -p 8501:8501 -e PORT=8501 simple-stock`

    Once the application is up and running, you can browse to the http://localhost:8501

    '''

    '''
    ### Wrapping up

    This post showed how to create a simple Python application, how to create a steamlit application and finally used Docker to run the application.

    The code snippets and files used on this page can be found in this Github repo, feel free to update the code or even add more features.

    `git clone https://github.com/socketio/chat-example.git`

    Happy coding!
    '''

    st.latex(r'''
     x^2 =
     \frac{n^{2}+n}{10}
     ''')

    '''
    ### References

    https://pypi.org/project/yfinance/    

    https://docs.streamlit.io/

    https://pandas.pydata.org/docs/getting_started/overview.html

    https://www.docker.com/blog/containerized-python-development-part-1/

    '''