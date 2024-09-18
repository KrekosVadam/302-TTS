import time
import numpy as np

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
     
    def process(self, text: str, max_words: int):
        audio_chunks = []
        
        for i, chunk in enumerate(self.stream_strategy.stream(text, max_words)):
            chunk_start_time = time.time()

            audio = self.tts_strategy.generate_audio(chunk) # model inference occurs. (TTS)
            
            audio_chunks.append(audio) # audio chunk is added to 

            self.save_audio_chunk(audio, i) # Save each chunk as a .wav file

            chunk_end_time = time.time()
            chunk_total_time = chunk_end_time - chunk_start_time
            print(f"Time to create and save chunk {i+1} as a .wav file: {chunk_total_time:.2f} seconds")
        
        if audio_chunks:
            final_audio = np.concatenate(audio_chunks)
            print("All chunks processed and saved as .wav files.")
        else:
            print("No audio chunks were processed.")
    
    def save_audio_chunk(self, audio_chunk, chunk_index):
        # Normalize and save audio using scipy
        audio_chunk_normalized = np.int16(audio_chunk / np.max(np.abs(audio_chunk)) * 32767)  # Normalize audio to 16-bit PCM
        write(f'generated_chunk_{chunk_index}.wav', 24000, audio_chunk_normalized)  # Save using scipy's write method
