FROM python:3.14-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8080

RUN useradd app

# Create a directory for QR codes and give the app user ownership
RUN mkdir -p /app/qrcodes && chown -R app:app /app/qrcodes

USER app

CMD ["python3", "app/main.py", "--host", "0.0.0.0", "--port", "8080"]