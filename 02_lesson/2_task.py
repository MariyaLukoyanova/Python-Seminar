# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
a = int(input("Введите число для проверки: "))
first = 0
second = 1
n = 2
while a >= second:
    if a == second:
        print(f"Это число Фибоначчи под номером {n}")
        break
    first, second = second, first+second
    n += 1
else:
    print("-1")