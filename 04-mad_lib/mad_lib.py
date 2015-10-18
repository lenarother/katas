def get_user_words():
    noun = input("Please enter a noun > ")
    verb = input("Please enter a verb > ")
    adjective = input("Pleas enter an adjective > ")
    adverb = input("Please enter an adverb > ")
    return noun, verb, adjective, adverb


def get_story(noun, verb, adjective, adverb):
    return 'Once upon a time a small girl was runing {} through a forest, when suddenly she saw a {} {} and started to {}'.format(adverb, adjective, noun, verb)


if __name__=='__main__':
    noun, verb, adjective, adverb = get_user_words()
    print(get_story(noun, verb, adjective, adverb))

