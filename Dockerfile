FROM python:3.9
RUN apt-get update && apt-get clean
RUN apt install default-jre

COPY . /app
WORKDIR /app

COPY requirements.txt /
RUN pip3 install -r requirements.txt

CMD streamlit run --server.port $PORT interface.py