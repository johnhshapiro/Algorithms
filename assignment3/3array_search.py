"""John Shapiro
3. Array Search
Generate an array of 1000 random elements. Give 5000 random checks to find an item known to be in the array.
If the item is found, record the number of guesses.
Repeat the process 10000 times.
"""

import random

def probabalistic_search(array, guesses):
    search_target = array[random.randrange(0, 1000)]
    comparisons = 0
    while comparisons < guesses:
        comparisons += 1
        if search_target == array[random.randrange(0,1000)]:
            return True, comparisons
    return False, comparisons

def one_hundred_probabalistic_searches(array, guesses):
    target_found = False
    total_comparisons = 0
    not_found_count = 0
    for search in range(10000):
        comparisons = 0
        target_found, comparisons = probabalistic_search(array, guesses)
        total_comparisons += comparisons
        if not target_found:
            not_found_count += 1

    average_number_of_comparisons = total_comparisons / 10000
    print(f"Average number of comparisons to find value: {average_number_of_comparisons}\n" +
          f"Target not found {not_found_count} times\n")
    
NUMBER_OF_ELEMENTS = 1000
NUMBER_OF_GUESSES = 5000

randoms_no_dupes = random.sample(range(NUMBER_OF_ELEMENTS), NUMBER_OF_ELEMENTS)

one_hundred_probabalistic_searches(randoms_no_dupes, NUMBER_OF_GUESSES)