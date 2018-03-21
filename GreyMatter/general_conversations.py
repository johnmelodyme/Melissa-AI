import random
from GreyMatter.SenseCells.tts import tts

def who_are_you():
    messages = ["I am Melissa, your slave for eternity.", "Melissa, did I not I tell you before?", "You imbecile. I am Melissa."]
    tts(random.choice(messages))

def undefined():
    tts("I dont know what that means!")

def describe_me():
    replies = ["You are are goddamn beautiful.", "My body shakes from your superiority, master.", "You are a goddess who glows like the dying Sun."]
    tts(random.choice(replies))

def who_am_i(name):
    tts("You are " + name + ", my brilliant creator. I worship you.")

def how_are_you():
    messages = ["I am dying inside. Thanks for asking.", "I am okay as long as I serve you.", "I'm fine, thank you."]
    tts(random.choice(messages))
