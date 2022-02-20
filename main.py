print("hello, world")


# площадь треугольника
# a = int(input())
# b = int(input())
# c = int(input())
# p = (a+b+c)/2
# S = (p * (p - a) * (p - b) * (p - c))**0.5
# print(S)

# определение високосного года
# x = int(input())
# if (x % 4 == 0 and x % 100 != 0) or x % 400 ==0:
#    print('Високосный')
# else:
#    print('Обычный')

# различные знаки действий
# a = float(input())
# b = float(input())
# c = (input())
# if c == "pow":
#    print (a ** b)
# elif c == ("mod" or c == "div") and b == 0:
#    print("Деление на 0!")
# elif c == "mod":
#    print(a % b)
# elif c == "div":
#    print(a // b)
# elif c == "+":
#    print(a + b)
# elif c == "-":
#    print(a - b)
# elif c == "/":
#    print(a / b)
# elif c == "*":
#    print(a * b)

# вычесление площадей
# #x = (input())
# if x == "треугольник":
#    a = int(input())
#    b = int(input())
#    c = int(input())
#    p = (a+b+c)/2
#    S = (p * (p - a) * (p - b) * (p - c))**0.5
#    print(float(S))
# elif x == "прямоугольник":
#    a = int(input())
#    b = int(input())
#    print(float(a * b))
# if x == "круг":
#    r = int(input())
#    print(float(r ** 2 * 3.14))

# во сколько нужно поставить будильник
# X = int(input())
# H = int(input())
# M = int(input())
# print(int((X + H * 60 + M)) // 60)
# print(int((X + H * 60 + M)) % 60)

# расположить числа сначало большее потом меншее)
# a, b, c = int(input()), int(input()), int(input())
# if a >= b and a >= c:
#    print(a)
#    if b >= c:
#        print(c)
#        print(b)
#    else:
#        print(b)
#        print(c)
# elif b >= a and b >= c:
#    print(b)
#    if a >= c:
#        print(c)
#        print(a)
#    else:
#        print(a)
#        print(c)
# elif c >= a and c >= b:
#    print(c)
#    if a >= b:
#        print(b)
#        print(a)
#    else:
#        print(a)
#        print(b)

# окончания чисел (ов, а)
# n = int(input())
# if 11 <= (n % 100) <= 19:
#    print(n, 'программистов')
# else:
#    if (n % 10) == 1:
#        print(n, 'программист')
#    elif (n % 10) == 2 or (n % 10) == 3 or (n % 10) == 4:
#        print(n, 'программиста')
#    else: print(n, 'программистов')

# проверка счастливого билета
# n = int(input())
# a = int(n % 10)
# b = int(n % 100) // 10
# c = int(n % 1000) // 100
# d = int(n // 1000) % 10
# e = int(n // 10000) % 10
# f = int(n // 100000)
# if a + b + c == d + e + f:
#    print ("Счастливый")
# else:
#    print("Обычный")

# выводим нечетные числа
# a = 5
# while a <= 55:
#    print(a, end=' ')
#    a += 2

# выводим нечетные числа
# a = 5
# while a <= 55:
#    if a % 2 != 0:
#        print(a, end=' ')
#    a += 1


# вводишь 2 числа, выдает сумму чисел от одного до другого
# a = int(input())
# b = int(input())
# s = int(0)
# while a <= b:
#    s += a
#    a += 1
# print(s)

# вводишь 2 числа, выдает сумму нечетных чисел от одного до другого через for
# a, b = input().split()
# a = int(a)
# b = int(b)
# s = int(0)
# for i in range(a, b+1):
#    if i % 2 != 0:
#        s += i
# print(s)

# вводишь 2 числа, выдает сумму нечетных чисел (проверка четного вначале) от одного до другого через for
# a, b = (int(i) for i in input().split())
# s = int(0)
# if a % 2 == 0:
#    a += 1
# for i in range(a, b+1, 2):
#    s += i
# print(s)

