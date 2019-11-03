FROM python:3.8.0-slim 
WORKDIR /app
COPY src  ./src
COPY certificates ./certificates
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "src/auth_server.py"]
