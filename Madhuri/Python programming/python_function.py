"""
def<function_name>:
code
"""
"""
def greeting():
    print("Good morning")
greeting()
"""
"""
def greeting_msg(msg):
    print(msg)
greeting_msg("good morning")
greeting_msg("How are you?")
"""
# import specificfunction in this module
#greeting_msg("have a nice day")
#greeting()
def addition(num1,num2):
    print("add vales:",num1+num2)
# pass the values by 2 ways
# 1.pass by value
addition(50,70)
#2. pass by reference
X = 400
y = 600
addition(X,y)
#3
list1 =[3,6,8,2]
list2 = [10,20,30,40]
for i in range (len(list1)):
 addition (list1[i],list2[i])

# function with default parameter  value--
def mulitiplication(num1,num2):
    print(f"multiple values {num1},{num2},{num1*num2}")

"""
# if we cal function without passing value of default parameter
then it will consider default value only
# if we cal function and pass value to the default parameter,then defaultvalue will be overwritten by new value
# we can interchange the parmeter value position with the of parmetername only
# default parmeter always fallow the non default parameter,it means default parmeter always come at the endor roght most side
wrong:def fun(var1 =40,var2)
right:def fun1(var1,var2=50)
# all parameters can have defalut value
def fun(v1 =40,v2 = 50,v3 = 60)
"""