"""
STATEMENT OF REQUIREMENTS: coffee.py
1. Functional Requirements:
   - Starting Balance: The system begins with a fixed cost of 75p.
   - Input Acceptance: The system only accepts integers: 50, 20, 10, and 5.
   - Balance Update: Valid inputs decrement the total due.
   - Output: Upon reaching a balance of <= 0, the system must output the 
     absolute value of the remaining balance as "Change Owed".

2. Non-Functional Requirements (Reliability):
   - Data Integrity: If a user enters non-integer data (strings, symbols), 
     the system must catch the error, display "Invalid Input," and 
     continue the loop without crashing.
"""
Price = 75
accepted_coins = [50, 20, 10, 5]

print("Welcome! The price of a coffee is 75p.")

while Price > 0:
    print(f"Price: {Price}p")
    
    # Prompt user for input
    coin = int(input("Insert Coin (50, 20, 10, 5): "))

    # Validate the denomination
    if coin in accepted_coins:
        Price -= coin
    else:
        print(f"Sorry, the machine does not accept {coin}p coins.")

print("-" * 20)
print("Thank you! Dispensing coffee...")

change_owed = abs(Price)
print(f"Change Owed: {change_owed}p")
