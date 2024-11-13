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
#append_content_to_file("append_data.txt", "India will win third T20")

#2. Existing File : Append mode update new content to existing file at end of file.
#append_content_to_file("append_existing_data.txt", "\nToday we are celebrating Diwali in India")

print("_"*50)
####################################
# context manager : Context Manager open file in it context, and it has its own enter and exist method
# no need to close explicitly

def read_with_context(filepath):
    with open(filepath, "r") as file:
        data = file.read()
        print(data)
        print("file closed inside context  :", file.closed) # False

    print("file closed outside context :", file.closed)  # True


#read_with_context("read_data.txt")







# different read option
"""
1.  read number of bytes data :  file.read(10)
2.  read one line at a time : file.readline()
3.  read list of lines : file.readlines()
"""

# 1. read number of bytes data

def read_num_of_bytes_data(filepath, bytes):
    with open(filepath, "r") as file:
        data = file.read(bytes)
        print(data)


#read_num_of_bytes_data("read_data.txt", 30)

# 2. read_specific_number_of_lines

def read_num_lines(filepath, total_line=0):
    with open(filepath, "r") as file:
        for i in range(total_line):
            print(file.readline(), end="")


# read_num_lines("read_data.txt", 4)


# read list of all lines :
def read_list_of_lines(filepath):
    with open(filepath, "r") as file:
        lines_list = file.readlines()
        print(lines_list)

# read_list_of_lines("read_data.txt")


def read_specific_lines(filepath, start, end):
    with open(filepath, "r") as file:
        lines_list = file.readlines()
        for i in range(start-1, end):
            print(lines_list[i], end="")

read_specific_lines("read_data.txt", 3, 6)
