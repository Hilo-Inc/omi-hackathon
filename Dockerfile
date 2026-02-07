FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY webhook/ ./webhook/

EXPOSE 3000

CMD ["python", "webhook/server.py"]
