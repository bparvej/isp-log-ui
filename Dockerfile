FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .
COPY templates/ /templates/

ENV FLASK_ENV=development

CMD ["python", "app.py"]
