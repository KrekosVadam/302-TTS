FROM python:3.9-slim-buster

ENV DEBIAN_FRONTEND=noninteractive 

WORKDIR /project

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

RUN pip install pip==24.0
RUN pip install torch==1.13.0+cu117 --extra-index-url https://download.pytorch.org/whl/cu117

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

#CMD ["python", "./project/main.py"]
#CMD ["python", "project/main.py"]
#CMD ["python", "-m", "project.tts.female_default_strategy"]
#CMD ["python", "-m", "project.tts.male_default_strategy"]
##CMD ["python", "-m", "project.tts_manager"]
#CMD ["python", "-m", "project.sound.audio_player"]
CMD ["python", "-m", "project.main"]
