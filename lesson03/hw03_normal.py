# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib = [1, 1]
    idx = 2
    while idx <= m:
        fib.append(fib[idx-2] + fib[idx-1])
        idx+=1

    print(fib[n-1:m])
    return fib

fibonacci(10,35)
    

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    sorted_list = []
    i = 1
    count = len(origin_list)
    while i <= count:
        max = origin_list[0]
        for idx in origin_list:
            if idx > max:
                max = idx
        origin_list.remove(max)
        i += 1
        sorted_list.append(max)
    print (sorted_list)
    return sorted_list


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filters(n, m):
    new_list = []

    list_map = list(map(n,m))
    idx = 0
    for itm in m:
        if list_map[idx]:
            new_list.append(itm)
        idx+=1

    return new_list

print(filters(lambda x: x>=4, [2,4,12,0,4,21]))
print(filters(len, ['hello','','  ','0','4','21']))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math

coord = ((3, 2), (10, 4), (1, 6), (8, 8))

def rectangle_check(c):
    return abs(c[0][0] - c[1][0]) == abs(c[2][0] - c[3][0]) and abs(c[0][1] - c[2][1]) == abs(c[1][1] - c[3][1])

if rectangle_check(coord):
    print("Является параллелограммом")
else:
    print("Не является параллелограммом")

