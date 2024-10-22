# 302-TTS
This is the project repo for ICT302 T2S-Kev.
Strategy Design Pattern is utilised throughout the code for TTS and Streaming.

TO RUN DOCKER CONTAINER:

1. Navigate to directory
2. Enter following commands:
    docker build -t tts-app .  
    docker run --rm -it tts-app
3. For audio on windows use:
    wsl docker run --rm -it -e "PULSE_SERVER=/mnt/wslg/PulseServer" -v /mnt/wslg/:/mnt/wslg/ tts-app
4. For cloning:
    In the train command check accelerator is correct (cpu or gpu)
    docker run --shm-size=16g --rm -it tts-app
