# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
n = int(input("Введите размер n: "))
m = int(input("Введите размер m: "))
k = int(input("Введите k долек: "))
if ((k % n == 0) or (k % m == 0)) and (k < m*n):
    print("Такой кусок можно отломить")
elif k == m*n:
    print("Возьми шоколадку целиком :)")
else:
    print("Такой кусок нельзя отломить")
