def calculate_slope(x1, y1, x2, y2):
    """Calculates the slope of a line given two points."""
    slope = (y2 - y1) / (x2 - x1)
    return slope

# Prompt user for the coordinates of two points
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

# Calculate the slope of the line
slope = calculate_slope(x1, y1, x2, y2)

# Display the result
print(f"The slope of the line passing through ({x1}, {y1}) and ({x2}, {y2}) is: {slope}")
