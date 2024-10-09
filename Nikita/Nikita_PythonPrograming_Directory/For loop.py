
"""num = 13
prime = True
for i in range(2, num):
       if num % i == 0:
           print("i :", i)
           prime = False
       else:
           pass
if prime:
    print("This is prime number :", num)
else:
    print("This is not prime number :", num)"""

"""for i in range(1,11):
    if i==6:
        break
    print(i)"""

tup_val = (5, 7, 9, 11, 4, 3, 1, 17, 8, 14)
odd_count = 0
even_count = 0

for val in tup_val:
    if val % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("odd count", odd_count)
print("even count :", even_count)


