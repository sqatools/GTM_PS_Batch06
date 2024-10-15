print(dir(str))
"""
'capitalize', 'casefold', 'center', 'count', 'encode',
 'endswith', 'expandtabs', 'find', 'format', 'format_map', 
 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
 'isdigit', 'isidentifier', 'islower', 'isnumeric',
  'isprintable', 'isspace', 'istitle', 'isupper', 'join', 
  'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
   'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',
    'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
    'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper',
     'zfill'
"""
######
# lower() and upper() Method:

str_a = "Hello Good Morning"
print(str_a.lower())  # hello good morning
print(str_a.upper())  # HELLO GOOD MORNING

# isupper() and islower() : These methods check the given string in upper case
#                    or lower case.

str_b = "PYTHON"
str_c = "programming"
str_d = "Language"
print("str_b :", str_b.isupper())  # True
print("str_c :", str_c.islower())  # True
print("str_d :", str_d.isupper())  # False
print("str_d :", str_d.islower())  # False

#######
# swapcase() method : This method convert all upper case character to lower, and
#  lower case character to upper case.

str_e = "LearNing PyThon ProgRamminG"
print("str_e :", str_e.swapcase()) # lEARnING pYtHON pROGrAMMINg

#######
# title() method: This method convert first character of each word into camel case.
str_f = "LearNing PyThon ProgRamminG"
print(str_f.title())  # Learning Python Programming

str_g = "Hello Good Morning"
str_h = "GooD Evening"
print("str_g :", str_g.istitle())  # True
print("str_h :", str_f.istitle())  # False

