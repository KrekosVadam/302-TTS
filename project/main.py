from tts_manager import TTSManager 
from clone.tts_clone import TTSClone

#import onnx

def main():
    """Main function to select strategy and process text-to-speech."""

    # Initialise
    tts_manager = TTSManager()

    print("Welcome to the Piper-TTS program, created by Murdoch Miles!")
    print("Please select either [1] custom voice, [2] default male voice, or [3] default female voice.")

    # Ask for user input and ensure it's either '1' or '2'
    #action = 0;
    #while action < 1 or action > 3:
    action = input("Enter 1, 2, or 3: ").strip()

    if action == '1':
        clone = TTSClone()
        clone.run()
        a = input()
        voice_type = 'custom'
    elif action == '2':
        voice_type = 'male'
    elif action == '3':
        voice_type = 'female'

    # Hardcode text as a list
    #samples = ['Hey, I just ','got off work','and thought','I would give','you a call.']
    samples = ['Hey, I just got off work and thought I would give you a call.']

    # Process each text sample
    for sample in samples:
        tts_manager.process(sample, voice_type) # Call the process method
        
if __name__ == "__main__":
    main()
