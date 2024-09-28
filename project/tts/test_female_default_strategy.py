import unittest
from unittest.mock import patch, MagicMock
from female_default_strategy import FemaleDefaultStrategy

class TestFemaleDefaultStrategy(unittest.TestCase):
    
    @patch("piper.voice.PiperVoice") 
    def test_synthesize(self, mock_piper_voice):
        # Create a mock instance of PiperVoice
        mock_voice_instance = MagicMock()
        
        # Set up the mock to return an iterable of bytes
        mock_voice_instance.synthesize_stream_raw.return_value = [b"audio_chunk1", b"audio_chunk2"]
        
        # When PiperVoice.load is called, return the mock instance
        mock_piper_voice.load.return_value = mock_voice_instance
        
        # Create an instance of FemaleDefaultStrategy to test
        tts_strategy = FemaleDefaultStrategy()
        
        # Input text for the test
        input_text = "Hello, this is a test."
        
        # Call the synthesize method
        result = tts_strategy.synthesize(input_text)
        
        # Check that the PiperVoice.load method was called with the correct voice
        mock_piper_voice.load.assert_called_once_with("en_US-lessac-high")
        
        # Check that the synthesize_stream_raw method was called
        mock_voice_instance.synthesize_stream_raw.assert_called_once_with(input_text)
        
        # Verify the result is the expected iterable of bytes
        expected_output = [b"audio_chunk1", b"audio_chunk2"]
        self.assertEqual(list(result), expected_output)

# Run the unit tests
if __name__ == "__main__":
    unittest.main()
