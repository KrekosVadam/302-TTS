from .tts_strategy import TTSStrategy

class CustomStrategy(TTSStrategy):
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
        
        # voice = "custom_voice"
        
        return 
