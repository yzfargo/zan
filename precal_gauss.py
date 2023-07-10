def solve_system_of_equations_gauss_seidel(coefficients, constants, initial_guess, max_iterations, tolerance):
    """Solves a system of equations using the Gauss-Seidel method."""
    num_equations = len(coefficients)
    num_variables = len(coefficients[0])
    x = initial_guess.copy()
    iteration = 0
    error = [tolerance + 1] * num_equations

    while max(error) > tolerance and iteration < max_iterations:
        for i in range(num_equations):
            x[i] = constants[i]
            for j in range(num_variables):
                if j != i:
                    x[i] -= coefficients[i][j] * x[j]
            x[i] /= coefficients[i][i]
            error[i] = abs(x[i] - initial_guess[i])
            initial_guess[i] = x[i]
        iteration += 1
    
    if iteration == max_iterations:
        print("The method did not converge within the specified number of iterations.")
    
    return x

# Prompt user for the number of equations
num_equations = int(input("Enter the number of equations in the system: "))

# Prompt user for the coefficients of the equations
coefficients = []
for i in range(num_equations):
    equation_coeffs = input(f"Enter the coefficients for equation {i+1} separated by spaces: ").split()
    coefficients.append([float(coeff) for coeff in equation_coeffs])

# Prompt user for the constants of the equations
constants = []
for i in range(num_equations):
    constant = float(input(f"Enter the constant term for equation {i+1}: "))
    constants.append(constant)

# Prompt user for the initial guess
initial_guess = []
for i in range(num_equations):
    guess = float(input(f"Enter the initial guess for variable x{i+1}: "))
    initial_guess.append(guess)

# Prompt user for the maximum number of iterations
max_iterations = int(input("Enter the maximum number of iterations: "))

# Prompt user for the tolerance
tolerance = float(input("Enter the tolerance for convergence: "))

# Solve the system of equations using the Gauss-Seidel method
solution = solve_system_of_equations_gauss_seidel(coefficients, constants, initial_guess, max_iterations, tolerance)

# Display the solution
print("The solution to the system of equations is:")
for i, value in enumerate(solution):
    print(f"x{i+1} = {value}")
