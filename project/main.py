"""
This is a test file for the TTS subsystem

import tts_processor

if __name__ == "__main__":
    if tts_processor:
        print("confirmed and working !")
"""

import csv
from tts_manager import TTSManager
from tts.default_strategy import DefaultStrategy
from tts.female_default_strategy import FemaleDefaultStrategy
from tts.male_default_strategy import MaleDefaultStrategy

def read_samples_from_csv(file_path):
    """Read samples from a CSV file and return a list of text chunks."""
    samples = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                samples.append(row[0])  # Assuming each row contains a text chunk
    return samples

def main():
    """Main function to select strategy and process text-to-speech."""
    
    # Path to the CSV file containing text samples
    csv_file_path = 'phonetext.csv'

    # Read samples from the CSV file
    samples = read_samples_from_csv(csv_file_path)

    # Ask the user to choose a TTS strategy
    print("Choose a TTS strategy:")
    print("1. Default Strategy")
    print("2. Female Default Strategy")
    print("3. Male Default Strategy")

    # Get user choice
    choice = input("Enter the number of your choice (1-3): ")

    # Determine the strategy based on user input
    if choice == '1':
        tts_strategy = DefaultStrategy()
    elif choice == '2':
        tts_strategy = FemaleDefaultStrategy()
    elif choice == '3':
        tts_strategy = MaleDefaultStrategy()
    else:
        print("Invalid choice, defaulting to Default Strategy.")
        tts_strategy = DefaultStrategy()

    # Initialize the TTS Manager with the chosen strategy
    tts_manager = TTSManager(tts_strategy=tts_strategy)

    # Process each text sample
    for sample in samples:
        print(f"Processing sample: {sample}")
        tts_manager.process(sample, max_words=10)  # Adjust max_words as needed

# Ensure the script runs when executed directly
if __name__ == "__main__":
    main()
