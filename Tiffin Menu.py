# Define the menu of Sravani Tiffin Center
Menu = {
    "Tea": 20,
    "Coffee": 30,
    "Idly": 30,
    "Sambar Idly": 35,
    "Puri": 20,
    "Vada": 30,
    "Mysoor Bonda": 25,
    "Plain Dosa": 30,
    "Onion Dosa": 35,
    "Masala Dosa": 35,
    "Upma Dosa": 45,
    "Plain Pesara": 30,
    "Onion Pesara": 35,
    "Upma Pesara": 35,
}

# Greeting and displaying the menu
print("Welcome to Sravani Tiffin Center")
print("Menu:")
for item, price in Menu.items():
    print(f"{item}: Rs{price}")

Order_Total = 0

# Function to handle item orders
def order_item():
    global Order_Total
    item = input("Enter the name of item you want to order: ").strip()
    if item in Menu:
        Order_Total += Menu[item]
        print(f"Your item '{item}' has been added to your order.")
    else:
        print(f"Sorry, the item '{item}' is not available.")

# Loop to handle multiple orders
while True:
    order_item()
    another_order = input("Do you want to add another item? (Yes/No): ").strip().lower()
    if another_order != "yes":
        break

# Display the total amount
print(f"The total amount to pay is Rs{Order_Total}")
 