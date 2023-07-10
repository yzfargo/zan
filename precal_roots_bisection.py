def find_root_bisection(function, a, b, tolerance):
    """Finds the root of a function using the bisection method."""
    if function(a) * function(b) >= 0:
        raise ValueError("The function values at the provided bounds must have opposite signs.")
    
    while abs(b - a) > tolerance:
        c = (a + b) / 2
        if function(c) == 0:
            return c
        elif function(a) * function(c) < 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2

# Prompt user for a mathematical expression
expression_str = input("Enter a mathematical expression in terms of 'x': ")
function = lambda x: eval(expression_str)

# Prompt user for the initial bounds of the root
lower_bound = float(input("Enter the lower bound of the root: "))
upper_bound = float(input("Enter the upper bound of the root: "))

# Prompt user for the tolerance
tolerance = float(input("Enter the tolerance for finding the root: "))

# Find the root of the function using the bisection method
root = find_root_bisection(function, lower_bound, upper_bound, tolerance)

# Display the result
print("The root of the function is:")
print(root)
