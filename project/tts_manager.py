import time
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
    def process(self, text: str, max_words: int):
        audio_chunks = []
        
        for i, chunk in enumerate(self.stream_strategy.stream(text, max_words)):
            chunk_start_time = time.time()

            audio = self.tts_strategy.generate_audio(chunk) # model inference occurs. (TTS)
            
            audio_chunks.append(audio) # audio chunk is added to 

            self.play_audio(audio, 0.5) # Play audio through onboard device

            chunk_end_time = time.time()
            chunk_total_time = chunk_end_time - chunk_start_time
            print(f"Time to create and save chunk {i+1} as a .wav file: {chunk_total_time:.2f} seconds")
        
        if audio_chunks:
            final_audio = np.concatenate(audio_chunks)
            print("All chunks processed and saved as .wav files.")
        else:
            print("No audio chunks were processed.")
    
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
