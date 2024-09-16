# tts_processor.py

import numpy as np
import time
import torch
from scipy.io.wavfile import write  # Import scipy's write function for saving .wav files
from TTS_Shell.chunking_strategy import ChunkingStrategy
from TTS_Shell.tts_strategy import TTSStrategy

# Context class that manages chunking and TTS generation
class TTSProcessor:
    def __init__(self, chunking_strategy: ChunkingStrategy, tts_strategy: TTSStrategy):
        self.chunking_strategy = chunking_strategy
        self.tts_strategy = tts_strategy
    
    def process(self, text: str, max_words: int):
        concatenated_audio = []
        
        # Process each text chunk
        for i, chunk in enumerate(self.chunking_strategy.chunk(text, max_words)):
            print(f"Processing chunk {i+1}: {chunk}")
            chunk_start_time = time.time()

            # Generate audio for each chunk
            audio = self.tts_strategy.generate_audio(chunk)
            concatenated_audio.append(audio)

            # Save each chunk as a .wav file
            self.save_audio_chunk(audio, i)

            chunk_end_time = time.time()
            chunk_total_time = chunk_end_time - chunk_start_time
            print(f"Time to create and save chunk {i+1} as a .wav file: {chunk_total_time:.2f} seconds")
        
        if concatenated_audio:
            final_audio = np.concatenate(concatenated_audio)
            print("All chunks processed and saved as .wav files.")
        else:
            print("No audio chunks were processed.")
    
    def save_audio_chunk(self, audio_chunk, chunk_index):
        # Normalize and save audio using scipy
        audio_chunk_normalized = np.int16(audio_chunk / np.max(np.abs(audio_chunk)) * 32767)  # Normalize audio to 16-bit PCM
        write(f'generated_chunk_{chunk_index}.wav', 24000, audio_chunk_normalized)  # Save using scipy's write method
