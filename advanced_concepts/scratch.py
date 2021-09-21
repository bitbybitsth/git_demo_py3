except (KeyError, ValueError):
    try:
        print(6)
        print(1+"30")
        print(7)
    except:
        print(8)
else:
    print(9)
    try:
        try:
            print(1/0)
        except ValueError:
            print(10)
    except ZeroDivisionError:
        print(11)
