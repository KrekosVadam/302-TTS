import numpy as np

from tts.tts_strategy import TTSStrategy
from tts.male_default_strategy import MaleDefaultStrategy
from tts.female_default_strategy import FemaleDefaultStrategy
from tts.custom_strategy import CustomStrategy
from sound.audio_player import AudioPlayer

class TTSManager:
    """
    Acts as the context class responsible for managing the process of turning Text to Speech

    methods
        process(text: str, voice_type: str):
            Handles passing the text to the respective voice model
            Passes the returned list of bytes to the audio player
    """
    
    def __init__(self, tts_strategy=MaleDefaultStrategy):
        self.tts_strategy = tts_strategy
        self.audio_player = AudioPlayer()
     
    # Main process for creating text into speech and playing the speech
    def process(self, text: str, voice_type: str):
        """"
        Main function for handling the passing of text to piper model,
        then passing speech to onboard sound

        Args:
            text (String): A String of text
            voice_type (String): Voice type to be used for speech synthesis (male, female, custom)

        Returns:
            none
        """
            
        # Load strategy based on voice type
        if voice_type == "male":
            # do male
            self.tts_strategy = MaleDefaultStrategy()
        elif voice_type == "female":
            # do female
            self.tts_strategy = FemaleDefaultStrategy()
        elif voice_type == "custom":
            # do custom
            self.tts_strategy = CustomStrategy()
        else:
            # set default if nothing else chosen
            self.tts_strategy = MaleDefaultStrategy()

        # Create audio
        audio_array = self.tts_strategy.synthesize(text)

        # Play audio
        self.audio_player.play_audio(audio_array)