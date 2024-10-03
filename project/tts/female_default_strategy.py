from collections.abc import Iterable
from piper.voice import PiperVoice
from project.tts.tts_strategy import TTSStrategy
import sounddevice as sd

class FemaleDefaultStrategy(TTSStrategy):
    """
    Default TTS Strategy class implementing the TTSStrategy interface. 
    This allows for a default voice to be used, no voice clone, etc.

    methods:
        synthesize(text: str):
            Generate speech from a chunk of text. Can be overridden by subclasses 
            for more specific implementations, such as generating male or female voices.
    """
    
    def synthesize(self, text: str) -> Iterable[bytes]:
        """
        Concrete method for generating default speech for the given text chunk.

        param: text (str): A string representing the segment of text to be converted 
                            into speech.

        return: iterable of bytes representing the audio
        """
        
        voice = PiperVoice.load("project/voices/en_US-lessac-high.onnx")
        audio_stream = voice.synthesize_stream_raw(text)
        print("Audio Stream:", audio_stream)
        
        if audio_stream is None:
            raise ValueError("Audio synthesis returned None.")

        return audio_stream

# 1. Test Initialization of MaleDefaultStrategy
try:
    strategy = FemaleDefaultStrategy()
    assert strategy is not None, "MaleDefaultStrategy should initialize successfully"
    print("Test 1: Initialization of MaleDefaultStrategy - Passed")
except Exception as e:
    print(f"Test 1: Initialization of MaleDefaultStrategy - Failed ({str(e)})")

# 2. Test Voice Model Loading
voice = PiperVoice.load("project/voices/en_US-lessac-high.onnx")
assert voice is not None, "Voice model should load successfully"
print("Test 2: Voice Model Loading - Passed")

# 3. Test Successful Audio Synthesis
audio_stream = strategy.synthesize("Hello, world!")
assert isinstance(audio_stream, Iterable), "Failed: Successful Audio Synthesis Test"
audio_chunk = next(audio_stream)  # Get the first chunk of audio
assert audio_chunk is not None, "Failed: Audio stream should produce audio data"
print("Test 3: Audio Synthesis - Passed")

# 4. Test Audio Synthesis with Empty String
audio_stream_empty = strategy.synthesize("")
audio_chunk_empty = next(audio_stream_empty)  # Get the first chunk of audio
assert audio_chunk_empty is not None, "Failed: Audio data should be generated for empty string"
print("Test 4: Audio Synthesis with Empty String - Passed")

# Mock PiperVoice.load by overriding it inline
PiperVoice.load = lambda model_path: type(
    "MockedPiperVoice", 
    (object,), 
    {"synthesize_stream_raw": lambda text: None}  # Simulate synthesize_stream_raw returning None
)()

# Now run the test for audio synthesis returning None
try:
    # This will trigger the mocked synthesize_stream_raw to return None
    audio_stream = strategy.synthesize("Hello")
    assert False, "Failed: Expected ValueError when synthesize_stream_raw returns None"
except ValueError as e:
    # Ensure the error message is the expected one
    assert str(e) == "Audio synthesis returned None.", "Failed: Error message mismatch"

print("Test 5: Audio Synthesis Returning None - Passed")
