import time
from project.tts_manager import TTSManager 

def main():
    """Main function to select strategy and process text-to-speech."""

    # Initialise
    tts_manager = TTSManager()

    # Hard code voice type
    # Accepts male, female, custom, defaults to male
    voice_type = 'male'

    # Hardcode text as a list
    samples = ['Hey, I just ','got off work','and thought','I would give','you a call.']
    #samples = ['Hey, I just got off work and thought I would give you a call.']

    # Process each text sample
    for sample in samples:
        print(f"Processing sample: {sample}")
        
        start_time = time.time() # Start time measurement
        tts_manager.process(sample, voice_type) # Call the process method
        end_time = time.time()         # End time measurement
        inference_time = end_time - start_time # Calculate inference time
        print(f"Inference time for sample: {inference_time:.4f} seconds")
        
if __name__ == "__main__":
    main()
