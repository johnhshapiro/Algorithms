import random

def generate_test_values():
    """Generates a list of large numbers we know are not prime,
    based on assignment suggestions
    
    Returns:
        list -- numbers we know are not prime
    """
    test_values = []
    # generate even numbers
    for i in range(10):
        test_values.append(2 * random.randrange(100000, 1000000))
    # generate multiples of 5
    for i in range(10):
        test_values.append(5 * random.randrange(100000, 1000000))
    # generate multiples of 3
    for i in range(10):
        test_values.append(3 * random.randrange(100000, 1000000))
    # generate numbers constructed of by product of two positive ints
    for i in range(10):
        test_values.append(random.randrange(1000, 10000) * random.randrange(1000, 10000))
    # generate numbers we know to be not prime with various divisors
    for i in range(60):
        x = random.randrange(1000000, 1100000)
        k = random.randrange(2, 100)
        test_values.append(x - x % k)

    return test_values

def check_prime_probablistically(number_to_check, number_of_values_to_check):
    """check if a number is prime by guessing some number of possible divisors
    
    Arguments:
        number_to_check {int} -- Check if this number is prime
        number_of_values_to_check {int} -- number of possible divisors to check
    
    Returns:
        boolean -- The guess whether a number is prime or not based on values checked
    """
    for i in range(number_of_values_to_check):
        if number_to_check % random.randrange(2, number_to_check // 2) == 0:
            return False
    return True

def check_prime(number_to_check):
    """This checks whether a number is prime (not guessing)
    
    Arguments:
        number_to_check {int} -- Check if this number is prime
    
    Returns:
        boolean -- Prime or not
    """
    if number_to_check > 1:
        for i in range(2, number_to_check // 2):
            if (number_to_check % i) == 0:
                return False
        return True
    return False

def run_tests(test_values):
    """Does 100 tests each for 10, 100, 1000, 10000 guesses and prints the average
    ratio of times that the probabilistic algorithm guessed right at each level
    
    Arguments:
        test_values {list} -- A list of numbers known to be prime, generated using
        the generate_test_values function
    """
    total_correct = 0
    number_of_guesses = 10
    while number_of_guesses <= 10000:
        total_correct = 0
        for i in range(100):
            for test_value in test_values:
                if check_prime_probablistically(test_value, number_of_guesses) == check_prime(test_value):
                    total_correct += 1
        print("{:.4f}".format(total_correct/10000))
        number_of_guesses *= 10
    
test_values = generate_test_values()
run_tests(test_values)