# dummy_tts.py

import time
import numpy as np
from TTS_Shell.tts_strategy import TTSStrategy

# Concrete Strategy for TTS (dummy simulation)
class DummyTTS(TTSStrategy):
    def generate_audio(self, chunk: str):
        # Simulate the time taken for generating audio
        print(f"Generating audio for chunk: {chunk}")
        time.sleep(0.5)  # Simulate processing time
        return np.random.rand(10000)  # Dummy audio data
