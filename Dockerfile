FROM python:3.10

ARG api_id
ARG api_hash
ENV LIKE_COUNT=$like_count
ENV API_ID=$api_id
ENV API_HASH=$api_hash

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN echo $LIKE_COUNT

COPY . .

CMD ["python", "main.py", "${LIKE_COUNT}"]
