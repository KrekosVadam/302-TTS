import numpy as np

from project.tts.tts_strategy import TTSStrategy
from project.tts.male_default_strategy import MaleDefaultStrategy
from project.tts.female_default_strategy import FemaleDefaultStrategy
from project.tts.custom_strategy import CustomStrategy
from project.sound.audio_player import AudioPlayer

class TTSManager:
    """
    Acts as the context class responsible for managing the process of turning Text to Speech

    methods
        process(text: str, voice_type: str):
            Handles passing the text to the respective voice model
            Passes the returned list of bytes to the audio player
    """
    
    #def __init__(self, tts_strategy=MaleDefaultStrategy):
        #self.tts_strategy = tts_strategy
        #self.audio_player = AudioPlayer()

    def __init__(self, tts_strategy=None):
        if tts_strategy is None:
            self.tts_strategy = MaleDefaultStrategy()  
        else:
            self.tts_strategy = tts_strategy()
        self.audio_player = AudioPlayer()
    
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

        # Create audio
        audio_array = self.tts_strategy.synthesize(text)

        # Play audio
        self.audio_player.play_audio(audio_array)
           


#----------------------------------------START OF UNIT TESTING----------------------------------------------------------------------------------------
"""
# Test 1: Ensure TTSManager can be initialized with the default MaleDefaultStrategy
try: 
    manager = TTSManager()  # This should create an instance with tts_strategy initialized.
    assert isinstance(manager.tts_strategy, MaleDefaultStrategy)
    print("Test 1 Passed: TTSManager is initialized correctly.")
except AssertionError:
    print("Test 1 Failed: TTSManager should initialize tts_strategy to MaleDefaultStrategy.")

# Test 2: Test process with male voice type
try:
    manager = TTSManager()
    manager.process("Hello, this is a test.", "male")
    print("Test 2 Passed: process works with male voice type.")
except Exception as e:
    print(f"Test 2 Failed: An error occurred with male voice type - {e}")
    
# Test 3: Test process with female voice type
try:
    manager = TTSManager()
    manager.process("Hello, this is a test.", "female")
    print("Test 3 Passed: process works with female voice type.")
except Exception as e:
    print(f"Test 3 Failed: An error occurred with female voice type - {e}") 

# Test 4: Test process with custom voice type
#try:
    #manager = TTSManager()
    #manager.process("Hello, this is a test.", "custom")
    #print("Test 4 Passed: process works with custom voice type.")
#except Exception as e:
    #print(f"Test 4 Failed: An error occurred with custom voice type - {e}")

# Test 5: Test process with an unknown voice type (should default to MaleDefaultStrategy)
try:
    manager = TTSManager()
    manager.process("Hello, this is a test.", "unknown")
    print("Test 5 Passed: process works with unknown voice type (defaults to male).")
except Exception as e:
    print(f"Test 5 Failed: An error occurred with unknown voice type - {e}")

# Test 6: Test process with empty text
try:
    manager = TTSManager()
    manager.process("", "male")  # Empty text should be handled gracefully
    print("Test 6 Passed: process handles empty text without error.")
except Exception as e:
    print(f"Test 6 Failed: An error occurred with empty text - {e}")

# Test 7: Test process with invalid text type (number instead of string)
try:
    manager = TTSManager()
    manager.process(12345, "male")  
    print("Test 7 Failed: Invalid input type was not handled.")
except Exception as e:
    print(f"Test 7 Passed: Error raised as expected for invalid input type")

# Test 8: Process with Valid Text but No Voice Type
try:
    manager = TTSManager()
    manager.process("Hello, Empty voice type should be gracefully handled", "")  
    print("Test 8 Passed: process handles empty text without error.")
except Exception as e:
    print(f"Test 8 Failed: An error occurred with empty text - {e}")4

"""      
#----------------------------------------END OF UNIT TESTING----------------------------------------------------------------------------------------
