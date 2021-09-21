finally:
    print(12)
    try:
        f = open("kkk.txt")
        f.read()
        next(f)
        print(13)
    except FileNotFoundError:
        print(14)
    else:
        print("^^^")
# print(10+"10")