import csv
from tts_manager import TTSManager

def read_samples_from_csv(file_path):
    """Read samples from a CSV file and return a list of text chunks."""
    samples = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                samples.append(row[0]) 
    return samples

def main():
    """Main function to select strategy and process text-to-speech."""
    
    # Path to the CSV file containing text samples
    csv_file_path = 'phonetext.csv'

    # Read samples from the CSV file
    samples = read_samples_from_csv(csv_file_path)

    # Initialize the TTS Manager with the chosen strategy
    tts_manager = TTSManager(tts_strategy=tts_strategy)

    # Process each text sample
    for sample in samples:
        print(f"Processing sample: {sample}")
        tts_manager.process(sample, max_words=10)  # Adjust max_words as needed

# Ensure the script runs when executed directly
if __name__ == "__main__":
    main()
