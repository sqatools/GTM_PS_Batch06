def greeting():
    return "Good Morning"
    return "Good Evening"

msg = greeting()
print(msg)
# Good Morning


def greeting_msgs():
    yield "Good Morning"
    yield "Good Afternoon"
    yield "Good Evening"
    yield "Good Night"

values = greeting_msgs()
print(values)
# print(next(values))
# print(next(values))
# print(next(values))
# print(next(values))
#print(next(values))

for data in values:
    print(data)



def get_square_of_longs_num(nums):
    for val in nums:
        yield val

long_nums = [4, 5, 7]*4000
output = get_square_of_longs_num(long_nums)

for data in output:
    print(data)
