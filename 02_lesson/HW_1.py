# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
n = int(input("Введите количество монеток: "))
count = 0
for _ in range(n):
    i = int(input("Ведите 0 или 1: "))
    if i == 0:
        count+=1
if count > n - count:
    print(f"Необхожимо перевернуть минимум {n - count} монеток")
else:
    print(f"Необхожимо перевернуть минимум {count} монеток")