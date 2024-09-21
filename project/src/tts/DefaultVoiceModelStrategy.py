from src.tts.BaseVoiceModelStrategy import BaseVoiceModelStrategy
from project.src.tts.DefaultVoiceModel import DefaultVoiceModel

class DefaultVoiceModelStrategy(BaseVoiceModelStrategy):
    """
    Default Voice Model Strategy class implementing BaseVoiceModelStrategy class.
    Implements a default selectable voice model that is returnable.

    methods:
        __init__(voiceType: DefaultVoiceType):
            Initialises the class with a chosen default model.
        getVoiceModel():
            Returns the file location of the voice model.
    """
    def __init__(self, voiceType: DefaultVoiceModel) -> None:
        """
        Initialises the class with a voice type.

        param: voiceType (DefaultVoiceType): default voice model to use when generating speech

        return: None: no returns
        """

        super().__init__()
        self.model = voiceType

    def getVoiceModel(self) -> str:
        """
        Return the path to a given voice model.

        return: str: Return a string, which is the file location of the voice model.
        """

        return self.model