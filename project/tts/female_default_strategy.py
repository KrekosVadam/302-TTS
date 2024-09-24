from piper.voice import PiperVoice

from src.tts.tts_strategy import TTSStrategy

class FemaleDefaultStrategy(TTSStrategy):
    """
    Default TTS Strategy class implementing the TTSStrategy interface. 
    This allows for a default voice to be used, no voice clone, etc.

    methods:
        synthesize(text: str):
            Generate speech from a chunk of text. Can be overridden by subclasses 
            for more specific implementations, such as generating male or female voices.
    """
    
    def synthesize(self, text: str):
        """
        Concrete method for generating default speech for the given text chunk.

        param: text (str): A string representing the segment of text to be converted 
                            into speech.

        return: 
        """
        
        voice = PiperVoice.load("en_US-lessac-high")
        voice.synthesize_stream_raw(text) # This call will have to be updated to stream to the right device
        
        return 