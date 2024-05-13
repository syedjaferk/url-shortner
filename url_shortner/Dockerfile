FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8090

CMD ["gunicorn", "url_shortner.asgi:application", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8090"]