import numpy as np
import simpleaudio as sa
import threading

from scipy.io.wavfile import write
from tts.default_strategy import DefaultStrategy
from tts.female_default_strategy import FemaleDefaultStrategy
from tts.male_default_strategy import MaleDefaultStrategy
from tts.tts_strategy import TTSStrategy

class TTSManager:
    """
    Acts as the context class responsible for managing the process of turning Text to Speech.

    param: choice (str): The voice choice for generating audio ('Male', 'Female', 'Default').
    """
    
    def __init__(self, choice: str):
        """
        Initializes the TTSManager with the appropriate TTS strategy based on the choice.

        Args:
            choice (str): The user's voice choice ('Male', 'Female', 'Default').
        """
        if choice == 'Male':
            self.tts_strategy = MaleDefaultStrategy()
        elif choice == 'Female':
            self.tts_strategy = FemaleDefaultStrategy()
        elif choice == 'Default':
            self.tts_strategy = DefaultStrategy()
        else:
            # If an invalid option is given, default to the general DefaultStrategy
            self.tts_strategy = DefaultStrategy()

    # Main process for creating text into speech and playing the speech
    def process(self, text: str):
        """
        Main function for handling the passing of text to the TTS model,
        then passing speech to onboard sound.

        Args:
            text (str): A string of text.

        Returns:
            None
        """
        # Generate audio for the entire input text
        audio = self.tts_strategy.generate_audio(text)

        # Play audio through onboard device
        self.play_audio(audio, 0.5) 
    
    # Thread creation for playing audio
    def play_audio(self, audio, delay):
        """
        Creates a thread for audio playback.

        Args:
            audio (): Audio processed by the TTS model ready for playback.
            delay (int): An int used to add artificial delay.

        Returns:
            None
        """
        thread = threading.Thread(target=self._play_audio_thread, args=(audio, delay))
        thread.start()

    # Audio logic for playing on onboard sound system
    def _play_audio_thread(self, audio, delay):
        """
        Plays audio on onboard sound system. 

        Args:
            audio (): Audio processed by the TTS model ready for playback.
            delay (int): An int used to add artificial delay.

        Returns:
            None
        """

        # Normalize the audio
        audio_normalized = np.int16(audio / np.max(np.abs(audio)) * 32767)
        
        # Convert the audio to bytes
        audio_bytes = audio_normalized.tobytes()
        
        # Play the audio using simpleaudio
        play_obj = sa.play_buffer(audio_bytes, 1, 2, 22050)  # Mono, 16-bit PCM, 22.05kHz sample rate
        
        # Wait for playback to finish
        play_obj.wait_done()

        # Add a delay
        time.sleep(delay)

