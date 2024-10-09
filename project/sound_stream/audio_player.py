import threading
import time
import numpy as np
import simpleaudio as sa

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

        self.audio_data = audio_data

        # Start new thread for audio playback
        self.play_thread = threading.Thread(target=self._play_audio_thread)
        self.play_thread.start()

    def _play_audio_thread(self):
        """
        Thread that handles the actual audio playback.

        Args:
        """

        # Convert the audio data to bytes for playback
        audio_bytes = self.audio_data.tobytes()
        
        # Start playing audio without blocking
        play_obj = sa.play_buffer(audio_bytes, 1, 2, 22050)  # Mono, 16-bit PCM, 22.05kHz sample rate
        
        # Wait for the audio to finish (in the background)
        play_obj.wait_done()

    