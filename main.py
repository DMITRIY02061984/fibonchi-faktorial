# ряд фибоначи через рекурсию

def fibonacci(n):
    if n in(1, 2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(13))


# факториал через рекурсию
def faktorial(num):
    if num <= 1:
        return 1
    else:
        return num * faktorial(num - 1 )

x = faktorial(int(input('Введите число: ')))

print(x)
