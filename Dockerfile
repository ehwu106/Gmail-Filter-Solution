FROM python:3.10.7-slim
WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]