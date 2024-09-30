import threading
import numpy as np
import simpleaudio as sa

from tts.tts_strategy import TTSStrategy
from tts.male_default_strategy import MaleDefaultStrategy
from tts.female_default_strategy import FemaleDefaultStrategy
from tts.custom_strategy import CustomStrategy

class TTSManager:
    """
    Acts as the context class responsible for managing the process of turning Text to Speech

    param: tts_strategy (TTSStrategy): The strategy for generating audio from text.
    """
    
    def __init__(self):
        self.tts_strategy = None
     
    # Main process for creating text into speech and playing the speech
    def process(self, text: str, voice_type: str):
        """"
        Main function for handling the passing of text to piper model,
        then passing speech to onboard sound

        Args:
            text (String): A String of text
            voice_type (String): Voice type to be used for speech synthesis (male, female, custom)

        Returns:
            none
        """
            
        # Load strategy based on voice type
        if voice_type == "male":
            # do male
            self.tts_strategy = MaleDefaultStrategy()
        elif voice_type == "female":
            # do female
            self.tts_strategy = FemaleDefaultStrategy()
        elif voice_type == "custom":
            # do custom
            self.tts_strategy = CustomStrategy()
        else:
            # set default if nothing else chosen
            self.tts_strategy = MaleDefaultStrategy()
            
        self.tts_strategy.synthesize(text)  
        
        audio = self.tts_strategy.synthesize(text)
           
def test_constructor():
    """
    Test that the constructor initializes the tts_strategy to None.
    """
    manager = TTSManager()
    assert manager.tts_strategy is None, "Constructor should initialize tts_strategy to None"
    print("test_constructor passed")

def test_process_strategy_selection_male():
    manager = TTSManager()
    manager.process("test text", "male")
    assert isinstance(manager.tts_strategy, MaleDefaultStrategy), "MaleDefaultStrategy should be selected for 'male' voice type"
    print("test_process_strategy_selection_male passed")

def test_process_strategy_selection_female():
    manager = TTSManager()
    manager.process("test text", "female")
    assert isinstance(manager.tts_strategy, FemaleDefaultStrategy), "FemaleDefaultStrategy should be selected for 'female' voice type"
    print("test_process_strategy_selection_female passed")


def test_process_strategy_selection_custom():
    manager = TTSManager()
    manager.process("test text", "custom")
    assert isinstance(manager.tts_strategy, CustomStrategy), "CustomStrategy should be selected for 'custom' voice type"
    print("test_process_strategy_selection_custom passed")


def test_process_strategy_selection_default():
    manager = TTSManager()
    manager.process("test text", "unknown")
    assert isinstance(manager.tts_strategy, MaleDefaultStrategy), "MaleDefaultStrategy should be selected as default for an unknown voice type"
    print("test_process_strategy_selection_default passed")


def test_play_audio_creates_thread():
    manager = TTSManager()
    dummy_audio = np.array([0.1, 0.2, 0.3])  # Dummy audio data for testing

    # Try to play audio
    manager.play_audio(dummy_audio, 0.5)
    print("test_play_audio_creates_thread passed")


def test_play_audio_thread():
    manager = TTSManager()
    dummy_audio = np.array([0.1, 0.2, 0.3])  # Dummy audio data for testing

    # Test the internal audio playback logic
    try:
        manager._play_audio_thread(dummy_audio, 0.5)
        print("test_play_audio_thread passed")
    except Exception as e:
        print(f"test_play_audio_thread failed with exception: {e}")

test_constructor()
#test_process_strategy_selection_male()
test_process_strategy_selection_female()
#test_process_strategy_selection_custom()
#test_process_strategy_selection_default()
#test_play_audio_creates_thread()
#test_play_audio_thread()
