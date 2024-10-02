from collections.abc import Iterable
from piper.voice import PiperVoice
from tts.tts_strategy import TTSStrategy

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


