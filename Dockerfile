FROM python:3.9-slim-buster

ENV DEBIAN_FRONTEND=noninteractive 

WORKDIR /project

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    python3-dev \
    build-essential \
    espeak-ng \ 
    libasound2-dev \
    libportaudio2 \
    libportaudiocpp0 \
    portaudio19-dev \
    pulseaudio \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install torch
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./project/main.py"]
#CMD ["python", "project/main.py"]
#CMD ["python", "-m", "project.tts.female_default_strategy"]
#CMD ["python", "-m", "project.tts_manager"]
