"""
Three Modes of File Access
1- Read Mode (r)
2- Write Mode (w)
3- Append Mode (a)
"""


def read_file(filepath):
    file = open(filepath, "r")
    data = file.read()
    print(data)
    file.close()


read_file("E:\\News.txt")
