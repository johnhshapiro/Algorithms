import random
import math
import time

def f(x, fn):
    lookup = {"sin"  : math.sin(x),
              "cos"  : math.cos(x),
              "poly" : 3 * x ** 3 + x ** 2 + 5 * x + 3,
              "e"    : math.e ** x,
              "thing": (math.e ** -x)/(1 + (x - 1) ** 2)}
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
    start = time.time()
    darts_under_function = 0
    x_range = xmax - xmin
    # get the y max and min based on x max and y
    ymin, ymax = find_ymax_and_min(xmin, xmax, fn)
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
    argument_lists = [[data_points, 0, math.pi/2, "sin"],
                      [data_points, 0, math.pi/2, "cos"],
                      [data_points, -2, 2, "poly"],
                      [data_points, 1, 2, "e"]]
    total_time = 0
    total_integral = 0
    trap_time, trap_integral = 0, 0
    for list in argument_lists:    
        trap_integral, trap_time = zoidal_rule_approximation(list[0], list[1], list[2], list[3])    
        for i in range(10):
            integral, time = monte_carlo_approximation(list[0], list[1], list[2], list[3])
            total_integral += integral
            total_time += time
        integral = total_integral/10
        time = total_time/10

data_points = 10000

print(monte_carlo_approximation(data_points, 0, 5, "thing"))
# monte_carlo_approximation(data_points, 0, math.pi/2, "cos")
# monte_carlo_approximation(data_points, -2, 2, "poly")
# monte_carlo_approximation(data_points, 1, 2, "e")
# mean_values_approximation(data_points, 0, math.pi/2, "sin")
# zoidal_rule_approximation(data_points, 0, math.pi/2, "sin")
# run_tests()