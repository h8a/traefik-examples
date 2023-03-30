FROM python:3.11-alpine3.17

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY src .

EXPOSE 5000

ENTRYPOINT [ "python", "./main.py" ]