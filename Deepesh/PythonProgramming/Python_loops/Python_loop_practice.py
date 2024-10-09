# range(initial value, end value, different value)
# -> when we iterate values of range then the last value is always going to skip
# -> range function accept three parameter initial value, last value and different
# -> if we call range with one single value, then it will consider as end value, for initial
# and different it will consider zero and 1 respectively.

for var1 in range(1, 10, 1):
    print(var1)

"""
1
2
3
4
5
6
7
8
9
"""
print("_" * 50)
# print output in one line then provide custom value to end parameter
for var1 in range(1, 10, 1):
    print(var1, end=" ")

# 1 2 3 4 5 6 7 8 9


print("_" * 50)
###########################
# consider default initial value and end value in the range function
# default initial value =0 and difference value is 1

# default initial value will be o and difference is 1
for i in range(5):
    print(i, end=' ')

# 0 1 2 3 4

print()
print("_" * 50)
##################
# print numbers in reverse order
for i in range(10, 0, -1):
    print(i, end=" ")

print()
print("_" * 50)
###########################################
# write a python program to print all the even numbers from 1 to 20

for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=' ')
    else:
        pass

# 2 4 6 8 10 12 14 16 18 20

print()
for j in range(2, 21, 2):
    print(j, end=" ")

print()
print("_" * 50)
# write a python program to find out the given number is prime or not

num = 31
prime = True
for i in range(2, num):
    if num % i == 0:
        print("i :",i)
        prime = False
    else:
        pass

result = "prime" if prime else "not prime"
print(result , ":", num)
# if prime:
#     print("This is prime number :", num)
# else:
#     print("This is not prime number :", num)
#


###################################################
print("_"*50)
# write a python program to find the factorial of given number
# factorials 5 = 5*4*3*2*1 = 120

num1 = 5
fact = 1
for i in range(num1, 0, -1):
    fact = fact*i
    print("fact :",i, ":", fact)

print("factorials of num :", fact)

print("_"*50)
##################################################
# continue and break statement
# continue : continue statement does not execute the further code if condition is met.
#            and move the loop to next iteration.

for i in range(1, 11):
    if i == 6:
        continue
    print("value if i :", i)


print("_"*50)
# write a python program to print the number which is divisible by 5 except divisible by 2

for j in range(50):
    if j%5 == 0:
        if j%2 == 0 and j%3 == 0:
            continue
        print(j)



print("_"*50)
############## break statement ############
# break : break statement stop the execution any loop condition if break condition is met

for i in range(1, 11):
    if i == 6:
        break
    print("value if i :", i)

print("_"*50)
#####
# write a python program to find the prime number
num = 91
prime = True
for i in range(2, num//2):
    print(i)
    if num%2 == 0:
        prime = False
        break

if prime:
    print("This is prime no :", num)
else:
    print("This is not prime no :", num)

print("_"*50)
############################################################
# write a python program to calculate total number of odd or
# even numbers in given list of values

tup_val = (5, 7, 9, 11, 4, 3, 1, 17, 8, 14)
odd_count = 0
even_count = 0

for val in tup_val:
    if val%2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("odd count", odd_count)
print("even count :", even_count)


print("_"*50)
# get tuple value with index position

odd_cnt = 0
even_cnt = 0
tup_length = len(tup_val)
print("tuple length :", tup_length)
for i in range(tup_length):
    print(i, tup_val[i])
    if tup_val[i]%2 == 0:
        even_cnt = even_cnt + 1
    else:
        odd_cnt = odd_cnt + 1

print("Odd count :", odd_cnt)
print("Even count :", even_cnt)


"""
# apply loop on list data
print("_"*50)
list1 = [5, 7, 2, 8, 12, 67, 1, 7]

for val in list1:
    print(val)

# apply loop on set data
print("_"*50)
list2 = {4, 7, 9, 1}

for val in list2:
    print(val)


print("_"*50)
str1 = "Hello Python"
for char in str1:
    print(char, end=" ")
# H e l l o   P y t h o n 
"""


# 6). Write a program to get the Fibonacci series between 0 to 20 using python.
# Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181

a = 0
b = 1
for _ in range(20):
    print(a, end= " ")
    a, b = b, a+b


# p, q, r = 40, 50, 60
