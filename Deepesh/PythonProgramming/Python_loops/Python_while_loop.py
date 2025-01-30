#list2 = [5, 7, 2, 8, 22, 12, 34]
"""
num1 = 0
while num1 < 10:
    print(num1)
    num1 = num1 + 1
"""
"""
# infinite loop with break condition
n1 = 1
while True:
    print(n1)
    n1 += 1
    if n1 == 10000:
        break
#The condition True means the loop will continue
forever unless explicitly interrupted by a break statement. So, it's an infinite loop.
"""

# write a python program to reverse the number without conversion
num = 456789
reverse_val = 0

while num > 0:
    temp = num%10 # 5, 4, 3
    reverse_val = reverse_val*10 + temp # 5 | 5*10 + 4 = 54 | 54*10 + 3 = 543
    num = num//10 # 34 , 3, 0

print("reverse value :", reverse_val)

