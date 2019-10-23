import random
import math

def f(x):
    """A dictionary of different functions from which to calculate integrals
    
    Arguments:
        x {float} -- y is calculated based on the given x
    
    Returns:
        [float] -- the calculated y value
    """
    return math.sin(x)

def find_ymax_and_min(xmin, xmax):
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
    ymin = f(xmin)
    ymax = ymin
    # calculates y for given x values and finds the max and min
    for i in range(num_steps):
        x = xmin + (xmax - xmin) * float(i) / num_steps
        y = f(x)
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y
    return ymin, ymax


def monte_carlo_dart_integral(number_of_darts, xmin, xmax):
    """calculate the approximated definite integral from xmin to xmax and check against
    the accepted value of x, which we have lazily asked the user to provide...
    
    Arguments:
        number_of_darts {integer} -- number of darts to throw at the region
        xmin {float} -- lower bound of x
        xmax {float} -- upper bound of x
    """
    darts_under_function = 0
    x_range = xmax - xmin
    # get the y max and min based on x max and y
    ymin, ymax = find_ymax_and_min(xmin, xmax)
    y_range = ymax - ymin
    area_of_box = x_range * y_range
    # Let's throw some darts!
    for i in range(number_of_darts):
        # A random point in the box is calculated
        x = x_range * random.random() + xmin
        y = y_range * random.random() + ymin
        # check if the y value is between the function and zero
        if abs(y) <= abs(f(x)):
            # function is above zero, add area
            if f(x) > 0 and y > 0 and y <= f(x):
                darts_under_function += 1
            #function is below zero, subtract area
            if f(x) < 0 and y < 0 and y >= f(x):
                darts_under_function -= 1
    approx_integral = "{:.4f}".format(area_of_box * darts_under_function / number_of_darts)

    print(approx_integral)

def mean_values_integral(number_of_points, xmin, xmax):
    """calculate the approximated definite integral from xmin to xmax and check against
    the accepted value of x, which we have lazily asked the user to provide...
    
    Arguments:
        number_of_points {integer} -- number of points to calculate
        xmin {float} -- lower bound of x
        xmax {float} -- upper bound of x
    """
    x_range = xmax - xmin
    total = 0
    # keep a running total of the random y's calculated from x
    for point in range(number_of_points):
        x = x_range * random.random() + xmin
        total += f(x)
    mean = total / number_of_points
    approx_integral = "{:.4f}".format(x_range * mean)

    print(approx_integral)

def trapezoidal_rule_approximation(number_of_zoids, xmin, xmax):
    x_range = xmax - xmin
    # all trapezoids will be this wide
    zoid_width = float(x_range) / number_of_zoids
    a = xmin
    b = a + zoid_width
    total_area = 0
    approx_integral = 0
    # keep a running total of trapezoid area
    for zoid in range(number_of_zoids):
        approx_integral += zoid_width * (f(a) + f(b)) / 2
        a = b
        b += zoid_width
    print("{:.4f}".format(approx_integral))

DATA_POINTS = 100000

monte_carlo_dart_integral(DATA_POINTS, -math.pi/2, math.pi/2)
mean_values_integral(DATA_POINTS, -math.pi/2, math.pi/2)
trapezoidal_rule_approximation(DATA_POINTS, -math.pi/2, math.pi/2)