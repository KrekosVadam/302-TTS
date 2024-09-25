import numpy as np
import simpleaudio as sa

from scipy.io.wavfile import write

from src.stream.stream_strategy import StreamStrategy
from src.tts.tts_strategy import TTSStrategy

class TTSManager:
    """
    Acts as the context class responsible for managing the process of turning Text to Speech

    param: stream_strategy (StreamStrategy): The strategy for chunking the input text.
    param: tts_strategy (TTSStrategy): The strategy for generating audio from text.
    """
    
    def __init__(self, stream_strategy: StreamStrategy, tts_strategy: TTSStrategy):
        self.stream_strategy = stream_strategy
        self.tts_strategy = tts_strategy
     
    # Main process for creating text into speech and playing the speech
    def process(self, text: str):
        """"
        Main function for handling the passing of text to piper model,
        then passing speech to onboard sound

        Args:
            text (String): A String of text

        Returns:
            none
        """
        
        for i, chunk in enumerate(self.stream_strategy.stream(text)):

            # model inference occurs. (TTS)
            audio = self.tts_strategy.generate_audio(chunk) 

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
