"""Calculate integrals with 3 approaches:
    Monte Carlo, Mean Value, Trapezoidal integration.
    Trapezoidal integration is usede as the baseline because it yields the same results every time, and gets more accurate as steps are added.
Results of Monte Carlo and Mean Value are compared to the baseline to guage accuracy and run time of probabilistic methods for integral calculation.
"""

import random
import math
import time

def f(x, fn):
    lookup = {"sin"  : math.sin(x),
              "cos"  : math.cos(x),
              "poly" : 3 * x ** 3 + x ** 2 + 5 * x + 3,
              "e"    : math.e ** x,
              "luke": (math.e ** -x)/(1 + (x - 1) ** 2)}
    return lookup.get(fn)

def find_ymax_and_min(xmin, xmax, fn):
    """This method adapted from
    http://code.activestate.com/recipes/577263-numerical-integration-using-monte-carlo-method/
    Calculates the y max and min based on the function of x.
    This is done because if the upper and lower y bounds aren't the max and min
    of y over the upper and lower x bounds then the function will not return proper
    ratios that can be used to calculate the integral.
    
    Arguments:
        xmin {float} -- lower bound of x
        xmax {float} -- upper bound of x
    
    Returns:
        float -- upper and lower bounds of y
    """
    # find ymin-ymax
    num_steps = 1000000 # bigger the better but slower!
    ymin = f(xmin, fn)
    ymax = ymin
    # calculates y for given x values and finds the max and min
    for i in range(num_steps):
        x = xmin + (xmax - xmin) * float(i) / num_steps
        y = f(x, fn)
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y
    return ymin, ymax


def monte_carlo_approximation(number_of_darts, xmin, xmax, fn):
    """calculate the approximated definite integral from xmin to xmax and check against
    the accepted value of x, which we have lazily asked the user to provide...
    
    Arguments:
        number_of_darts {integer} -- number of darts to throw at the region
        xmin {float} -- lower bound of x
        xmax {float} -- upper bound of x
    """
    # get the y max and min based on x max and y
    ymin, ymax = find_ymax_and_min(xmin, xmax, fn)
    start = time.time()
    darts_under_function = 0
    x_range = xmax - xmin
    y_range = ymax - ymin
    area_of_box = x_range * y_range
    # Let's throw some darts!
    for i in range(number_of_darts):
        # A random point in the box is calculated
        x = x_range * random.random() + xmin
        y = y_range * random.random() + ymin
        # check if the y value is between the function and zero
        if abs(y) <= abs(f(x, fn)):
            # function is above zero, add area
            if f(x, fn) > 0 and y > 0 and y <= f(x, fn):
                darts_under_function += 1
            #function is below zero, subtract area
            if f(x, fn) < 0 and y < 0 and y >= f(x, fn):
                darts_under_function -= 1
    approx_integral = area_of_box * darts_under_function / number_of_darts
    elapsed = time.time() - start
    return approx_integral, elapsed

def mean_values_approximation(number_of_points, xmin, xmax, fn):
    """calculate the approximated definite integral from xmin to xmax and check against
    the accepted value of x, which we have lazily asked the user to provide...
    
    Arguments:
        number_of_points {integer} -- number of points to calculate
        xmin {float} -- lower bound of x
        xmax {float} -- upper bound of x
    """
    start = time.time()
    x_range = xmax - xmin
    total = 0
    # keep a running total of the random y's calculated from x
    for point in range(number_of_points):
        x = x_range * random.random() + xmin
        total += f(x, fn)
    mean = total / number_of_points
    approx_integral = x_range * mean
    elapsed = time.time() - start
    return approx_integral, elapsed

def zoidal_rule_approximation(number_of_zoids, xmin, xmax, fn):
    """Approximation using the trapezoidal rule. As more data points are added
    the accuracy increases in a direct relationship, because there is no
    randomness.
    
    Arguments:
        number_of_zoids {int} -- the number of trapezoids to divide the function into
        xmin {float} -- lower bound of x
        xmax {float} -- lowerbound of x
    """
    start = time.time()
    x_range = xmax - xmin
    # all trapezoids will be this wide
    zoid_width = float(x_range) / number_of_zoids
    a = xmin
    b = a + zoid_width
    total_area = 0
    approx_integral = 0
    # keep a running total of trapezoid area
    for zoid in range(number_of_zoids):
        approx_integral += zoid_width * (f(a, fn) + f(b, fn)) / 2
        a = b
        b += zoid_width
    elapsed = time.time() - start
    return approx_integral, elapsed

def run_tests():
    argument_lists = [[0, math.pi/2, "sin"],
                      [0, math.pi/2, "cos"],
                      [-2, 2, "poly"],
                      [1, 2, "e"],
                      [0, 5, "luke"]]
    data_points = 100
    while data_points <= 100000:
        for list in argument_lists:
            trap_time = trap_integral = 0
            total_time = total_integral = time_off = integral_off = 0
            # Calculate trapezoidal
            for i in range(10):
                integral, time = zoidal_rule_approximation(data_points, list[0], list[1], list[2])
                trap_integral += integral
                trap_time += time
            # Run monte carlo ten times
            for i in range(10):
                integral, time = monte_carlo_approximation(data_points, list[0], list[1], list[2])
                total_integral += integral
                total_time += time
            integral_off = "{:.4%}".format(abs(total_integral - trap_integral)/trap_integral)
            time_off = "{:.1%}".format((total_time - trap_time)/trap_time)
            print(f"Monte Carlo\n" +
                f"{data_points}\n" +
                f"{list[2]}\n" +
                f"{time_off}\n" +
                f"{integral_off}")
            total_time = total_integral = time_off = integral_off = 0
            # Run mean_values ten times
            for i in range(10):
                integral, time = mean_values_approximation(data_points, list[0], list[1], list[2])
                total_integral += integral
                total_time += time
            integral_off = "{:.4%}".format(abs(total_integral - trap_integral)/trap_integral)
            time_off = "{:.1%}".format((total_time - trap_time)/trap_time)
            print(f"Mean Values\n" +
                f"{data_points}\n" +
                f"{list[2]}\n" +
                f"{time_off}\n" +
                f"{integral_off}")
        data_points *= 10


# points = 10000
# print(monte_carlo_approximation(points, 0, math.pi/2, "sin"))
# print(mean_values_approximation(points, 0, math.pi/2, "sin"))
# print(zoidal_rule_approximation(points, 0, math.pi/2, "sin"))
run_tests()