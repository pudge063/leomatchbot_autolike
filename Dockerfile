FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN echo $LIKE_COUNT

COPY . .

CMD ["python", "main.py", "${LIKE_COUNT}"]
