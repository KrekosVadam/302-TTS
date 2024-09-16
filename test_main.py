# test_main.py

from TTS_Shell.interface import process_text

# Call the subsystem to process the text and stream audio through onboard speakers
process_text(
    text="This is a sample text. It will be split into chunks and played back one by one.",
    voice_type="dummy"
)


# note for self
# tts_venv\Scripts\activate
