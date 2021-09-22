n =  int(input("Enter a number"))

def pattern1(n):
    """
    n=6
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * * * *
    :return:
    """
    for i in range(1, n+1):
        for j in range(i):
            print("*", end=" ")
        print("")
        # print("* "*i)

# pattern1(n)

def pattern2(n):
    """
    * * * * *
    * * * *
    * * *
    * *
    *
    :param n:
    :return:

        for i in range(1, n+1):
            for j in range(i):
                print("*", end=" ")
            print("")
    """
    for i in range(n,0,-1):
        for j in range(i):
            print("*", end=" ")
        print("")

# pattern2(n)

def patern_3(n):
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    :param n:
    :return:
    """
    for i in range(0,n):
        print(" "*n+"* "*(i+1))
        n = n-1
        # for j in range(n):
        #     print(end=" ")
        # n=n-1
        #
        # for k in range(0, i+1):
        #     print("*", end=" ")
        # print("")

# patern_3(n)

def pattern_4(n):
    """
    * * * * *
     * * * *
      * * *
       * *
        *
    :param n:
    :return:
    """
    for i in range(0, n):
        print(" "*i + "* " *n)
        n = n - 1
# pattern_4(n)

def pattern_5(n):
    """
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * * * *
    * * * * *
    * * * *
    * * *
    * *
    *
    :param n:
    :return:
    """
    pattern1(n)
    print("* "*(n+1))
    pattern2(n)
# pattern_5(n)

def xmas(n):
    """
        *
       * *
      * # *
     * & * *
    * * * * *
        *
       * *
      * + *
     * @ ^ *
    * * * * *
        *
       * ^
      * * *
     * $ * *
    * * * * *
       |||
       |||
       |||

    :return:
    """
    # patern_3(8)
    # patern_3(8)
    # patern_3(8)
    # for i in range(0, 6):
    #     print(" " * 6 + "#" * 4)

    import random
    l = ['@', 'O', '%', 'M', 'Q']
    for i in range(0, 3):
        for j in range(0, 8):
            x = "*" * (2 * j + 1)
            # print("OOOOOOOOOOOO", x)
            if j > 1 and j % 2 == 0:
                x = list(x)
                x[random.randint(1, j)] = random.choice(l)
                x = "".join(x)
            print(" " * (8 - j - 1) + x)
    for i in range(0, 6):
        print(" " * 6 + "#" * 4)

xmas(n)
