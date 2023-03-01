# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def Degree(a, b):
    if b == 0:
        return 1
    if b < 0:
        return Degree(a, b+1) * 1 / a
    return a * Degree(a, b-1)
    
print(Degree(int(input("Enter a: ")), int(input("Enter b: "))))