from custom_and_nested_exception import MedicineExpired
data = {"today": "Friday", "date": "25"}

def function():
    print(data["today"])
    f = open("kkk.txt")
    print(f.read())
    print(next(f))
    print(10+"10")
    print(10/0)
    x = [2,3,4]
    print(x[5])

try:
    print(1)
    print(1*"30")
    print(2)
    try:
        function()
    except (IndexError, StopIteration):
        print(3)
    else:
        print(4)
        print(5)
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
finally:
    print(12)
    try:
        f = open("kkk.txt")
        f.read()
        next(f)
        print(13)
    except FileNotFoundError:
        print(14)
