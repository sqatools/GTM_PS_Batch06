def read_file(filepath):
    file=open(filepath, "r")
    data=file.read()
    print(data)
    file.close()

read_file("C:\Users\Test Application\Documents\Todaysnews.txt")