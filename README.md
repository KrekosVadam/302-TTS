# T2S-Kev (ICT302 Project by Murdoch Miles)
A Text-to-Speech (TTS) application leveraging the Strategy Pattern Design to create natural TTS and Cloned Voices. 

## Prerequisites

1. **Docker**: Ensure docker is installed and running.
2. **Model Checkpoint (.ckpt) Files**: If you are Cloning a voice, please follow the Clone script and user guide.
       Download the checkpoint file from https://huggingface.co/datasets/rhasspy/piper-checkpoints/tree/main/en/en_US/ryan/medium and place it in project/voices/training-resources
       Others can be found from the same website
   
## Setup and Installation

1. **Clone Repository**
2. **Build/Run Docker Image**

## Build/Run Docker Image:

1. Navigate to directory
2. Enter following commands:
## For Windows:
    docker build -t tts-app .  
    wsl docker run --shm-size=16g --rm -it -e "PULSE_SERVER=/mnt/wslg/PulseServer" -v /mnt/wslg/:/mnt/wslg/ tts-app

## For Linux:
    docker build -t tts-app .  
    wsl docker run --shm-size=16g --rm -it tts-app
