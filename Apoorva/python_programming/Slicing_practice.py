
str3 = "Indian is batsman virat best"
first = str3[-10:-5:1]
second = str3[10:1]
third = str3[-4:-1]
fourth = str3[0:6]
fifth = str3[10:17]
Result = f"{first} {second} {third} {fourth} {fifth}"
print(Result)


#1.
# str_a = "My name is John"
# o/p = "ny name is JohM"

str_a = "My name is John"
print(str_a[-1]+str_a[1:-1]+str_a[0])


#2.
str_b = "India is best country"
# o/p = "IIndia iis bbest ccountry"

print(str_b[0]+str_b[0:6]+str_b[6]+str_b[6:9]+str_b[9]+str_b[9:14]+str_b[14]+str_b[14:21])

#3.

str_c = "Sachin is god of cricket"
# o/p = "nachiS si dog fo trickec"

print(str_c[5]+str_c[1:5]+str_c[0]+str_c[6]+str_c[8]+str_c[7]+str_c[6]+str_c[12]+str_c[11]+str_c[10]+str_c[6]+str_c[-9]+str_c[-10]+str_c[6]+str_c[-1]+str_c[-6:-1]+str_c[-7])
