# chunking_strategy.py

from abc import ABC, abstractmethod

# Strategy Interface for chunking text
class ChunkingStrategy(ABC):
    @abstractmethod
    def chunk(self, text: str, max_words: int):
        pass
