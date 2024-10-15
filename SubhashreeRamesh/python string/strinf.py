str_1="hello world"
for ch in str_1:
    print(ch,end=" ")

    str_1 = "hello world"
    str_len=len(str_1)
    for i in range(str_len):
        print(i, str_1)

        str3 = "Indian is Batsman virat best"
        First = str3[-10:-5:1]
        second = str3[7:9]
        third = str3[-4:]
        fourth = str3[0:6]
        fifth = str3[10: -11]
        # } {[]
        result = f"{First} is {third} {fourth} {fifth}"
        print(result)

        str5 = "learning python"

        print(str5[-2: 2:-2])