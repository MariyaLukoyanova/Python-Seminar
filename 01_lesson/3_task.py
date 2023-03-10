# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.

n = int(input("В какой вагон от головы сел? "))
m = int(input("Какой номер у этого вагона? "))
if (n == m):
    print("Невозможно посчитать длину электрички!") 
else:
    print(f"В электричке {n+m-1} вагонов")