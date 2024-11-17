import os, shutil, sys

"""
# get current working directory path
print("current dir :", os.getcwd())
# E:\Trainings\GTM_PS_Batch06_13Sept24\GTM_PS_Batch06\Deepesh\PythonProgramming\Python_OS_Module
"""

"""
# Change the working directory
os.chdir("D:\\Drivers")
print("new updated working directory :", os.getcwd())
#  D:\Drivers
"""

"""
# create directory on local system
os.mkdir("folder1") # create folder in current directory
os.mkdir("D:\\Drivers\\folder1") # create folder in specific directory path
"""

"""
# remove folder from any location
# os.rmdir("D:\\Drivers\\folder1")
# os.rmdir("folder1")
"""


# create a folder
# os.makedirs("D:\\Drivers\\f1\\f2\\f3\\f4\\f5\\f6\\f7")
# os.makedirs("D:\\Drivers\\batch06\\python\\selenium\\pytest\\jenksin\\API\\framework")



# remove folder tree, all folders in the path will removed
#os.removedirs("D:\\Drivers\\batch06\\python\\selenium\\pytest\\jenksin\\API\\framework")


"""
# create multiple folder on same location
for i in range(1, 11):
    os.mkdir(f"D:\\Drivers\\folder{i}")
"""

"""
# Execute windows command from python
os.system("dir E:\\")
os.system("notepad.exe")
os.system("python ./first_program.py")
"""

"""
# check CPU info
print("CPU count :", os.cpu_count()) # CPU count : 8
"""

# Check given path is exists or not
print("check path is available or not :", os.path.exists("D:\\Drivers\\folder1")) # True
print("check path is available or not :", os.path.exists("D:\\Drivers\\folder200")) # False


# Join two paths using os module
path1 = "E:\\Filesdata"
file = "batch04\\count_name.txt"
file_path = os.path.join(path1, file)
print("Filepath :", file_path)
# Filepath : E:\Filesdata\count_name.txt


print("_"*50)
# Check the path is file or folder
file2 = "E:\\Filesdata\\count_name.txt"  # True
print("Check for file :", os.path.isfile(file2)) # True
# Check for file : True

print("Check for folder :", os.path.isdir(file2)) # False
# Check for folder : False

folder_path = "E:\\Filesdata\\batch04"
print("Check for folder :", os.path.isdir(folder_path))
# Check for folder : True

"""
print("_"*50)
# get files/folder list
src_path = "E:\\Filesdata"
data_list = os.listdir(src_path)

print(data_list)

for data in data_list:
    print(data)
    data_path = os.path.join(src_path, data)
    print(data_path)
    if os.path.isfile(data_path):
        print("File")
    else:
        print("Folder")
    print("_"*20)

"""

print("_"*50)
# copy file from one location to another
src_location  = "E:\\Filesdata\\count_name.txt"
tar_location1 = "E:\\Filesdata\\batch06\\count_name.txt"
tar_location2 = "E:\\Filesdata\\batch06\\updated_count_name.txt"
shutil.copy(src_location, tar_location1)
shutil.copy(src_location, tar_location2)


print("Platform name :", sys.platform) #  win32
print("Python Version :", sys.version, sys.version_info, sys.winver)
# 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]
print("size of", sys.getsizeof(tar_location2))
