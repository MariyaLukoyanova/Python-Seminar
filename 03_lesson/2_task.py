# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.
list_nums = [1, 2, 3, 4, 5]
k = int(input("Enter k: "))
print(list_nums)
# result = list_nums[(k % len(list_nums)):]+list_nums[:(k % len(list_nums))]
# print(result)
for _ in range(k % len(list_nums)):
    list_nums.insert(len(list_nums), list_nums.pop(0))
print(list_nums)