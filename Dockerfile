FROM python:3.10.2-slim-buster
#FROM python:3.9.10-slim-buster
#FROM python:3.9.10-alpine3.15

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code/main.py
COPY ./extractor /code/extractor

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
