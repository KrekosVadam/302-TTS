from tts_manager import TTSManager

def main():
    """Main function to select strategy and process text-to-speech."""

    # Initialise
    tts_manager = TTSManager()

    # Hardcode text
    samples = [
        'Hey, I just ',
        'got off work',
        'and thought',
        'I would give',
        'you a call.']

    # Hard code voice type
    # Accepts male, female, custom, defaults to male
    voice_type = 'male'

    # Process each text sample
    for sample in samples:
        print(f"Processing sample: {sample}")
        tts_manager.process(sample, voice_type)

# Ensure the script runs when executed directly
if __name__ == "__main__":
    main()