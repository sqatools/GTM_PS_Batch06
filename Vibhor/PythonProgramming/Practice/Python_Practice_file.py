import os
'''
#current directory path
print("Current Directory: ", os.getcwd())

#change directory path
os.chdir("D:\\AutomationRepo\\GTM_PS_Batch06\\Vibhor\\PythonProgramming\\Practice")
print("Updated Directory: ", os.getcwd())


#create folder
os.mkdir("folder1") #create folder in current directory
os.mkdir("E:\\folder1") #create folder in different directory

#remove folder
os.rmdir("folder1") # remove folder in current directory
os.rmdir("E:\\folder1") #remove folder in different directory


#create a folder tree
os.makedirs("E:\\F1\\F2\\F3\\F4") #create  tree
os.removedirs("E:\\F1\\F2\\F3\\F4") #remove tree

# create 10 folders with Loop
for i in range(1,11):
    os.mkdir(f"E:\\folder{i}")
'''

os.system("Notepad.exe") #open notepad
os.system("python ./basic.py") #open python file  in same folder
print(os.cpu_count()) #CPU count
os.system("control") #open control panel