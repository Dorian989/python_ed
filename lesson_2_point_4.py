my_str = input("Enter row ")
word = []
col = 1
for col, my_str in enumerate(my_str.split()):
    word = my_str.split()
    if len(str(my_str)) <= 10:
     print(f" {col} {my_str }")
    else:
     print(f" {col} {my_str [0:10]}")