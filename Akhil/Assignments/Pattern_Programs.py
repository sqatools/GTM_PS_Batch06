# T pattern
'''
*****
  *
  *
  *
  *
  *
  *
'''

for row in range(1, 8):
    for column in range(1, 6):
        if row == 1:
            print("*", end="")

        elif 1 < row < 8 and column != 3:
            print(" ", end="")

        elif 1 < row < 8 and column == 3:
            print("*", end="")
    print()
print("#" * 50)
# l pattern
'''
  *
  *
  *
  *
  *
  *
  *
'''

for row in range(1, 8):
    for column in range(1, 6):
        if 0 < row < 8 and column == 3:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("#" * 50)
# I pattern
'''
*****
  *
  *
  *
  *
  *
***** 
'''

for row in range(1, 8):
    for column in range(1, 6):
        if row == 1 or row == 7:
            print("*", end="")
        elif 1 < row < 7 and column == 3:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 0 pattern
'''
  * * *  
*       *
*       *
*       *
*       *
*       *
  * * *  
'''
print("#" * 50)
for row in range(1, 8):
    for column in range(1, 6):
        if (row == 1 or row == 7) and (1 < column < 5):
            print("*", end="")
        elif (row == 1 and column == 1) or (row == 1 and column == 5):
            print(" ", end="")
        elif (row == 7 and column == 1) or (row == 7 and column == 5):
            print(" ", end="")
        elif (1 < row < 8 and (column == 1 or column == 5)):
            print("*", end="")
        else:
            print(" ", end="")

    print()

# L pattern
'''
*
*
*       
*       
*       
*       
* * * * * 

'''

for row in range(1, 8):
    for column in range(1, 6):
        if column == 1 or (row == 7 and 1 < column < 6):
            print("*", end=" ")
        else:
            print(" ", end="")
    print()

print("#" * 50)



'''
 ***
*   *
*   *
*****   
*   *
*   *
*   *
'''



for row in range(1,8):
    for column in range(1,6):
        if (column == 1 or column == 5) and row != 1:
            print("*", end = "")
        elif row ==1 and 1 < column < 5:
            print("*", end = "")
        elif row == 4 and 1 < column <5:
            print("*", end= "")
        else:
            print(" ", end ="")
    print()


print("#" * 50)
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
'''
2). Write a small application of Fruit shop with the help of list

 -> create a list which contains fruit name, price, stocks
fruit_list = [['Apple', 50, 100], ['Mango', 40, 200], ['Banana', 3, 300]]

 -> do purchase from given list
 purchase_list = [['Apple', 10], ['Mango', 5, 200], ['Banana', 20]]

 -> Calculate total bill

 -> update the fruit list as per purchase
 fruit_list = [['Apple', 50, 90], ['Mango', 40, 195], ['Banana', 3, 280]]
'''

fruit_list = [['Apple', 50, 100], ['Mango', 40, 200], ['Banana', 3, 300]]
purchase_list = [['Apple', 10], ['Mango', 5, 200], ['Banana', 20]]
total_bill = 0

for purchase in purchase_list:
    fruit_name = purchase[0]
    fruit_quantity = purchase[1]

    for fruit in fruit_list:
        if fruit[0] == fruit_name:
            price_per_unit = fruit[1]
            stock = fruit[2]

            if stock >= fruit_quantity:
                total_bill = total_bill + (fruit_quantity * price_per_unit)
                fruit[2] = fruit[2] - fruit_quantity

print(f"Total Bill: {total_bill}")
for fruit in fruit_list:
    print(f"{fruit[0]}: Price = {fruit[1]}, Stock = {fruit[2]}")
print(fruit_list)








