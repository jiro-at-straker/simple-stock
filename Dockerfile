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

# CMD streamlit run app.py
CMD streamlit run --server.port $PORT app.py