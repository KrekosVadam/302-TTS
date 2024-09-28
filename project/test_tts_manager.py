import unittest
from unittest.mock import patch, MagicMock
from project.tts_manager import TTSManager

class TestTTSManager(unittest.TestCase):

    @patch('project.tts.male_default_strategy.MaleDefaultStrategy')
    @patch('project.tts.female_default_strategy.FemaleDefaultStrategy')
    @patch('project.tts.custom_strategy.CustomStrategy')
    @patch('simpleaudio.play_buffer')
    def test_process_male_voice(self, mock_play_buffer, mock_custom_strategy, mock_female_strategy, mock_male_strategy):
        # Arrange
        tts_manager = TTSManager()
        mock_male_strategy.return_value.synthesize.return_value = [0.5, -0.5, 0.3]  # Mock audio output

        # Act
        tts_manager.process("Hello, world!", "male")

        # Assert
        mock_male_strategy.assert_called_once()
        mock_play_buffer.assert_called_once()

    @patch('project.tts.female_default_strategy.FemaleDefaultStrategy')
    @patch('project.tts.custom_strategy.CustomStrategy')
    @patch('simpleaudio.play_buffer')
    def test_process_female_voice(self, mock_play_buffer, mock_custom_strategy, mock_female_strategy):
        # Arrange
        tts_manager = TTSManager()
        mock_female_strategy.return_value.synthesize.return_value = [0.5, -0.5, 0.3]  # Mock audio output

        # Act
        tts_manager.process("Hello, world!", "female")

        # Assert
        mock_female_strategy.assert_called_once()
        mock_play_buffer.assert_called_once()

    @patch('project.tts.male_default_strategy.MaleDefaultStrategy')
    @patch('project.tts.female_default_strategy.FemaleDefaultStrategy')
    @patch('project.tts.custom_strategy.CustomStrategy')
    @patch('simpleaudio.play_buffer')
    def test_process_custom_voice(self, mock_play_buffer, mock_custom_strategy, mock_female_strategy, mock_male_strategy):
        # Arrange
        tts_manager = TTSManager()
        mock_custom_strategy.return_value.synthesize.return_value = [0.5, -0.5, 0.3]  # Mock audio output

        # Act
        tts_manager.process("Hello, world!", "custom")

        # Assert
        mock_custom_strategy.assert_called_once()
        mock_play_buffer.assert_called_once()

    @patch('project.tts.male_default_strategy.MaleDefaultStrategy')
    @patch('project.tts.female_default_strategy.FemaleDefaultStrategy')
    @patch('project.tts.custom_strategy.CustomStrategy')
    @patch('simpleaudio.play_buffer')
    def test_process_default_voice(self, mock_play_buffer, mock_custom_strategy, mock_female_strategy, mock_male_strategy):
        # Arrange
        tts_manager = TTSManager()
        mock_male_strategy.return_value.synthesize.return_value = [0.5, -0.5, 0.3]  # Mock audio output

        # Act
        tts_manager.process("Hello, world!", "unknown")  # Using an unknown voice type

        # Assert
        mock_male_strategy.assert_called_once()  # Should default to MaleDefaultStrategy
        mock_play_buffer.assert_called_once()

if __name__ == '__main__':
    unittest.main()