# вводишь 2 числа, список, среднее арифметическое кратное 3
# a = int(input())
# b = int(input())
# s = int(0)
# v = int(0)
# while a % 3 != 0:
#    a += 1
# for i in range(a, b + 1, 3):
#    s += i
#    v = v+1
# print(s / v)


# вводишь числа пока не введешь 0, после сумма введенных чисел
# n = int(input())
# s = int(0)
# while n != 0:
#    s += n
#    n = int(input())
# print(s)

# на сколько минимальых частей порезать пирог, для каждой из команд
# a = int(input())
# b = int(input())
# x = int(1)
# while x % a != 0 or x % b != 0:
#    x += 1
# print(x)

# ввод двух чисел через пробел split и произведение этих чисел, всего 5 значений, нули игнорируются, два нуля прерывание
# i = 0
# while i < 5:
#    a, b = input().split()
#    a = int(a)
#    b = int(b)
#    if a == 0 and b == 0:
#        break
#    if a == 0 or b == 0:
#        continue
#    print(a * b)
#    i += 1

# меньше 10 не выводим, от 10 до 100 печатаем, свыше 100 прерываем
# a = 0
# while a <= 100:
#    a = int(input())
#    if a < 10:
#        continue
#    if 10 <= a <= 100:
#        print(a)
#    else: break


# квадрат из звездочек
# a = int(input())
# for i in range(a):
#    for j in range(a):
#        print('*', end='')
#    print()

# разделители и конец строки в print
# print(1, 2, 3)
# print(4, 5, 6)
# print(1, 2, 3, sep=', ', end='. ')
# print(4, 5, 6, sep=', ', end='. ')
# print()
# print(1, 2, 3, sep='', end=' -- ')
# print(4, 5, 6, sep=' * ', end='.')


# таблица пифагора
# for i in range(1, 10+1):
#    for j in range (1, 10+1):
#        print(i*j, end='\t')
#    print()

# вводишь 2 числа, выдает сумму нечетных чисел от одного до другого через for
# a, b = input().split()
# a = int(a)
# b = int(b)
# s = int(0)
# for i in range(a, b+1):
#    if i % 2 != 0:
#        s += i
# print(s)

# вводишь 2 числа, выдает сумму нечетных чисел (проверка четного вначале) от одного до другого через for
# a, b = (int(i) for i in input().split())
# s = int(0)
# if a % 2 == 0:
#    a += 1
# for i in range(a, b+1, 2):
#    s += i
# print(s)

# вводишь 2 числа, список, среднее арифметическое кратное 3
# a = int(input())
# b = int(input())
# s = int(0)
# v = int(0)
# while a % 3 != 0:
#    a += 1
# for i in range(a, b + 1, 3):
#    s += i
#    v = v+1
# print(s / v)

# Напишите программу, на вход которой даются четыре числа aa, bb, cc и dd, каждое в своей строке. Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a; b][a;b] на все числа отрезка [c;d][c;d].
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# for i in range(c, d+1):
#    print('\t',i,end="")
# print()
# for i in range(a, b+1):
#    print(i, end="")
#    for j in range (c, d+1):
#        print('\t', i*j, end='')
#    print()

# считает кол-во символов "С"
# stroka = input()
# s = 0
# for i in stroka:
#    if i == 'C':
#        s += 1
# print(s)

# считает кол-во символов "С" через count
# stroka = input()
# print(stroka.count('C'))

# методы у строк
# X.count(x или 'x')
# X.find(x или 'x')
# X.find('x') , но лучше if 'x' in X:
# X.replace('x', 'y')
# resUp = stroka.upper()
# resLo = stroka.lower()

# процент отношения кол-ва "С" + "G" ко всем буквам
# stroka = input()
# resUp = stroka.upper()
# s = resUp.count('C') + resUp.count('G')
# all = len(stroka)
# print(s / all * 100)

