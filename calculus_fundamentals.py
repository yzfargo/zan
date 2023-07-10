import math

def differentiate(f, x, h=1e-6):
    """Approximates the derivative of a function at a point using the difference quotient."""
    numerator = f(x + h) - f(x)
    denominator = h
    derivative = numerator / denominator
    return derivative

def integrate(f, a, b, n=100):
    """Approximates the definite integral of a function over an interval using the trapezoidal rule."""
    interval_width = (b - a) / n
    integral = 0
    x = a
    for _ in range(n):
        integral += (f(x) + f(x + interval_width)) * interval_width / 2
        x += interval_width
    return integral

# Prompt user for a mathematical expression
expression_str = input("Enter a mathematical expression in terms of 'x': ")

# Define the function f(x)
def f(x):
    return eval(expression_str)

# Prompt user for the operation
operation = input("Enter 'd' for differentiation or 'i' for integration: ")

if operation == 'd':
    # Prompt user for the point at which to differentiate
    x_value = float(input("Enter the point at which to differentiate: "))

    # Calculate the derivative of f(x)
    derivative = differentiate(f, x_value)

    # Display the result
    print("The derivative at x =", x_value, "is:", derivative)

elif operation == 'i':
    # Prompt user for the interval for integration
    lower_bound = float(input("Enter the lower bound of integration: "))
    upper_bound = float(input("Enter the upper bound of integration: "))

    # Calculate the definite integral of f(x)
    integral = integrate(f, lower_bound, upper_bound)

    # Display the result
    print("The definite integral over [", lower_bound, ",", upper_bound, "] is:", integral)

else:
    print("Invalid operation. Please choose 'd' for differentiation or 'i' for integration.")
