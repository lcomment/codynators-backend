FROM python:3.8
RUN mkdir myapp/
RUN mkdir myapp/config
COPY app.py myapp/app.py
COPY DB_handler.py myapp/DB_handler.py
COPY config/firebaseAuth.json myapp/config/firebaseAuth.json
COPY 여행을떠나요.csv myapp/여행을떠나요.csv
COPY requirements.txt myapp/requirements.txt
WORKDIR /myapp/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]