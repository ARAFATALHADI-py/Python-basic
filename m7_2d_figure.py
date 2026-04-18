import math
# --- 1. Define Calculation Functions ---
def calculate_square_area(side):
    return side * side

def calculate_square_perimeter(side):
    return 4 * side

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_triangle_perimeter(s1, s2, s3):
    return s1 + s2 + s3

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_circle_circumference(radius):
    return 2 * math.pi * radius

# --- 2. Define the Menu Function ---
def display_menu():
    while True:
        # Step 8 & 9: Logic for Square, Triangle, and Circle
        choice = input("Enter your choice (1/2/3/0): ")

        if choice == "1":
            side = float(input("Enter the length of a side: "))
            square_area = calculate_square_area(side)
            square_perimeter = calculate_square_perimeter(side)
            print("Square area:", square_area)
            print("Square perimeter:", square_perimeter)

        elif choice == "2":
            base = float(input("Enter the length of the base: "))
            height = float(input("Enter the height: "))
            triangle_area = calculate_triangle_area(base, height)
            side1 = float(input("Enter the length of side 1: "))
            side2 = float(input("Enter the length of side 2: "))
            side3 = float(input("Enter the length of side 3: "))
            triangle_perimeter = calculate_triangle_perimeter(side1, side2, side3)
            print("Triangle area:", triangle_area)
            print("Triangle perimeter:", triangle_perimeter)

        elif choice == "3":
            radius = float(input("Enter the radius: "))
            circle_area = calculate_circle_area(radius)
            circle_circumference = calculate_circle_circumference(radius)
            print("Circle area:", circle_area)
            print("Circle circumference:", circle_circumference)

        # Step 10: Exit and Invalid Choice logic
        elif choice == "0":
            print("Thank you for using this program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

        print() # Add an empty line to separate output (Step 10)

# --- 3. Main Program Execution (Step 11) ---
print("=== 2D Figure Calculators ===")
display_menu()