FROM python:3.8
RUN mkdir myapp/
RUN mkdir myapp/config
RUN mkdir myapp/source
RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx
COPY app.py myapp/app.py
COPY algorithm_1.py myapp/algorithm_1.py
COPY algorithm_2.py myapp/algorithm_2.py
COPY butter_function.py myapp/butter_function.py
COPY pyxl_modules.py myapp/pyxl_modules.py
COPY DB_handler.py myapp/DB_handler.py
COPY config/firebaseAuth.json myapp/config/firebaseAuth.json
COPY 여행을떠나요.csv myapp/여행을떠나요.csv
COPY requirements.txt myapp/requirements.txt
COPY resource myapp/resource
WORKDIR /myapp/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]