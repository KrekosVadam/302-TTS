from tts_manager import TTSManager 
from clone.tts_clone import TTSClone

#import onnx

def main():
    """Main function to select strategy and process text-to-speech."""

    # Initialise
    tts_manager = TTSManager()

    print("Welcome to the Piper-TTS program, created by Murdoch Miles!")
    print("Please select from the following:")
    
    print("1. Train a voice")
    print("2. Male Voice")
    print("3. Female Voice")
    print("4. Custom Voice")

    # Ask for user input and ensure it's either '1' or '2'
    #action = 0;
    #while action < 1 or action > 3:
    action = input("Enter 1, 2, or 3: ").strip()

    if action == '1':
        clone = TTSClone()
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
            tts_manager.process(sample, voice_type) # call the process method
        
if __name__ == "__main__":
    main()
