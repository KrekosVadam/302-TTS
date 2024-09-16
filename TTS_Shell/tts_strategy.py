# tts_strategy.py

from abc import ABC, abstractmethod

# Strategy Interface for TTS generation
class TTSStrategy(ABC):
    @abstractmethod
    def generate_audio(self, chunk: str):
        pass
