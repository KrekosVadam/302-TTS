
import numpy as np
import simpleaudio as sa

from tts.tts_strategy import TTSStrategy
from tts.male_default_strategy import MaleDefaultStrategy
from tts.female_default_strategy import FemaleDefaultStrategy
from tts.custom_strategy import CustomStrategy

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
            

        # model inference occurs. (TTS) based on voice type given
        audio = self.tts_strategy.synthesize(text)
            
        # Play audio through onboard device
        self.play_audio(audio, 0.5) 
    
    # Thread creation for playing audio
    def play_audio(self, audio, delay):
        """"
        Creates a thread for audio playback

        Args:
            audio (): Audio processed by the TTS model readly for playback
            delay (int): an int used to add artificial delay

        Returns:
            none
        """

        thread = threading.Thread(target=self._play_audio_thread, args=(audio, delay))
        thread.start()

    # Audio logic for playing on onboard sound system
    def _play_audio_thread(self, audio, delay):
        """"
        Plays audio on onboard sound system. 

        Args:
            audio (): Audio processed by the TTS model readly for playback
            delay (int): an int used to add artificial delay

        Returns:
            none
        """

        # Normalize the audio
        audio_normalized = np.int16(audio / np.max(np.abs(audio)) * 32767)
        
        # Convert the audio to bytes
        audio_bytes = audio_normalized.tobytes()
        
        # Play the audio using simpleaudio
        play_obj = sa.play_buffer(audio_bytes, 1, 2, 22050)  # Mono, 16-bit PCM, 24kHz sample rate
        
        # Wait for playback to finish
        play_obj.wait_done()

        # Add a delay
        time.sleep(delay)
