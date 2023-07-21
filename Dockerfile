FROM python:3.10.6

WORKDIR /app

COPY api_poetry api_poetry
COPY tests tests
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "./api_poetry/server.py"]