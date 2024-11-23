def read_file(filepath):
    file = open(filepath, "r")
    data = file.read()
    print(data)
    file.close()

read_file("new_text_file")
# new_text_file("E:\\readfile\\new_file.txt")
