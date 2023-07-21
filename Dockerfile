FROM python:3.10.6

WORKDIR /app

COPY api_poetry/ /app/api_poetry
COPY tests/ /app/test
COPY requirements.txt/ /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "./api_poetry/main.py"]