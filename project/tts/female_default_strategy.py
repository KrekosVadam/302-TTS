from piper.voice import PiperVoice
<<<<<<< HEAD
import numpy as np
import sounddevice as sd

from .tts_strategy import TTSStrategy
=======
from project.tts.tts_strategy import TTSStrategy
>>>>>>> c0478bedd220ed39c6ef7499399c6a2e8779a858

class FemaleDefaultStrategy(TTSStrategy):
    """
    Default TTS Strategy class implementing the TTSStrategy interface. 
    This allows for a default voice to be used, no voice clone, etc.

    methods:
        synthesize(text: str):
            Generate speech from a chunk of text.
    """
    
    def synthesize(self, text: str):
        """
        Concrete method for generating default speech for the given text chunk.

        Args: text (str): A string representing the segment of text to be converted 
                            into speech.

        return: a list of bytes
        """

<<<<<<< HEAD
        # Empty list
        audio_data = []

        # load voice model
        # Ryan is a standard male voice
        voice = PiperVoice.load("project/voices/en_US-lessac-high.onnx")

        # Loop through text and create voice then add to list
        for audio_bytes in voice.synthesize_stream_raw(text):
            int_data = np.frombuffer(audio_bytes, dtype=np.int16)
            audio_data.append(int_data)

        # Join
        np.concatenate(audio_data)

        return audio_data
=======
        return audio_stream

#----------------------------------------START OF UNIT TESTING----------------------------------------------------------------------------------------
#Test Initialization of FemaleDefaultStrategy
"""
strategy = FemaleDefaultStrategy()
assert strategy is not None, "FemaleDefaultStrategy should initialize successfully"
print("Test 1: Initialization of FemaleDefaultStrategy - Passed")
    
#Test Voice Model Loading
voice = PiperVoice.load("project/voices/en_US-lessac-high.onnx")
assert voice is not None, "Voice model should load successfully"
print("Test 2: Voice Model Loading - Passed")

#Test Successful Audio Synthesis
audio_stream = strategy.synthesize("Hello, world!")
assert isinstance(audio_stream, Iterable), "Failed: Successful Audio Synthesis Test"
audio_chunk = next(audio_stream)  # Get the first chunk of audio
assert audio_chunk is not None, "Failed: Audio stream should produce audio data"
print("Test 3: Audio Synthesis - Passed")

assert isinstance(audio_stream, Iterable), "Failed: audio_stream should be of type Iterable"
print("Test 4: Audio Stream Type iterable - Passed")

#Test Audio Synthesis with Empty String
audio_stream_empty = strategy.synthesize("")
audio_chunk_empty = next(audio_stream_empty)  # Get the first chunk of audio
assert audio_chunk_empty is not None, "Failed: Audio data should be generated for empty string"
print("Test 5: Audio Synthesis with Empty String - Passed")

original_load = PiperVoice.load
# Mock PiperVoice.load by creating an inline object with a lambda function for synthesize_stream_raw
PiperVoice.load = lambda model_path: type(
    "MockedPiperVoice", 
    (object,), 
    {"synthesize_stream_raw": lambda self, text: None}  # Simulate synthesize_stream_raw returning None
)()
try:
    strategy.synthesize("Hello")  # This should raise ValueError
    assert False, "Failed: Expected ValueError when synthesize_stream_raw returns None"
except ValueError as e:
    assert str(e) == "Audio synthesis returned None.", "Failed: Error message mismatch"
print("Test 6: Audio Synthesis Returning None - Passed")
PiperVoice.load = original_load

try:
    strategy.synthesize(123)  # Passing an integer
    assert False, "Failed: Expected TypeError for invalid input type"
except TypeError:
    print("Test 7: Handling Invalid Text Input - Passed")

"""
#----------------------------------------END OF UNIT TESTING----------------------------------------------------------------------------------------
>>>>>>> c0478bedd220ed39c6ef7499399c6a2e8779a858
