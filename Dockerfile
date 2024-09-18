FROM python==3.9-slim-buster

ENV DEBIAN_FRONTEND=noninteractive 

WORKDIR /project

COPY requirements.txt .

RUN pip install --upgrade pip && 
    pip install -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]