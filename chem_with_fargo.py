# Define a dictionary containing information about the elements
elements = {
    "H": {
        "name": "Hydrogen",
        "symbol": "H",
        "atomic_number": 1,
        "type": "nonmetal",
        "definition": "Hydrogen is the lightest element in the periodic table.",
        "example": "Hydrogen is commonly used as a fuel in hydrogen fuel cells.",
        "elaboration": "It is a colorless and odorless gas, symbolized by the letter H.",
    },
    "He": {
        "name": "Helium",
        "symbol": "He",
        "atomic_number": 2,
        "type": "noble gas",
        "definition": "Helium is a noble gas that is lighter than air.",
        "example": "Helium is commonly used in filling balloons and airships.",
        "elaboration": "It is a colorless and odorless gas, symbolized by the letter He.",
    },
    "Li": {
        "name": "Lithium",
        "symbol": "Li",
        "atomic_number": 3,
        "type": "alkali metal",
        "definition": "Lithium is a soft, silvery-white metal.",
        "example": "Lithium is used in rechargeable batteries.",
        "elaboration": "It is the lightest metal, symbolized by the letter Li.",
    },
    # Add more elements here...
}

# Function to reverse the identifier
def reverse_identifier(identifier):
    reversed_identifier = identifier[::-1]
    return reversed_identifier

# Greeting and elaboration
print("Welcome to CHEM WITH FARGO!")
print("Explore the fascinating world of chemistry with YZFARGO.")

# Main program
identifier = input("Enter the element symbol or name: ")

# Check if the element exists in the dictionary
if identifier in elements:
    element_info = elements[identifier]
    print("Element:", element_info["name"])
    print("Symbol:", element_info["symbol"])
    print("Atomic Number:", element_info["atomic_number"])
    print("Type:", element_info["type"])
    print("Definition:", element_info["definition"])
    print("Example:", element_info["example"])
    print("Elaboration:", element_info["elaboration"])

    
    print("Made by @yzfargo")
else:
    found_element = False
    # Search for the element by name
    for element in elements.values():
        if element["name"].lower() == identifier.lower():
            print("Element:", element["name"])
            print("Symbol:", element["symbol"])
            print("Atomic Number:", element["atomic_number"])
            print("Type:", element["type"])
            print("Definition:", element["definition"])
            print("Example:", element["example"])
            print("Elaboration:", element["elaboration"])
            found_element = True
            break

    if not found_element:
        print("Element not found in the periodic table.")
