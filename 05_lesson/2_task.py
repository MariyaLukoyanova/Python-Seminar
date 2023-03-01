# Хакер Василий получил доступ к классному журналу и хочет заменить 
# все свои минимальные оценки на максимальные. Напишите программу, которая 
# заменяет оценки Василия, но наоборот: все максимальные – на минимальные.


def max_to_min(list_1):
    Min = min(list_1)
    Max = max(list_1)
    return [Min if i == Max else i for i in list_1]

print(max_to_min([int(i) for i in input().split()]))