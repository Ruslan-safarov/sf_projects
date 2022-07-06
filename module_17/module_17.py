# функция двоичного поиска
def binary_search(num, my_list):
    middle = len(my_list) // 2
    # if my_list[middle] < num and my_list[middle+1] >= num:
    #     print('asdfasdf')
    #     return middle
    if my_list[middle] == num and my_list[middle - 1] < num:
        return middle - 1
    elif num < my_list[middle]:
        return binary_search(num, my_list[:middle])
    else:
        return binary_search(num, my_list[middle:]) + len(my_list[:middle])


# функция сортировки списка
def list_sort(my_list):
    for n in range(len(my_list)):
        n += 1
        for j in range(len(my_list) - 1):
            if my_list[j] > my_list[j + 1]:
                buf = my_list[j + 1]
                my_list[j + 1] = my_list[j]
                my_list[j] = buf
    return my_list


a = input("Введите числа через пробел")
print(type(a))
b = a.split(" ")

for i in range(len(b)):
    b[i] = int(b[i])
print(b)

c = int(input("Введите любое число"))
d = 0

list_sort(b)
print(b)

if binary_search(c, b) <= len(b):
    d = binary_search(c, b)
    print(d)
else:
    print('Нет элемента, соответсвующего условиям')

# Проверка:
# вводим 9 8 7 6 5 4 3 2 1
# затем три кейса, когда вводимое число принимает значения: 3, 5, 7