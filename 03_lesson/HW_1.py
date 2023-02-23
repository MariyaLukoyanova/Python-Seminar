# Требуется вычислить, сколько раз встречается некоторое число X 
# в массиве A[1..N]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X


# n = int(input("Enter N: "))
# x = int(input("Enter X: "))
# print(sum([1 for i in range(1, n+1) if i == x]))

list_nums = [int(input()) for _ in range(int(input("Enter N: ")))]
print(list_nums.count(int(input("Enter X: "))))