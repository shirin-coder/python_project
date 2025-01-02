# Define the Pen class
class Pen:
    def __init__(self, color, brand, ink_type):
        # Initialize instance attributes
        self.color = color
        self.brand = brand
        self.ink_type = ink_type

    # Method to display pen details
    def display_details(self):
        print(f"This is a {self.color} pen from {self.brand} with {self.ink_type} ink.")

# Create three objects of the Pen class with different attributes
pen1 = Pen("blue", "Parker", "gel")
pen2 = Pen("black", "Reynolds", "ballpoint")
pen3 = Pen("red", "Pilot", "fountain")

# Display the details of each pen
pen1.display_details()
pen2.display_details()
pen3.display_details()
