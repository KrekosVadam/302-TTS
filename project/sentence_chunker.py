# sentence_chunker.py

import re
from TTS_Shell.chunking_strategy import ChunkingStrategy

# Concrete Strategy for chunking text by sentence
class SentenceChunker(ChunkingStrategy):
    def chunk(self, text: str, max_words: int):
        sentences = re.split(r'(?<=[.!?])\s+', text)
        chunk = []
        word_count = 0

        for sentence in sentences:
            words = sentence.split()
            if word_count + len(words) <= max_words:
                chunk.append(sentence)
                word_count += len(words)
            else:
                yield_chunk = ' '.join(chunk).strip()
                if yield_chunk:
                    yield yield_chunk
                chunk = [sentence]
                word_count = len(words)

        # Yield the last chunk if there's any remaining text
        yield_chunk = ' '.join(chunk).strip()
        if yield_chunk:
            yield yield_chunk
