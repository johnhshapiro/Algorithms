import random
import math

def calculate_pi_probabilistically(number_of_darts):
    darts_in_circle = 0

    for i in range(number_of_darts):
        x = random.random() - 0.5
        y = random.random() - 0.5
        if ((x ** 2 + y ** 2) ** (0.5)) <= 0.5:
            darts_in_circle += 1

    approx_pi = 4 * darts_in_circle / number_of_darts
    percent_from_pi = "{:.1}".format(abs(approx_pi - math.pi) / math.pi)
    print(f"Number of Darts: {number_of_darts}\n" +
          f"Calculated pi: {approx_pi}\n" +
          f"Off of Accepted by {percent_from_pi}%\n" +
          "***********************")

calculate_pi_probabilistically(1000)
calculate_pi_probabilistically(10000)
calculate_pi_probabilistically(100000)
calculate_pi_probabilistically(1000000)
calculate_pi_probabilistically(100000000)