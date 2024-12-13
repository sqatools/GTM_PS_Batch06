from datetime import datetime
print(datetime.now().year) # 2024
print(datetime.now().month) # 12
print(datetime.now().day) # 13
print(datetime.now())  # 2024-12-13 21:54:41.155157
var = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
print(var)
