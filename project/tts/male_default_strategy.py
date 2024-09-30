from piper.voice import PiperVoice
import numpy as np
import sounddevice as sd

from .tts_strategy import TTSStrategy

class MaleDefaultStrategy(TTSStrategy):
    """
    Default TTS Strategy class implementing the TTSStrategy interface. 
    This allows for a default voice to be used, no voice clone, etc.

    methods:
        synthesize(text: str):
            Generate speech from a chunk of text. Can be overridden by subclasses 
            for more specific implementations, such as generating male or female voices.
    """
    
    def synthesize(self, text: str):
        """
        Concrete method for generating default speech for the given text chunk.

        param: text (str): A string representing the segment of text to be converted 
                            into speech.

        return: iterable of bytes representing the audio
        """

        voice = PiperVoice.load("project/voices/en_US-ryan-high.onnx")
        print(sd.query_devices())
        stream = sd.OutputStream(device=0, samplerate=voice.config.sample_rate, channels=1, dtype='int16')
        stream.start()

        for audio_bytes in voice.synthesize_stream_raw(text):
            int_data = np.frombuffer(audio_bytes, dtype=np.int16)
            stream.write(int_data)

        stream.stop()
        stream.close()

        return
