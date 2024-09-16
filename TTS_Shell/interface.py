# interface.py

from TTS_Shell.sentence_chunker import SentenceChunker
from TTS_Shell.dummy_tts import DummyTTS
from TTS_Shell.tts_processor import TTSProcessor

def process_text(text: str, voice_type: str = 'dummy'):
    # handle streaming text into model
    chunking_strategy = SentenceChunker()

    # call TTS model
    if voice_type == 'dummy':
        tts_strategy = DummyTTS()
    else:
        raise ValueError(f"Unknown model type: {voice_type}")
        # check what raise does? like a try?

    # Initialize processor
    processor = TTSProcessor(chunking_strategy, tts_strategy)

    # Process text using model
    processor.process(text, max_words=10)