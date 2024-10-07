import threading
import numpy as np
import simpleaudio as sa

from project.tts.tts_strategy import TTSStrategy
from project.tts.male_default_strategy import MaleDefaultStrategy
from project.tts.female_default_strategy import FemaleDefaultStrategy
from project.tts.custom_strategy import CustomStrategy

class TTSManager:
    """
    Acts as the context class responsible for managing the process of turning Text to Speech

    param: tts_strategy (TTSStrategy): The strategy for generating audio from text.
    """
    
    def __init__(self):
        self.tts_strategy = None
     
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
            
        audio = self.tts_strategy.synthesize(text)  
        
       self.play_audio_from_iterable(audio)

    def play_audio_from_iterable(self, audio_chunks, sample_rate=44100, num_channels=1, bytes_per_sample=2):
        """
        Takes an Iterable[bytes] and plays the audio using simpleaudio.

        Args:
            audio_chunks (Iterable[bytes]): The audio data in byte format.
            sample_rate (int): The sample rate (default is 44100 Hz).
            num_channels (int): Number of audio channels (default is 1 for mono).
            bytes_per_sample (int): Bytes per sample (default is 2 for 16-bit audio).
        """
        audio_buffer = b''.join(audio_chunks)
        
        play_obj = sa.play_buffer(audio_buffer, num_channels, bytes_per_sample, sample_rate)
        play_obj.wait_done()

tts_manager = TTSManager()

# Call the process method with text and a chosen voice type
tts_manager.process("Hello, how are you?", "male")
