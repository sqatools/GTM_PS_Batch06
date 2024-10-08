num=345
reverse_val=0
while num>0:
    temp=num%10
    reverse_val=reverse_val*10+temp
    num= num//10
print("Reverse number= ",reverse_val)