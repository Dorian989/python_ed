element_count = int(input("Enter quantity: "))
my_list = []

ind1 = 0
ind2 = 0

while ind1 < element_count:
    my_list.append(input("Next value: "))
    ind1 += 1

for elem in range(int(len(my_list)/2)):
        my_list[ind2], my_list[ind2 + 1] = my_list[ind2 + 1], my_list[ind2]
        ind2 += 2
print(my_list)