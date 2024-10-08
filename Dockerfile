FROM python:3.13-bullseye

WORKDIR /

COPY . .

RUN ["pip3", "install", "-r", "requirements.txt"]

CMD ["python3", "main.py"]