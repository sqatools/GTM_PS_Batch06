"""
 Write a small application of Fruit shop with the help of list

 -> create a list which contains fruit name, price, stocks
fruit_list = [['Apple', 50, 100], ['Mango', 40, 200], ['Banana', 3, 300]]

 -> do purchase from given list
 purchase_list = [['Apple', 10], ['Mango', 5, 200], ['Banana', 20]]

 -> Calculate total bill

 -> update the fruit list as per purchase
 ruit_list = [['Apple', 50, 90], ['Mango', 40, 195], ['Banana', 3, 280]]

"""
"""
fruit_list = [['Apple', 50, 100], ['Mango', 40, 200], ['Banana', 3, 300]]

purchase_list = [['Apple', 10], ['Mango', 5], ['Banana', 20]]

total_bill = 0

for purchase in purchase_list:
    fruit_name = purchase[0]
    quantity = purchase[1]

    for fruit in fruit_list:
        if fruit[0] == fruit_name:
            if fruit[2] >= quantity:
                total_bill += fruit[1] * quantity
                fruit[2] -= quantity
            else:
                print("Not enough stock for", fruit_name)
            break

print("Total Bill:", total_bill)
print("Updated Fruit List:", fruit_list)
"""
#d). L Pattern
"""
for row in range(7):
    for col in range(7):
        if col == 0 or row == 6:
            print("*", end=" ")
    print()
    """

"""
#I Pattern
for row in range(7):
    for col in range(7):
        if row == 0 or row == 6 or col == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
"""
#T Pattern

for row in range(7):
    for col in range(7):
        if row == 0 or col == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#O Pattern



