import random

NUMBER_OF_ELEMENTS = 1000
NUMBER_OF_GUESSES = 5000

randoms_no_dupes = random.sample(range(NUMBER_OF_ELEMENTS), NUMBER_OF_ELEMENTS)

def probabalistic_search(array_to_search, number_of_guesses):
    index = random.randrange(0, 1000)
    search_target = array_to_search[index]
    for guess in range(number_of_guesses):
        if search_target == array_to_search[random.randrange(0,1000)]:
            return True
        return False