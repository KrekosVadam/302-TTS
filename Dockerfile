FROM python==3.9-slim-buster

ENV DEBIAN_FRONTEND=noninteractive 

WORKDIR /project

COPY requirements.txt .

RUN rm -rf /var/lib/apt/lists/* \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]