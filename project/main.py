from tts_manager import TTSManager 
from clone.tts_clone import TTSClone

#import onnx

def main():
    """Main function to select strategy and process text-to-speech."""

    # Initialise
    tts_manager = TTSManager()
    clone = TTSClone()

    print("Welcome to the Piper-TTS program, created by Murdoch Miles!")
    
    while True:
        print("\nPlease select from the following:")
        print("1. Train a voice")
        print("2. Male Voice")
        print("3. Female Voice")
        print("4. Custom Voice")
        print("q: Quit\n")

        action = input("Enter 1, 2, 3, 4 or q: ").strip()

        if action == '1':
            clone.run() 
        elif action == '2':
            voice_type = 'male'
        elif action == '3':
            voice_type = 'female'
        elif action == '4':
            voice_type = 'custom'
        elif action.lower() == 'q':
            print("Terminating program.")
            break
        else:
            print("Invalid input.")
            continue
            
        while action in ('2', '3', '4'):
            print("\nEnter text to synthesize or 'x' to go back to the main menu and change the voice:")
            sample = input("Text: ").strip()

            if sample.lower() == 'x:
                break  # return to the main menu
            else:
                tts_manager.process(sample, voice_type)  # Synthesize speech
            
if __name__ == "__main__":
    main()
