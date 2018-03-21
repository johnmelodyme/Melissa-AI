from GreyMatter import tell_time, goodbye, general_conversations

def brain(name, speech_text):
    def check_message(check):
        words_of_message = speech_text.split() # split speech_text into words and store it in
                                               # words_of_message, which is an array of words
        if set(check).issubset(set(words_of_message)):
            return True
        else:
            return False

    if check_message(["who", "are", "you"]):
        general_conversations.who_are_you()
    elif check_message(["how", "i", "look"]) or check_message(["how", "am", "i"] or check_message(["describe", "me"])):
        general_conversations.describe_me()
    elif check_message(["who", "am", "i"]):
        general_conversations.who_am_i(name)
    elif check_message(["how", "are", "you"]):
        general_conversations.how_are_you()
    elif check_message(["time"]):
        tell_time.what_is_time()
    elif check_message(["say", "goodbye", "melissa"]):
        goodbye.goodbye()
    else:
        general_conversations.undefined()
