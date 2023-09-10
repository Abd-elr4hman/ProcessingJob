FROM python:3.7-slim-buster

WORKDIR /user/src

COPY ./ ./

RUN pip3 install -r requirements.txt

CMD ["python3", "./processing.py"]
