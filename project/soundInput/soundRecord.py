import time
import sounddevice as sd
import wave
import numpy as np
import os

class SoundRecord:
    """
    Class responsible for playing audio in the background.

    methods:
        input_prompt():
    """

    def __init__(self):
        pass

    def input_prompt(self):

        # Entry statements
        messages = [
            "Welcome to our voice recording.",
            "In this section, you will be prompted with some sentences to say and the system will record your voice for use.",
            "For best results, our system requires the following: ",
            "A high quality microphone.",
            "As clear audio as possible, such as, no background noise.",
            "If these requirements are not met, the quality of the model will decrease.",
            "Some of the sentences may appear to be silly, but they are used to collect samples of different pronunciations.",
            "The system requires 111 recordings, so please make sure you have enough time to do so.",
            "An estimation for amount of time needed is 30 minutes but please allow for extra to be safe.",
            "Please say the following lines."
            "Use the Enter key to start and stop recordings."
        ]

        # Loop through message prompts for user
        for message in messages:
            print(message)
            #time.sleep(2) # Add a small delay to not bombard user with texts

        # Hard code text to say
        # TODO wrap in a function reading from a file instead?
        script = [
            "When I was younger, I always knew my parents were working hard for the family."
            "There is no sandy beach, but if you like rocks and deep waters, it is the perfect place.",
            "It's a place where you see Earth for what it has come to be over the course of millions of years, not for the things we've done to it.",
            "I was having a bad day, it was around four P M and I was struggling to make things happen.",
            "If you can't stand the heat, get out of the kitchen and fire up the grill.",
            "Small incremental changes in your diet to increase whole-grain intake will make a difference over time.",
            "She opened the first red box, then she found our first super expensive rent bill.",
            "Okay, but I want the furniture in the living room to be yellow and dark blue.",
            "Afterwards, the teacher decided to do a class project to see what kind of impact the recognition would have on a community.",
            "It's hard to deny that tomatoes are the ideal summer food – and that's saying a lot in a season where so much produce is at its peak.",
            "We also recommend the grilled choices where you get a variety of fresh meat and fish dishes.",
            "You won't have to spend much time over the flame, but if you want a hot meal on a hot day, grilled dishes with tomatoes fit the bill.",
            "The two brightest planets in the sky, Venus and gas giant Jupiter, will get so close that they'll appear to collide and become one planet.",
            "He was just a guy who saw a dirty girl on the street who needed to eat.",
            "I don't often eat lunch at work, and tend to just work through the day and eat dinner when I get home.",
            "Fire up the grill, and give your peaches a little heat, to turn them into a sweetly charred accompaniment for a number of dishes.",
            "Instead, stir up a no-cook tomato sauce that practically explodes with the juiciness of fresh tomatoes.",
            "I reached in and pulled out a huge manila envelope that was bulky, but I couldn't tell what was in it.",
            "And that means going beyond benefits like vacation days and retirement plans, and considering things like the company's culture, manager expectations, job satisfaction and development, and work-life balance.",
            "You only think about the earth, but you should also consider the sky and the sea.",
            "They kept on walking until they found an oasis, where they decided to take a bath.",
            "Having complete focus on a recipe, and not allowing yourself to be distracted by your thoughts, can have a therapeutic effect.",
            "Yellowstone National Park also serves as a time capsule, a sort of 'land that time forgot' in terms of wildlife.",
            "Several methods to reduce livestock methane emissions are being tested, including adding seaweed to cattle diets.",
            "If being able to work from home is important to you, it's good to get a sense of a company's flexibility before getting too far along in the interview process.",
            "When it comes down to it, almost anything can be a salad or a sandwich – the potential combinations are endless.",
            "Turn it into the base for a Cobb salad with as many tomatoes and leftover fridge elements as you can handle.",
            "I may be scarce, but I am precious for I serve the needs of human life.",
            "Overnight oats are a trend that's not going away anytime soon, and summer is the ideal time to embrace this chilled-out breakfast dish.",
            "What was then said and thought still speaks to us as vividly as ever from the printed page.",
            "Although the occasion isn't going to turn us into smart savers, it sure is a good reminder.",
            "While my dog sniffed the ground, I opened my heart to the wonder of Nature's creation.",
            "I had forgotten to check the weather report for today, however, so I wasn't sure if I needed my light jacket or my heavy coat.",
            "And after that, the monkey climbed down from the tree and went to the riverside.",
            "I'm telling you, the charming, graceful sick person is just a myth, an urban legend.",
            "The chef is the mother of the family, and the majority of the ingredients used for the dishes are produced by the same family.",
            "Eating the whole grain, as our ancestors used to do, provides a host of benefits to the body that are lost when the grain is processed.",
            "Oh, it had been cold and snowy two days ago, and warm and rainy yesterday.",
            "Grilled peaches become the star of the show in a big salad, like this quinoa, peach and summer vegetable salad that works as a main course.",
            "The only effect of time has been to sift, like this quinoa, peach and summer vegetable salad that works as a main course.",
            " out the bad products, for nothing in literature can long survive but what is really good.",
            "One way to increase your chances of getting a lower rate, is to come prepared with information on other card offers that you have seen available, he said.",
            "This was matched by a dive downward by bassoons, bass clarinet, trombones and bass tuba.",
            "And if you want to pile on more ingredients, you'll find ways to make a tomato sandwich every day of the week.",
            "But it is very important to understand the fees, what the rate will be after the low-rate period ends and if there are any deadlines with balance transfer cards.",
            "Red is the colour of passion and of love, the red rose, the poinsettia and the poppy.",
            "Time is of no account with great thoughts, which are as fresh today as when they first passed through their author’s minds, ages ago.",
            "It is the water that is the basis of life and drawn up by the clouds from the deep sea.",
            "Here is another reason to get serious about saving - it is a new year.",
            "When they had all gone and come back, he called them together to describe what they had seen.",
            "You can experiment with these grains by incorporating them in small amounts into your morning bowl of oatmeal.",
            "The snow leopard appears to be doing well and is showing no additional symptoms, the zoo said.",
            "In addition to enjoying them raw and cooked in desserts, fresh peaches can be roasted, pickled, and even frozen for a burst of summer sunshine in the middle of winter.",
            "The flour in white breads, bagels, pastries and pasta has lost the grain's fibre-rich outer layer during the refining process.",
            "A single serving of whole grains is one slice of whole-grain bread, or a half cup of oats, or a half cup of brown rice.",
            "They helped finish off his birthday cake, while his other family enjoyed a cake too.",
            "It is so nice that every time you look at a sunflower, the whole world starts to smile.",
            "This blueberry coffee cake is my go-to recipe for all of our holiday get-togethers, because it's perfect for breakfast or dessert.",
            "I got dressed quickly because I knew both of my dogs would be eager to get outside for their morning walk.",
            "The dish is topped with crushed red and green chili, and you can heap it over rice, or scoop it all up with a buttered baguette.",
            "Every week my father would call the boy and get a 'generic' answering-machine message.",
            "Here's how you can maximize your peach perfection with recipe ideas for breakfast, lunch, dinner – and dessert, of course.",
            "Consuming fresh tomatoes with a source of fat, such as olive oil, is a great way to boost lycopene absorption, she said.",
            "I got the habit of visiting the church cemetery from my father, and of reading the newspaper, too.",
            "It was still dark outside, so I felt my way to the wall switch and turned on the light.",
            "As a restaurant owner I knew this thing was gold the moment I saw it.",
            "We all have our own methods of dealing with money, but here are a couple of saving tricks that will grow your money.",
            "In all of its sweet seasons here, it had never failed to touch my soul.",
            "I once saw nine different grizzly bears in one day and had almost forty bighorn sheep wander with me one day as I ate my lunch.",
            "She wishes she can run into the 'business man' who bought her lunches, and say something.",
            "The development is set to transform an old industrial site into an interconnected smart city.",
            "The monkey climbed up the tree and looked down at the river and the lake every day.",
            "But even this description is an understatement – the otherworldly nature of the area simply evokes awe.",
            "Or simply drizzle them with balsamic vinegar and quality olive oil along with a sprinkling of flaky sea salt and serve as a fruit salad.",
            "People love it, as it was laden with blossoms that smelled so sweet and looked so beautiful.",
            "The book he gave me was really interesting despite the strange title it had.",
            "Then I thanked Nature for the love that created the moon, the stars, and me.",
            "While the oil heats, dredge the chops in the flour, batting off any extra, then in the egg, then in the bread crumbs.",
            "Books introduce us into the best society, they bring us into the presence of the greatest minds that have ever lived.",
            "Foil packet meals are quite possibly the easiest way to grill with very little mess and clean-up.",
            "I had a feeling I knew who had sent it, but didn't want to tell my mom.",
            "Reasonably priced salads, crepes, fresh fish and a large selection of ice cream are served.",
            "Baking is very good for focusing the mind because it often relies on very exact measurements.",
            "Lee says he steams his rolls the day before, and leaves them in the fridge to rest, so that they are crispier and browner when he fries them.",
            "First, she told each of them how they had made a difference to her and the class.",
            "I can still remember gazing endlessly at the photographs of granite peaks, roaring waterfalls and magnificent wildlife, and daydreaming about wandering in those landscapes.",
            "I truly witnessed a love that brought me to tears when I got home from work last night.",
            "To grill peaches, preheat a gas or charcoal grill to medium heat, halve and pit the peaches, then brush the cut halves with olive oil or vegetable oil.",
            "One day my little dog Milo escaped the fenced yard of a friend in Vancouver and ran off.",
            "As we know, men often discover their affinity to each other by the mutual love.",
            "Their experience becomes ours, and we feel as if we were, in a measure, actors with them in the scenes which they describe.",
            "It's worthwhile mentioning that just a few hundred metres away there is an access to the sea.",
            "They waited for me in a grocery store parking lot until I came to pick him up.",
            "As I told him my name was Angela, my mom handed me the soup ladle and hair net to start getting to work.",
            "He would rather sit and read the paper and drink a cup of coffee.",
            "I decided on my light jacket, pulled it on, and leashed up my bigger dog, Fluffy, to walk first.",
            "Add fresh sliced peaches to a mason jar with oats, milk and spices, and you've got a sweet peach cobbler-inspired treat waiting for you in the morning.",
            "Last Thursday, wildlife care specialists noticed the snow leopard had a cough and nasal discharge, the zoo said in a new release.",
            "The Park has been a global leader in establishing the range of possibilities and approaches to caring for wild animals and landscapes.",
            "Gave my twenty-eight-year-old self a snack and a juice box and it was the most caring thing I've ever had a boss do.",
            "Only by forgetting can you walk towards the kind of life that you want with lighter steps.",
            "A familiar man called me back saying he thought I left something in our mailbox.",
            "The place is quite remote and is perfect for a relaxed swim before going for your meal.",
            "It is perfect for families since the kids can safely run around and play in the garden.",
            "Try this recipe as a start, and pick and choose add-ins like roasted red peppers and marinated chickpeas to suit your tastes.",
            "It had heated my heart on the coldest days and lighted my spirit on the darkest nights.",
            "The paste adds umami, while coriander powder gives it an earthy lift, which balances the heaviness of the pork belly.",
            "But we can eat in the summer on the balcony and in the winter in the living room.",
            "The two reservoirs fed by the Colorado River watershed, provide a critical supply of drinking water and irrigation for many across the region, including rural farms, ranches and native communities.",
            "As well as dwellings, the proposal would also introduce comprehensive planting to strengthen all boundaries, and ensure the next generation of mature trees and hedgerows, will flourish on the site.",
            "Place salmon fillets on a piece of heavy-duty foil drizzled with olive oil and load them up with halved cherry tomatoes and herbs like rosemary, dill or cilantro."
            ]
        
        save_directory = "/project/project/voices/custom-voice-samples/wav"
        
        counter = 1

        for text in script:
            # say text
            print("\n",text,"\n")

            # user input to start recording
            input("Press Enter to start recording")
            
            # open stream
            print("Recording in progress.")
            audio_input = []

            with sd.InputStream(samplerate=22050, channels=1) as stream:
                while True:
                    # Read audio data from the stream
                    audio_chunk, _ = stream.read(1024)
                    audio_input.append(audio_chunk)

                    # user input to stop recording
                    stop = input("Press Enter to stop recording: ")
                    if stop.strip() == "":
                        break

            # save file
            file_name = "{counter}.wav"
            file_path = os.path.join(save_directory, file_name)
            audio_data = np.concatenate(audio_input, axis=0)

            # Save the audio data as a .wav file
            with wave.open(file_path, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2) 
                wf.setframerate(22050)
                wf.writeframes(audio_data.tobytes())

            # iterative counter for file saves
            counter + 1