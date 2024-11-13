"""
There are three mode of the file to access
1.Read mode(r):
2.Write mode(w):
3.append mode(a):

"""
def read_file(filepath):
    file = open(filepath,"r")
    data  = file.read()
    print(data)
    file.close()
# read_file from current location
# read_file("read_data.txt")

# read file from specific path
#read_file("C:\Test")

############ open file in write mode###############
def write_to_file(filepath,content):
    file = open(filepath,"w")
    data = file.write()
    # file.write(content)
    file.close()



# 1.file doest not exist: it will create a new with specified name and add content  to the file
# write_to_file("write_data.txt", "India lost second T20 match with South Africa")

# 2. Existing file: write method will over write the existing content of the file
write_to_file("write_old_file.txt","India lost second t20 match with south Africa")


##########Append  content to the file############
print("-"* 50)
def Append_content_to_file(filepath,content):
# open file in append mode
  file  = open (filepath,"a")
  file.write(content)
  file.close()


#1.file doesnot exist:Append mode also create anew file ,if file doesnot exist.
Append_content_to_file("append_data.txt", "Hell0 world")
#2. Existing file:Append mode update new content to existing file at end of file
Append_content_to_file("append_existing_data.txt"," \nToday we are celebrating Diwali in india")