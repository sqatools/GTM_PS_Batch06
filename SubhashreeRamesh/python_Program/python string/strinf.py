
for i in range (1, 6):
     if i == 1 or i == 5:
         print(" ", end =" ")
     else:
         print("*", end =" ")

print()
for j in range (5):
    for i in range (1,6):
      if i == 1 or i == 5:
         print("*",end =" ")
      else:
         print(" ",end = " ")

    print()

for i in range (1, 6):
     if i == 1 or i == 5:
         print(" ", end =" ")
     else:
         print("*", end =" ")
print()

print("*"*50)

str3 = "Indian is batsman virat best"

first = str3[-10:-5:1]
second = str3[7:9]
third = str3[-5:]
fourth = str3[0:6]
fifth = str3[10:-11:1]
result = f"{first} {second} {third} {fourth} {fifth}"

print(result)
print("*"*50)
# Write a python slicing to get  below output

# Q1 .
str_a = "My Name is John"
#output1 = "ny Name is JohM"

one = str_a[-1:]
print(one)
two = str_a[1:14]
print(two)
three = str_a[0:-14]
print(three)
output1 = f"{one}{two}{three}"
print(output1)
print("*"*50)
# Q2.
str_b = "India is best country"
#output2 = "IIndia iis bbest ccountry "
aone = str_b[0:-20]
print(aone)
atwo = str_b[0:5]
print(atwo)
bone = str_b[6:7]
print(bone)
btwo = str_b[6:8]
print(btwo)
cone = str_b[9:-11]
print(cone)
ctwo = str_b[9:-8]
print(ctwo)
done = str_b[14:15]
print(done)
dtwo = str_b[14:]
print(dtwo)
output2 = f"{aone}{atwo} {bone}{btwo} {cone}{ctwo} {done}{dtwo}"
print(output2)
print("*"*50)
# Q3.
str_c = "Sachin is god of cricket"
#output3 = "nachiS si dog fo trickec"

onec = str_c[5:6]
print(onec)
twoc = str_c[1:6]
print(twoc)
threec = str_c[0:1]
print(threec)
fourc = str_c[-16:-18:-1]
print(fourc)
fivec = str_c[-11:-16:-1]
print(fivec)
sixc = str_c[-9:-12:-1]
print(sixc)
sevenc = str_c[-1:]
print(sevenc)
eightc = str_c[18:23]
print(eightc)
ninec = str_c[17:-6]
print(ninec)

output3 = f"{onec}{twoc}{threec} {fourc}{fivec}{sixc}{sevenc}{eightc}{ninec}"
print(output3)

print("*"*50)
# q1 : Write a program to replace any specific word without using replace method.
message = "Food Festival is happening in munich"
old_word = "Food"
new_word = "Indian food"
output = ''
word = message.split(" ")
for a in word:
    #print(a)
   if a == old_word:
       output = output + new_word + " "
   else:
       output = output + a + " "
print(output)
print("*"*50)
# q2 : Write a program to get count any specific word/substring without using count method.

Name = "Badhrinarayanandamodaran"
count = 0
find = "a"
for word in Name:
    if word == find:
     count += 1
    else:
     continue
print(f" count of {find}:{count}")

print("*"*50)
# q2 : Write a program to get count each character without using count method.

Name1 = "We are Learning python"
count = 0
for word in Name1:
    if word :
     count += 1
    else:
     continue
print(f" count of {find}:{count}")
