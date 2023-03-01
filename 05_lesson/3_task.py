# Напишите функцию, которая принимает одно число и проверяет, 
# является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

def Simple(n):
    if n == 2:
        return "yes"
    elif n < 2 or n % 2 == 0:
        return "no"
    for i in range(3, int((n**0.5)+1), 2):
        if n % i == 0:
            return 'no'
    return 'yes'
        
print(Simple(int(input("Enter n: "))))
    



