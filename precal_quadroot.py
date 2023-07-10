import cmath

def calculate_quadratic_roots(a, b, c):
    """Calculates the roots of a quadratic equation."""
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    return root1, root2

# Prompt user for the coefficients of the quadratic equation
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the roots of the quadratic equation
root1, root2 = calculate_quadratic_roots(a, b, c)

# Display the roots
print("The roots of the quadratic equation:")
print(f"Root 1: {root1}")
print(f"Root 2: {root2}")
