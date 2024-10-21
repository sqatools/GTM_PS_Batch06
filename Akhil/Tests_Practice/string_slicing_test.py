# str_a = "My Name is John"
# output = "ny Name is JohM"
str_a = "My Name is John"
first = str_a[-1]
print(first)
second = str_a[0]
print(second)
third = str_a[1:14]

print(f"result is : {first}{third}{second}")


#Q2. Write a python slicing get below output
str_b = "India is best country"
#output2 = "IIndia iis bbest ccountry"

fist_char = str_b[0]
first_word = str_b[0:6]
second_char = str_b[6]
second_word = str_b[6:9]
third_char = str_b[9]
third_word = str_b[9:14]
fourth_char = str_b[-7]
fourth_word = str_b[-7:]
print(f"result is : {fist_char}{first_word}{second_char}{second_word}{third_char}{third_word}{fourth_char}{fourth_word}")


#Q3. Write a python slicing get below output
str_c = "Sachin is god of cricket"

first = str_c[5]
second = str_c[1:5]
third = str_c[0]

fourth = str_c[-16:-18 :-1]
print(fourth)

fivth = str_c[-12:-15:-1]
print(fivth)

sixth = str_c[-9:-11:-1]
print(sixth)

seventh = str_c[-1]
eight = str_c[-6:-1]
nine = str_c[-7]

print(f"result is : {first}{second}{third} {fourth} {fivth} {sixth} {seventh}{eight}{nine}")
