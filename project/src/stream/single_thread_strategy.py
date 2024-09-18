import re
from src.stream.strategies.stream_strategies import StreamStrategy

class SingleThreadStream(StreamStrategy):
    """
    Concrete method:
        Implements single-thread stream for text processing.
        
    inherit: StreamStrategy (abstract class)

    methods:
        stream(text: str, max_words: int) -> str:
            Yields text chunks from a sample. Chunks do not exceed maximum word count.
    """
    
    def stream(self, text: str, max_words: int):
        """
        Splits text into chunks with a maximum word count, yielding each chunk as a separate string

        param: text (str): Text sample to be chunked
        param: max_words (int): Maximum number of words allowed per chunk

        return: str: A chunk of text containing sentences with a total word count up to `max_words`.
        """
        
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
