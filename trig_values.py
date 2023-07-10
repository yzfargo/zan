import math

def calculate_trig_values(angle):
    """Calculates the sine, cosine, and tangent of an angle in degrees."""
    # Convert the angle from degrees to radians
    angle_rad = math.radians(angle)

    # Calculate the trigonometric values
    sine = math.sin(angle_rad)
    cosine = math.cos(angle_rad)
    tangent = math.tan(angle_rad)

    return sine, cosine, tangent

# Prompt user for an angle in degrees
angle = float(input("Enter an angle in degrees: "))

# Calculate the trigonometric values
sine, cosine, tangent = calculate_trig_values(angle)

# Display the results
print("Sine:", sine)
print("Cosine:", cosine)
print("Tangent:", tangent)
