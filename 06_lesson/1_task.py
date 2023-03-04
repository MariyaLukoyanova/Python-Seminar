# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# 3 3 2 12
# list_1=[int(input()) for _ in range(int(input("Enter N: ")))]
# list_2=[int(input()) for _ in range(int(input("Enter M: ")))]
list_1 = list(map(int, input("Enter massive 1: ").split()))
list_2 = list(map(int, input("Enter massive 2: ").split()))
print([i for i in list_1 if i not in list_2])