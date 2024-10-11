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

# Test 2: Ensure the play_audio method can handle valid audio data.
audio_data = np.random.randint(-32768, 32767, 22050, dtype='int16')
try:
    player.play_audio(audio_data)
    print("Test 2 Passed: Audio plays successfully.")
except Exception as e:
    print(f"Test 2 Failed: An error occurred while playing audio - {e}")

# Test 3: Ensure play_audio can handle empty audio data.
empty_audio_data = np.array([], dtype='int16')
try:
    player.play_audio(empty_audio_data)
    print("Test 3 Passed: No error with empty audio data.")
except Exception as e:
    print(f"Test 3 Failed: An error occurred with empty audio data - {e}")

# Test 4: Ensure play_audio raises an error for incorrect data type.
invalid_audio_data = [1, 2, 3]  # List instead of numpy array
try:
    player.play_audio(invalid_audio_data)
    print("Test 4 Failed: Invalid data type was not handled.")
except Exception as e:
    print(f"Test 4 Passed: Error raised as expected for invalid data type - {e}")





    
