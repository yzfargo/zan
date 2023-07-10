import math

def classify_triangle(a, b, c):
    """Classifies the type of triangle based on its side lengths."""
    if a == b == c:
        return "Equilateral Triangle"
    elif a == b or b == c or c == a:
        if a is not None and b is not None and c is not None:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                return "Isosceles Right Triangle"
            else:
                return "Isosceles Triangle"
        else:
            return "Isosceles Triangle"
    else:
        if a is not None and b is not None and c is not None:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                return "Scalene Right Triangle"
            else:
                return "Scalene Triangle"
        else:
            return "Scalene Triangle"

def find_missing_sides(a, b, c):
    """Finds the missing side lengths of a triangle given the known side lengths."""
    missing_sides = []
    if a is None and b is not None and c is not None:
        missing_sides.append(math.sqrt(c**2 - b**2))
    if b is None and a is not None and c is not None:
        missing_sides.append(math.sqrt(c**2 - a**2))
    if c is None and a is not None and b is not None:
        missing_sides.append(math.sqrt(a**2 + b**2))
    return missing_sides

# Prompt user for the classification of the triangle
triangle_type = input("Enter the classification of the triangle: ")

# Prompt user for the known side lengths
side_a = input("Enter the length of side a (or leave blank if unknown): ")
side_b = input("Enter the length of side b (or leave blank if unknown): ")
side_c = input("Enter the length of side c (or leave blank if unknown): ")

# Convert side lengths to floats or None if not provided
side_a = float(side_a) if side_a else None
side_b = float(side_b) if side_b else None
side_c = float(side_c) if side_c else None

# Classify the type of triangle
classification = classify_triangle(side_a, side_b, side_c)

# Calculate the missing sides
missing_sides = find_missing_sides(side_a, side_b, side_c)

# Display the classification, missing sides, and known side lengths
print("Triangle Classification:", classification)
print("Missing Sides:", missing_sides)
print("Known Side Lengths:")
print("Side a:", side_a)
print("Side b:", side_b)
print("Side c:", side_c)
