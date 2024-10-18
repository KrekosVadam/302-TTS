from project.tts_manager import TTSManager 

def main():
    """Main function to select strategy and process text-to-speech."""

    # Initialise
    tts_manager = TTSManager()

    # Hard code voice type
    # Accepts male, female, custom, defaults to male
    voice_type = 'female'

    # Hardcode text as a list
    #samples = ['Hey, I just ','got off work','and thought','I would give','you a call.']
    samples = ['Hey, I just got off work and thought I would give you a call.']

    # Process each text sample
    for sample in samples:
        tts_manager.process(sample, voice_type) # Call the process method
        
if __name__ == "__main__":
    main()
