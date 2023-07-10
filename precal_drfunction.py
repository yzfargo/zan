def find_domain_range(function):
    """Finds the domain and range of a function."""
    domain = "All real numbers"
    range_values = set()

    # Evaluate the function for a range of input values
    for x in range(-10, 11):
        try:
            y = eval(function)
            range_values.add(y)
        except (SyntaxError, NameError):
            pass

    range_str = ", ".join(str(value) for value in sorted(range_values))

    return domain, range_str

# Prompt user for the function
function = input("Enter the function: ")

# Find the domain and range of the function
domain, range_str = find_domain_range(function)

# Display the results
print("Domain:", domain)
print("Range:", range_str)
