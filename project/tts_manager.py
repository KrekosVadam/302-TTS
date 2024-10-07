import threading
import numpy as np
import simpleaudio as sa

from project.tts.tts_strategy import TTSStrategy
from project.tts.male_default_strategy import MaleDefaultStrategy
from project.tts.female_default_strategy import FemaleDefaultStrategy
from project.tts.custom_strategy import CustomStrategy

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

results = []

# Test 1: Initialization of TTSManager
manager = TTSManager()
try:
    assert manager.tts_strategy is None  
    results.append("Test 1 Passed: TTSManager is initialized correctly.")
except AssertionError:
    results.append("Test 1 Failed: TTSManager should initialize tts_strategy to None.")

# Test 2: Male Voice
"""
manager.process("Hello, this is a test.", "male")
try:
    assert isinstance(manager.tts_strategy, MaleDefaultStrategy)
    results.append("Test 2 Passed: Should use MaleDefaultStrategy")
except AssertionError:
    results.append("Test 2 Failed: Should use MaleDefaultStrategy")
"""

# Test 3: Female Voice
manager = TTSManager()
manager.process("Hello, this is a test.", "female")
try:
    assert isinstance(manager.tts_strategy, FemaleDefaultStrategy)
    results.append("Test 3 Passed: Should use FemaleDefaultStrategy")
except AssertionError:
    results.append("Test 3 Failed: Should use FemaleDefaultStrategy")

# Test 4: Custom Voice
"""
manager = TTSManager()
manager.process("Hello, this is a test.", "custom")
try:
    assert isinstance(manager.tts_strategy, CustomStrategy)
    results.append("Test 4 Passed: Should use CustomStrategy")
except AssertionError:
    results.append("Test 4 Failed: Should use CustomStrategy")

# Test 5: Default Voice (unknown type)
manager = TTSManager()
manager.process("Hello, this is a test.", "unknown")
try:
    assert isinstance(manager.tts_strategy, MaleDefaultStrategy)
    results.append("Test 5 Passed: Should default to MaleDefaultStrategy")
except AssertionError:
    results.append("Test 5 Failed: Should default to MaleDefaultStrategy")
"""

# Test 6: Process with Empty String
manager = TTSManager()
try:
    manager.process("", "female")  # Testing with an empty string
    assert True  # Assuming the method should not raise an error
    results.append("Test 6 Passed: Processed with empty string without errors.")
except Exception:
    results.append("Test 6 Failed: Processing with an empty string should not raise an error.")

# Print all test results
for result in results:
    print(result)


