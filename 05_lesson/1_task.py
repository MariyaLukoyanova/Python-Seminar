# Последовательностью Фибоначчи называется последовательность чисел 
# a0=0, a1=1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

def Fib(n):
    if n < 2:
        return 1
    return Fib(n-1) + Fib(n-2)
print(Fib(int(input("Enter n: ")))) 