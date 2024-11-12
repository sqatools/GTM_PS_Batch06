"""
There are three mode of the file to access
1. Read mode (r):
2. Write mode (w) :
3. Append mode (a) :
"""

def read_file(filepath):
    file = open(filepath, "r")
    data = file.read()
    print(data)
    file.close()

# read file from current location
# read_file("read_data.txt")

# read file from specific path
# read_file("E:\\Filesdata\\count_name.txt")


########### Open file in write mode ###################
def write_to_file(filepath, content):
    file = open(filepath, "w")
    file.write(content)
    file.close()

# 1. File does not exist : It will create a new with specified name
#    and add content to the file
# write_to_file("write_data.txt", "India Lost Second t20 Match with south Africa")


# 2. Existing file : Write method will overwrite the existing content of the file
# write_to_file("write_old_file.txt", "India Lost Second t20 Match with south Africa")


######### Append content to the file ###########
print("_"*50)
def append_content_to_file(filepath, content):
    # open file in append mode
    file = open(filepath, "a")
    file.write(content)
    file.close()

#1. File does not exist : Append mode also create new file, if file does not exist.
append_content_to_file("append_data.txt", "India will win third T20")

#2. Existing File : Append mode update new content to existing file at end of file.
append_content_to_file("append_existing_data.txt", "\nToday we are celebrating Diwali in India")
