FROM python:3.7-slim-buster

# WORKDIR /user/src

COPY ./src/ ./

RUN pip3 install -r requirements.txt

#CMD ["python3", "./processing.py"]

# Add a Python script and configure Docker to run it
ADD processing.py /
ENTRYPOINT ["python3", "/processing.py"]
