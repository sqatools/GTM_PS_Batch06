# 1. write a python to read two files and append in third first

def read_write_content_to_third_file(file1, file2, file3):
    with open(file1, "r") as file1_obj:
        file1_data = file1_obj.read()

    with open(file2, "r") as file2_obj:
        file2_data = file2_obj.read()

    with open(file3, "a") as file3_obj:
        file3_obj.write(file1_data)
        file3_obj.write(file2_data)


#read_write_content_to_third_file("file_1.txt", "file_2.txt", "file_3.txt")

#2. write a python program to replace one with another in the file

def replace_file_content(file_path, word1, word2):
    with open(file_path, "r") as file:
        data = file.read()
    updated_data = data.replace(word1, word2)

    # print updated data, does not update file
    print(updated_data)

    # overwrite the previous content with updated data.
    with open(file_path, "w") as file2:
        file2.write(updated_data)


replace_file_content("read_data.txt", "NIKITA", "MADHURI")
