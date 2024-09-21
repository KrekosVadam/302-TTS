from abc import ABC, abstractmethod

class BaseVoiceModelStrategy(ABC): 
    """
    Abstract Base Class defining the Voice Type Strategy.

    methods:
        getVoiceModel():
            Abstract method returning the path to a voice model.
    """
    @abstractmethod
    def getVoiceModel(self) -> str:
        """
        Return the path to a given voice model.

        return: str: Return a string, which is the file location of the voice model.
        """
        
        pass
