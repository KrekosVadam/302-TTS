from project.tts_manager import TTSManager

import onnx

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
    voice_type = 'female'

    # Process each text sample
    for sample in samples:
        print(f"Processing sample: {sample}")
        tts_manager.process(sample, voice_type)

# Ensure the script runs when executed directly
if __name__ == "__main__":
    main()
#-------------------
#Test1
tts_manager = TTSManager()
samples1 = ['Hey, I just ']
outputs1 = []
expected_outputs1 = [
    "Processing sample: Hey, I just "
]
for sample in samples1:
    output = f"Processing sample: {sample}"
    tts_manager.process(sample, 'female')
    outputs1.append(output)
try:
    for expected in expected_outputs1:
        assert expected in outputs1
    print("Test 1 passed!")
except AssertionError as e:
    print(f"Test 1 failed: {e}")

# Test 2: Empty Sample
samples2 = ['']  # Testing with an empty string
outputs2 = []
expected_outputs2 = ["Processing sample: "]
for sample in samples2:
    output = f"Processing sample: {sample}"
    tts_manager.process(sample, 'female')
    outputs2.append(output)
try:
    for expected in expected_outputs2:
        assert expected in outputs2
    print("Test 2 passed!")
except AssertionError as e:
    print(f"Test 2 failed: {e}")

# Test 3: Long Sample
samples3 = [
    'This is a long sample that goes on and on, ',
    'to test the text-to-speech functionality.'
]
outputs3 = []
expected_outputs3 = [
    "Processing sample: This is a long sample that goes on and on, ",
    "Processing sample: to test the text-to-speech functionality."
]
for sample in samples3:
    output = f"Processing sample: {sample}"
    tts_manager.process(sample, 'female')
    outputs3.append(output)
try:
    for expected in expected_outputs3:
        assert expected in outputs3
    print("Test 3 passed!")
except AssertionError as e:
    print(f"Test 3 failed: {e}")
    
# Test 4: Special Characters
samples4 = ['@#$%^&*()!']  # Testing with special characters
outputs4 = []
expected_outputs4 = ["Processing sample: @#$%^&*()!"]
for sample in samples4:
    output = f"Processing sample: {sample}"
    tts_manager.process(sample, 'female')
    outputs4.append(output)
try:
    for expected in expected_outputs4:
        assert expected in outputs4
    print("Test 4 passed!")
except AssertionError as e:
    print(f"Test 4 failed: {e}")
