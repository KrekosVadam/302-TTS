<<<<<<< HEAD
=======
import threading
>>>>>>> c0478bedd220ed39c6ef7499399c6a2e8779a858
import numpy as np

<<<<<<< HEAD
from tts.tts_strategy import TTSStrategy
from tts.male_default_strategy import MaleDefaultStrategy
from tts.female_default_strategy import FemaleDefaultStrategy
from tts.custom_strategy import CustomStrategy
from sound_stream.audio_player import AudioPlayer
=======
from project.tts.tts_strategy import TTSStrategy
from project.tts.male_default_strategy import MaleDefaultStrategy
from project.tts.female_default_strategy import FemaleDefaultStrategy
from project.tts.custom_strategy import CustomStrategy
>>>>>>> c0478bedd220ed39c6ef7499399c6a2e8779a858

class TTSManager:
    """
    Acts as the context class responsible for managing the process of turning Text to Speech

    methods
        process(text: str, voice_type: str):
            Handles passing the text to the respective voice model
            Passes the returned list of bytes to the audio player
    """
    
    def __init__(self, tts_strategy=MaleDefaultStrategy):
        self.tts_strategy = tts_strategy
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
<<<<<<< HEAD

        # Create audio
        audio = self.tts_strategy.synthesize(text)

        # Convert the returned list to a numpy array
        audio_array = np.array(audio, dtype=np.int16)

        # Play audio
        self.audio_player.play_audio(audio_array)
=======
            
        self.tts_strategy.synthesize(text)  
        audio = self.tts_strategy.synthesize(text)  

#----------------------------------------START OF UNIT TESTING----------------------------------------------------------------------------------------
"""
results = []

# Test 1: Initialization of TTSManager
manager = TTSManager()
try:
    assert manager.tts_strategy is None  
    results.append("Test 1 Passed: TTSManager is initialized correctly.")
except AssertionError:
    results.append("Test 1 Failed: TTSManager should initialize tts_strategy to None.")

# Test 2: Male Voice

manager.process("Hello, this is a test.", "male")
try:
    assert isinstance(manager.tts_strategy, MaleDefaultStrategy)
    results.append("Test 2 Passed: Should use MaleDefaultStrategy")
except AssertionError:
    results.append("Test 2 Failed: Should use MaleDefaultStrategy")

# Test 3: Female Voice
manager = TTSManager()
manager.process("Hello, this is a test.", "female")
try:
    assert isinstance(manager.tts_strategy, FemaleDefaultStrategy)
    results.append("Test 3 Passed: Should use FemaleDefaultStrategy")
except AssertionError:
    results.append("Test 3 Failed: Should use FemaleDefaultStrategy")
    
# Test 4: Custom Voice

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

# Test 6: Process with Empty String
manager = TTSManager()
try:
    manager.process("", "female")  # Testing with an empty string
    assert True  # Assuming the method should not raise an error
    results.append("Test 6 Passed: Processed with empty string without errors.")
except Exception:
    results.append("Test 6 Failed: Processing with an empty string should not raise an error.")

# Test 7: Process with None Text
manager = TTSManager()
try:
    manager.process(None, "female")  # Testing with None as text
    assert True  # Assuming the method should not raise an error
    results.append("Test 7 Passed: Processed with None as text without errors.")
except Exception:
    results.append("Test 7 Failed: Processing with None should not raise an error.")

# Test 8: Process with Valid Text but No Voice Type

manager = TTSManager()
manager.process("Hello, this is a test.", "")  # Passing empty voice type
try:
    assert isinstance(manager.tts_strategy, MaleDefaultStrategy)
    results.append("Test 8 Passed: Should default to MaleDefaultStrategy when voice type is empty.")
except AssertionError:
    results.append("Test 8 Failed: Should default to MaleDefaultStrategy when voice type is empty.")


# Test 9: Check if the audio is generated
manager.process("Check synthesis", "female")  # Process with female voice
try:
    audio_output = manager.tts_strategy.synthesize("Check synthesis")  # Call synthesize to get the output
    assert audio_output is not None  # Check if the output is not None  
    # Check if audio_output is a generator and consume it
    audio_data = list(audio_output)  # Convert generator to a list to consume it  
    assert len(audio_data) > 0  # Ensure that the generator yields some audio data
    results.append(f"Test 9 Passed: Synthesize produced an output. Type of audio output: {type(audio_output)}. Number of audio chunks: {len(audio_data)}.")
except Exception as e:
    results.append(f"Test 9 Failed: An error occurred - {str(e)}")
    
# Test 10: Ensure Only One Strategy is Set
manager = TTSManager()
manager.process("First call", "male")
manager.process("Second call", "female")  # Change strategy to male
try:
    assert isinstance(manager.tts_strategy, FemaleDefaultStrategy)  # Check the last strategy set
    results.append("Test 10 Passed: Only one strategy should be set at a time.")
except AssertionError:
    results.append("Test 10 Failed: There should only be one strategy set.")
       
# Print all test results
for result in results:
    print(result)    
"""
#----------------------------------------END OF UNIT TESTING----------------------------------------------------------------------------------------
>>>>>>> c0478bedd220ed39c6ef7499399c6a2e8779a858
