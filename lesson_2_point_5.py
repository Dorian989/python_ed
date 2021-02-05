my_list = [7, 5, 3, 3, 2]
print(f"Rating - {my_list}")
digit = int(input("Enter digit "))
if my_list[0] < digit:
    my_list.insert(0, digit)
    print(f"now rating - {my_list}")
elif my_list[-1] > digit:
    my_list.append(digit)
    print(f"now rating - {my_list}")
elif (my_list[3] > digit) or (my_list[4] < digit):
    my_list.insert(3, digit)
    print(f"now rating - {my_list}")