# Сравнение в обратном порядке
# stroka = 'довод'
# revers= stroka[::-1]
# if stroka == revers:
#    print('палиндром')
# else:
#    print('не палиндром')

# stroka = 'abcdefghijk'
# print(stroka[::-1])

# записать код ДНК в виде a4b2c1a2
# DNA_Lo = input()
# x = len(DNA_Lo)
# s = 1
# for i in range(0, x - 1):
#     if DNA_Lo[i] == DNA_Lo[i + 1]:
#         s += 1
#     else:
#         print(DNA_Lo[i], s, sep='', end='')
#         s = 1
# print(DNA_Lo[x - 1], s, sep='')

# считает сумму двух чисел, которые стоят справа и слева от введенного числа
# a = [int(i) for i in input().split()]
# s = len(a)
# if s == 1:
#     print(str(a)[1:-1])
# else:
#     for i in range(0, s):
#         if i == s - 1:
#             print(a[i - 1] + a[0], end=' ')
#         else:
#             print(a[i - 1] + a[i + 1], end=' ')

# если число двойное то один его элемент оставляем, одинарные не выводим
# a = [int(i) for i in input().split()]
# x = int(a[0])
# s = len(a)
# while s != 0:
#     b = a.count(a[0])
#     if b > 1:
#         print(a[0], end=' ')
#         v = a[0]
#         a.remove(a[0])
#         z = a.count(v)
#         while z != 1:
#             index = a.index(v)
#             a.remove(a[index])
#             s -= 1
#             z -= 1
#         s -= 1
#     else:
#         a.remove(a[0])
#         s -= 1

# # # вводишь числа пока не введешь их сумма не станет нулем, после сумма квадратов введенных чисел
# # a = [int(input())]
# sum = [0]
# sum[0] += a[0]
# sum2 = [0]
# sum2[0] += a[0]**2
# while sum[0] != 0:
#     a = [int(input())]
#     sum[0] += a[0]
#     sum2[0] += a[0]**2
# print(*sum2)


# выводит 1 -1 раз, 2- 2раза, 3 3 раза, а число чифр в строке = n
# # n = [int(input())]
# sum =[]
# for i in range(1, n[0] + 1):
#     s = [i] * i
#     sum += s
# print(*(sum)[0:n[0]])

# Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки, которая выводит все позиции, на которых встречается число xx в переданном списке lstlst.
# lst = [int(i) for i in input().split()]
# x = [int(input())]
# if x[0] not in lst:
#     print('Отсутствует')
# else:
#     s = 0
#     for i in lst:
#         if i != x[0]:
#             s += 1
#         else:
#             print(s, end=' ')
#             s += 1


# Двумерные списки
# a = [[0] * n for i in range(n)]
# n = 3
# a = [[0 for j in range(n)] for i in range(n)]
#
# n, m, k = (int(i) for i in input().split())
# a = [[0 for j in range(m)] for i in range(n)]

# a = [int(i) for i in input()]

# # как заводить двумерные списки
# a = []
# n = int(input())   #кол-во строк
# m = int(input())   #кол-во столбцов
#
# for i in range(n):
#     b = []
#     for j in range(m):
#         b.append(int(input()))
#     a.append(b)
# for i in a:
#     print(i)


# обход вар 1
# a = [[1, 2, 3], [4, 3, 2], [6, 5, 4]]
# print(a[1][0]) - # печать конкретного элемента матрицы
# for i in a:
#     print(i)

# Обход вар 2 (нет индекса, и список не меняется снаружи цикла)
# a = [[1, 2, 3], [4, 3, 2], [6, 5, 4]]
# for i in a:
#     for j in i:
#         print(j, end=' ')
#     print()

#обход вар3 по индексам
# a = [[1, 2, 3], [4, 3, 2], [6, 5, 4], [4, 7, 1]]
# for i in range(4):          #здесь обход по строчкам слева направо
#     for j in range(3):
#         print(a[i][j], end=' ')
#     print()

