month = int(input("Enter month number  "))
list_1 = ['Winter', 'Spring', 'Summer', 'Fall']
if month == 12 or month == 1 or month == 2:
    print(list_1[0])
elif month == 3 or month == 4 or month == 5:
        print(list_1[1])
elif month == 6 or month == 7 or month == 8:
            print(list_1[2])
elif month == 9 or month == 10 or month == 11:
    print(list_1[3])
else:
    print('Wrong month number')

