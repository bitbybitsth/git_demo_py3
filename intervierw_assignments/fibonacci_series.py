"write a function that will print n numbers in fibonacci series"

# 0 1 1 2 3 5 8 13 21 34

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

def fibonacci_series_list(n):
    """
    write a function that return a list of fibonacci series containing n elements.
    :param n:
    :return:
    """
    fib_list = [0, 1]
    loop_con = list(range(0, n-2))
    for i in range(0, n-2):
        fib_list.append(fib_list[i] + fib_list[i+1])
    return fib_list


fi = fibonacci_series



fi(10)
fibonacci_series(5)
