from tts_manager import TTSManager 
from clone.tts_clone import TTSClone

#import onnx

def main():
    """Main function to select strategy and process text-to-speech."""

    # Initialise
    tts_manager = TTSManager()
    clone = TTSClone()


    # BELOW IS INCLUDED FOR DEMONSTRATION

    print("Welcome to the Piper-TTS program, created by Murdoch Miles!")
    print("Please select from the following:")
    
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
        
    while action in ('2', '3', '4'):
        print("Enter text:")
        sample = input().strip()
        if sample.lower() == 'q':
            break  # exit
        else:
            tts_manager.process(sample, voice_type) # this is the main method used to synthesise speech from text
        
if __name__ == "__main__":
    main()
