from clone.tts_clone import TTSClone

#import onnx

def main():
    """Main function to select strategy and process text-to-speech."""

    clone = TTSClone()
    clone.run()

# Ensure the script runs when executed directly
if __name__ == "__main__":
    main()