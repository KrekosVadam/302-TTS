# 302-TTS
This is the project repo for ICT302 T2S-Kev.
Strategy Design Pattern is utilised throughout the code for TTS and Streaming.

Check tts_clone.TTSClone.train to change batch sizes and max epochs

TO RUN DOCKER CONTAINER:

1. Navigate to directory
2. Download the checkpoint file from https://huggingface.co/datasets/rhasspy/piper-checkpoints/tree/main/en/en_US/ryan/medium and place it in project/voices/training-resources
3. Enter following commands:
    docker build -t tts-app .  
    wsl docker run --shm-size=16g --rm -it -e "PULSE_SERVER=/mnt/wslg/PulseServer" -v /mnt/wslg/:/mnt/wslg/ tts-app
