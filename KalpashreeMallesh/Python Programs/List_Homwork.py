# Problem to print the sum of all elements in a list

list1 = [1, 3, 5]
result = 0

for val in list1:
    result += val

print(result)

# Problem to get the square of all numbers In the python list

list1= [2, 4, 5]

for val in list1:
    print(val, ":", val**2)

# Program to print squares of even numbers from a list

list1 = [2, 4, 5, 10, 3]
new_list = []

for val in list1:
    if val % 2 == 0:
        new_list.append(val**2)
        print(val, ":", val ** 2)
        # 2 : 4
        # 4 : 16
        # 10 : 100

print("Square of even numbers are: ", new_list) # Square of even numbers are:  [4, 16, 100]

# Program to split the list into two-part

list1 = [1, 10, 5, 4, 8, 2, 5]
even = []
odd = []

for val in list1:
    if val % 2 == 0:
        even.append(val)
    else:
        odd.append(val)

# print(even) # [10, 4, 8, 2]
# print(odd) # [1, 5, 5]

odd.extend(even)
print(odd) # [1, 5, 5, 10, 4, 8, 2]

# Program to print list in reverse order using index slicing.

list1 = [2, 4, 6, 8]

list2 = list1[::-1]

print(list2) # [8, 6, 4, 2]


# Program to print the list in reverse order using while loop

list1 = [10, 5, 1, 4, 8]
count = len(list1)-1

while count >= 0:
    print(list1[count], end=" ") # 8 4 1 5 10
    count -= 1


# Program to reverse a list with reversed and reverse methods

############## Using reversed() ###############

list1 = [1, 5, 4, 2, 8]

print("Using reversed method:", list(reversed(list1))) # Using reversed method: [8, 2, 4, 5, 1]

############## Using reverse() ###############

list2 = [10, 18, 5, 4, 6]

list2.reverse()
print("Using reverse:", list2) # Using reverse: [6, 4, 5, 18, 10]


# Program to print the list in reverse order using for loop

list1 = [1, 8, 5, 4, 2]

print("Reverse values are:", list1[::-1]) # Reverse values are: [2, 4, 5, 8, 1]

##########Using Loop###########

list2 = [1, 10, 18, 5, 4]

for val in range(len(list1)-1,-1,-1):
    print(list2[val], end=" ") # 4 5 18 10 1
    

# Problem to get product of all elements in a list

list1 = [1, 3, 2, 5]
result = 1
for val in list1:
    result *= val

print(result)


# Problem to find minimum and maximum elements from a list

list1 = [2, 10, 25, 18, 5]

list1.sort()

print("Smallest number is: ", list1[0])
print("Largest number is: ", list1[-1])


# Program to differentiate even and odd elements from a list

list1 = [1, 3, 4, 5, 8, 10]

for val in list1:
    if val % 2 == 0:
        print(f"{val} is a even number")
    else:
        print(f"{val} is a odd number")

# 1 is a odd number
# 3 is a odd number
# 4 is a even number
# 5 is a odd number
# 8 is a even number
# 10 is a even number


# Program to get a list of elements divided by a number

list1 = [4, 21, 2, 25, 16, 38, 14]
new_list = []

for val in list1:
    if val%2 == 0:
        new_list.append(val)


# Problem to add elements from list1 to list2

list1 = [1, 3, 5]
list2 = [2, 4, 6]

output = list1 + list2

print(output)
