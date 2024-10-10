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



    