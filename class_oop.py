class Calculator:
    # No __init__ method here

    def take_numbers(self):
        self.num1 = float(input("Enter the first number: "))
        self.num2 = float(input("Enter the second number: "))

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2


# Main function to use the calculator
def main():
    calc = Calculator()
    calc.take_numbers()

    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        print("Result:", calc.add())
    elif choice == 2:
        print("Result:", calc.subtract())
    elif choice == 3:
        print("Result:", calc.multiply())
    else:
        print("Invalid choice. Please try again.")


# Run the program directly
main()
