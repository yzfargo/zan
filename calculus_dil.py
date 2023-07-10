def differentiate(expression, variable):
    """Differentiates a function with respect to the specified variable."""
    h = 1e-6
    numerator = expression.subs(variable, variable + h) - expression.subs(variable, variable)
    denominator = h
    derivative = numerator / denominator
    return derivative

def integrate(expression, variable, lower_bound, upper_bound):
    """Integrates a function with respect to the specified variable over the given bounds."""
    num_intervals = 100
    interval_width = (upper_bound - lower_bound) / num_intervals
    integral = 0
    x = lower_bound
    for _ in range(num_intervals):
        integral += (expression.subs(variable, x) + expression.subs(variable, x + interval_width)) * interval_width / 2
        x += interval_width
    return integral

def calculate_limit(expression, variable, value):
    """Calculates the limit of a function as it approaches a specific value."""
    epsilon = 1e-6
    left_limit = expression.subs(variable, value - epsilon)
    right_limit = expression.subs(variable, value + epsilon)
    return left_limit, right_limit

# Prompt user for a specific calculus problem
problem = input("Enter a calculus problem keyword (differentiation, integration, limits): ")

if problem == 'differentiation':
    expression_str = input("Enter a mathematical expression in terms of 'x': ")
    variable = 'x'
    expression = eval(expression_str)
    derivative = differentiate(expression, variable)
    print("The derivative of the function is:")
    print(derivative)

elif problem == 'integration':
    expression_str = input("Enter a mathematical expression in terms of 'x': ")
    variable = 'x'
    expression = eval(expression_str)
    lower_bound = float(input("Enter the lower bound of integration: "))
    upper_bound = float(input("Enter the upper bound of integration: "))
    integral = integrate(expression, variable, lower_bound, upper_bound)
    print("The integral of the function is:")
    print(integral)

elif problem == 'limits':
    expression_str = input("Enter a mathematical expression in terms of 'x': ")
    variable = 'x'
    expression = eval(expression_str)
    value = float(input("Enter the value the variable is approaching: "))
    left_limit, right_limit = calculate_limit(expression, variable, value)
    print("The left limit of the function as x approaches", value, "is:")
    print(left_limit)
    print("The right limit of the function as x approaches", value, "is:")
    print(right_limit)

else:
    print("Unknown problem. Please provide a valid keyword.")
