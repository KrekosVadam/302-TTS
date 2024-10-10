import threading
import time
import numpy as np
import simpleaudio as sa
import sounddevice as sd

class AudioPlayer:
    """
    Class responsible for playing audio in the background.

    methods:
        play_audio(audio_data: numpy array):
        _play_audio_thread():
    """

    def __init__(self):
        self.play_thread = None
        self.audio_data = None

    def play_audio(self, audio_data):
        """
        Starts playing audio asynchronously in the background.

        Args:
            audio_data (numpy array): The audio data to play.
        """

        stream = sd.OutputStream(device=0, samplerate=22050, channels=1, dtype='int16', blocksize=256)
        stream.start()

        stream.write(audio_data)

        stream.stop()
        stream.close()

#--------------------------Start of Unit Testing-------------------------------------------
player = AudioPlayer()
# Test 1: Ensure the AudioPlayer object is initialized properly.
try:
    if player.play_thread is None and player.audio_data is None:
        print("Test 1 Passed: AudioPlayer initialized successfully.")
    else:
        print("Test 1 Failed: AudioPlayer attributes not initialized correctly.")
except Exception as e:
    print(f"Test 1 Failed: An error occurred during initialization check - {e}")





    