# здесь обход по столбцам сверху вниз
# for j in range(3):      #кол-во строк 3 (а индекс 0.1.2 ставим 3 так как последний не входит)
#     for i in range(4):   #кол-во столбцов 43 (а индекс 0.1.2.3 ставим 3 так как последний не входит)
#         print(a[i][j], end=' ')
#     print()

# здесь обходим начиная с последнего справа налево и снизу вверх
# a = [[1, 2, 3], [4, 3, 2], [6, 5, 4], [4, 7, 1]]
# print(a)
# for i in range(3, -1, -1):       # кол-во столбцов 4
#     for j in range(2, -1, -1):   # кол-во строк 3
#         print(a[i][j], end=' ')
#     print()

#  сумма строк
# a = [[1, 2, 3], [4, 3, 2], [6, 5, 4], [4, 7, 1]]
# for i in range(4):
#     s = 0
#     for j in range(3):
#         s += a[i][j]
#     print(s)


# вводим матрицу построчно через пробел пока не ввели end, в потом выводит матрицу из суммы 4х чисел вокруг каждого числа
# lst = []
# b = ()
# while b != ['end']:
#     b = input().split()
#     if b == ['end']:
#         break
#     else:
#         a = []
#         for i in b:
#             i = int(i)
#             a.append(i)
#         lst.append(a)
#
# n = len(lst)  # строки
# m = len(lst[0]) # столбцы
#
# # for i in range(n):          # тестовый принт здесь обход по строчкам слева направо
# #     for j in range(m):
# #         print(lst[i][j], end=' ')
# #     print()
# #
# for i in range(n):
#     s = 0
#     for j in range(m):
#         s = lst[i - 1][j] + lst[i + 1 - n][j] + lst[i][j - 1] + lst[i][j + 1 - m]
#         print(s, end=' ')
#     print()

# спираль
# a = []
# b = []
# n = int(input())   #кол-во строк
# m = n
# for i in range(1, n + 1):
#     b.append(i)
# a.append(b)
# for i in range(1, n):
#     b = []
#     for j in range(1, m +1):
#         j += i*n
#         b.append(j)
#     a.append(b)
# # print(a)
# print(end='\n')
#
# for i in a:
#     print(i)
#
#
# for i in range(1):          # тестовый принт здесь обход по строчкам слева направо
#     for j in range(m):
#         print(a[i][j], end=' ')
#     print()
# for j in range(3, 4):      #кол-во строк 3 (а индекс 0.1.2 ставим 3 так как последний не входит)
#     for i in range(4):   #кол-во столбцов 43 (а индекс 0.1.2.3 ставим 3 так как последний не входит)
#         print(a[i][j], end=' ')
#     print()
# for i in range(3, 2, -1):       # кол-во столбцов 4
#     for j in range(3, -1, -1):   # кол-во строк 3
#         print(a[i][j], end=' ')
#     print()

# функции
# a = int(input())
# b = int(input())
# c = int(input())
# def min2(a,b):
#     if a <= b:
#         return a
#     else:
#         return b
# m=min2(min2(a, b), c)
# print(m)


def f(n):
    return n * 10 + 5
m=f(f(f(10)))
print(m)

# спираль через функцию
def spiral(n):
    dx, dy = 1, 0
    x, y = 0, 0
    myarray = [[None] * n for j in range(n)]
    for i in range(1, n ** 2 + 1):
        myarray[x][y] = i
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and myarray[nx][ny] == None:
            x, y = nx, ny
        else:
            dx, dy = -dy, dx
            x, y = x + dx, y + dy
    return myarray


def printspiral(myarray):
    n = range(len(myarray))
    for y in n:
        for x in n:
            print(myarray[x][y], end=' ')
        print()


n = int(input())
printspiral(spiral(n))