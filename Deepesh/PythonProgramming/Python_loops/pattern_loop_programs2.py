"""
Write a program to accept the kilometers covered and calculate the bill according to the following using Python Loops.
First 5 km- 15rs/km
Next 20 km- 12rs/km
After that- 10rs/km

Solution
"""
num_of_km = 55
total_amount = 0
a = b = c = 0
for i in range(1, num_of_km+1):
    if i <= 5:
        a += 1
    elif i >5 and i<=25:

        b += 1

    elif i>25:
        c +=1

print(a, b, c)
total_amount = a*15 + b*12 + c*10
print("Total bill :", total_amount)
