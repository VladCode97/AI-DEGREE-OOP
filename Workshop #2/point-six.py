def factorial(x) -> int:
    if(x == 1 or x == 0):
        return 1
    return x * factorial(x - 1)


print(f'factorial: {factorial(5)}')

#point two
def sum(n: int) -> int:
    sum_result: int = 0
    for i in range(1, n + 1):
        sum_result+=i
    return sum_result

def sum_recursive(n: int) -> int:
    if(n == 1):
        return 1
    else:
        return n + sum_recursive(n-1)


print(sum(100))
print(sum_recursive(100))
