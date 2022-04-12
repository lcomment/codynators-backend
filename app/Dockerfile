FROM python:latest
RUN mkdir myapp/
COPY app.py myapp/app.py
COPY requirements.txt myapp/requirements.txt
WORKDIR /myapp/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]