def fibonacci_series(n):
    first = 0
    second = 1
    print(0)
    print(1)
    for _ in range(2, n):
        third = first+second
        print(third)
        # first = second
        # second = third
        first, second = second, third


if __name__ == '__main__':
    fibonacci_series(10)
