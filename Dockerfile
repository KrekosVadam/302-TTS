FROM python:3.9-slim-buster

ENV DEBIAN_FRONTEND=noninteractive 

WORKDIR /project

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \ 
    libasound2-dev \
    libportaudio2 \
    libportaudiocpp0 \
    portaudio19-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD ["python", "project/main.py"]
CMD ["python", "tts_manager.py"]

