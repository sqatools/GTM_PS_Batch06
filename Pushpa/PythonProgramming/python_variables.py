a = 10
print(a)

# id() function return the memory address of any variable
# if two variables holding same value, then the memory address will be same.
print(id(a)) # 140716298865368


# assign one value to three different  variable

p = q = r = 50

print("value of p :", p, id(p))
print("value of q :", q, id(q))
print("value of r :", r, id(r))


# assign three different variables to three different values
print("_"*50) # this is to draw lines
x, y, z = 30, 40, 50

print("value of x :", x, id(x))
print("value of y :", y, id(y))
print("value of z :", z, id(z))

# Rules to define a variable
# Rule 1. There should not be space a variable

# Rule 2. Special characters are not in the variable name

# Rule 3. Can not contain number as prefix in the variable name

# Rule 4. Variable names are case-sensitive




