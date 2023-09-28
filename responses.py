import random
import string

JOKES = [
    "I was her semicolon but...    One day She decided to switch to Python.",
    "I'm on a seafood diet....   I see food and I wanna eat it.",
    "*Dad thinks you are gaming on the pc* Dad: Are you winning, son?  There is"
    " no winning with these syntax errors dad!",
    "What’s the best thing about Switzerland? I don’t know, but the flag is a big plus.",
    "What is an astronaut’s favorite part on a computer? The space bar.", "Why are iPhone chargers not called Apple Juice?!"
]

ADJECTIVES = [
    "sleepy",
    "happy",
    "gross",
    "faster",
    "dusty",
    "cool",
    "messy",
    "mischievous",
    "garrulous",
    "long",
    "cold",
    "hot",
    "warm",
    "slow",
    "smelly",
    "wet",
    "fat",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
    "fluffy",
    "white",
    "proud",
    "brave",
    "proud",
    "beutiful",
    "extreme",
]

NOUNS = [
    "apples",
    "dog",
    "cat",
    "skyscraper",
    "house",
    "garden",
    "pen",
    "pencil",
    "car",
    "music",
    "computer",
    "mouse"
    "dinosaur",
    "ball",
    "toaster",
    "goat",
    "dragon",
    "hammer",
    "duck",
    "panda",
    "telephone",
    "banana",
    "teacher",
]

COLOURS = [
    "blue",
    "red",
    "green",
    "yellow",
    "purple",
    "magenta",
    "black",
    "white",
    "orange",
    "cyan",
    "brown",
    "silver",
    "gold",
    "aqua",
    "aquamarine",
]

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return "Hey there!"
    
    if p_message == "roll":
        return str(random.randint(1, 6))
    
    if p_message == "waka":
        return "Waka Woka Wiki Weke Woko Weki Wake ..."
    
    if p_message == "emp":
        return "earthmapspictures.weebly.com"
    
    if p_message == "!help":
        return "`This is a help message that you can modify.`"
    
    if p_message == "about":
        return "Copyright EarthMapsPictures Inc. 2015-2023 \nDeveloped by @aavvironalex and EarthMapsPictures Inc."
    
    if p_message == "greet":
        return "Hello I am EarthMapsPictures Bot. The Official EarthMapsPictures Website: https://earthmapspictures.weebly.com/"
    
    if p_message == "joke":
        return random.choice(JOKES)
    
    if p_message == "newpassword":
        
        adjective = random.choice(ADJECTIVES)
        noun = random.choice(NOUNS)
        number = random.randrange(0, 100)
        colour = random.choice(COLOURS)
        special_char = random.choice(string.punctuation)

        password = adjective + colour + noun + str(number) + special_char

        password = "Your password is: " + password

        return password
    