import random

def check_prime_probablistically(number_to_check, number_of_values_to_check):
    number_is_prime = True
    for i in range(number_of_values_to_check):
        if number_to_check % random.randrange(1, number_to_check//2) == 0:
            number_is_prime = False
            print(f"{number_to_check} is not prime")
            break
    if number_is_prime:
        print (f"{number_to_check} is prime")

check_prime_probablistically(20, 1)