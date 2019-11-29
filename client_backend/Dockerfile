FROM python:3.8.0-slim 
WORKDIR /app 
COPY src  .
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "-u", "client_backend.py"]
