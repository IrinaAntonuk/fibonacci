def fibonacci(n):
    if n <= 0: return None
    if n <= 2: return 1
    f1, f2 = 1, 1
    for i in range(n - 2):
        fn = f1 + f2
        f1, f2 = f2, fn
    return fn


if __name__ =='__main__':
    n = int(input('Input n: '))
    print(fibonacci(n))
    input()
