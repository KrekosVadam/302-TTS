from abc import ABC, abstractmethod

class AbstractAudioPlayer(ABC):
    """
    Abstract base class for an audio player.
    This defines the methods that any concrete audio player must implement.
    """

    @abstractmethod
    def load_audio(self, audio_data):
        """
        Load audio data into the player.
        
        Args:
            audio_data: The audio data to be played.
        """
        pass

    @abstractmethod
    def play(self, delay=0.0):
        """
        Play the audio.
        
        Args:
            delay (float): Optional delay before starting the playback.
        """
        pass

    @abstractmethod
    def stop(self):
        """
        Stop the audio playback.
        """
        pass

    @abstractmethod
    def is_playing(self):
        """
        Check if the audio is currently playing.
        
        Returns:
            bool: True if the audio is playing, False otherwise.
        """
        pass
