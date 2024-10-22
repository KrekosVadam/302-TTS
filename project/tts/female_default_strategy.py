import numpy as np

from piper.voice import PiperVoice
from project.tts.tts_strategy import TTSStrategy

class FemaleDefaultStrategy(TTSStrategy):
    """
    Default TTS Strategy class implementing the TTSStrategy interface. 
    This allows for a default voice to be used, no voice clone, etc.

    methods:
        synthesize(text: str):
            Generate speech from a chunk of text.
    """
    
    def synthesize(self, text: str):
        """
        Concrete method for generating default speech for the given text chunk.

        Args: 
            text (str): A string representing the segment of text to be converted 
                         into speech.

        return: a numpy array
        """
        # Empty list
        audio_data = []

        # Load voice model
        voice = PiperVoice.load("project/voices/en_US-lessac-high.onnx")

        # Loop through text and create voice then add to list
        for audio_bytes in voice.synthesize_stream_raw(text):
            int_data = np.frombuffer(audio_bytes, dtype=np.int16)
            audio_data.append(int_data)

        # Join
        # Concatenate all chunks in the list to form a single audio array
        audio_array = np.concatenate(audio_data)

        # return list
        return audio_array

#----------------------------------------START OF UNIT TESTING----------------------------------------------------------------------------------------
"""
strategy = FemaleDefaultStrategy()

# Test 1: Check if the FemaleDefaultStrategy object is initialized properly.
try:
    if isinstance(strategy, FemaleDefaultStrategy):
        print("Test 1 Passed: FemaleDefaultStrategy initialized successfully.")
    else:
        print("Test 1 Failed: FemaleDefaultStrategy not initialized correctly.")
except Exception as e:
    print(f"Test 1 Failed: An error occurred during initialization check - {e}")

# Test 2: Check if the synthesize method returns a numpy array.
text_input = "Hello, this is a test."
try:
    result = strategy.synthesize(text_input)
    if isinstance(result, np.ndarray):
        print("Test 2 Passed: synthesize returns a numpy array.")
    else:
        print("Test 2 Failed: synthesize did not return a numpy array.")
except Exception as e:
    print(f"Test 2 Failed: An error occurred during synthesize - {e}")

# Test 3: Check if the length of the output is greater than 0 for valid input.
try:
    result = strategy.synthesize(text_input)
    if len(result) > 0:
        print("Test 3 Passed: synthesize output length is greater than 0.")
    else:
        print("Test 3 Failed: synthesize output length is 0.")
except Exception as e:
    print(f"Test 3 Failed: An error occurred during length check - {e}")

# Test 4: Check if the synthesize method can handle empty input without error.
empty_text_input = ""
try:
    result = strategy.synthesize(empty_text_input)
    if isinstance(result, np.ndarray):
        print("Test 4 Passed: synthesize handles empty input without error.")
    else:
        print("Test 4 Failed: synthesize did not return a numpy array for empty input.")
except Exception as e:
    print(f"Test 4 Failed: An error occurred during empty input check - {e}")

# Test 5: Check if the synthesize method raises an error for non-string input.
invalid_text_input = 12345  # Integer instead of string
try:
    result = strategy.synthesize(invalid_text_input)  # This should raise an error
    print("Test 5 Failed: Invalid input type was not handled.")
except Exception as e:
    print(f"Test 5 Passed: Error raised as expected for invalid input type")

# Test 6: Check if the audio data generated is of the expected dtype.
text_input = "Testing audio generation."
try:
    result = strategy.synthesize(text_input)
    if result.dtype == np.int16:
        print("Test 6 Passed: Output audio data is of expected dtype int16.")
    else:
        print("Test 6 Failed: Output audio data is not of expected dtype int16.")
except Exception as e:
    print(f"Test 6 Failed: An error occurred during dtype check - {e}")
"""
#----------------------------------------END OF UNIT TESTING----------------------------------------------------------------------------------------
