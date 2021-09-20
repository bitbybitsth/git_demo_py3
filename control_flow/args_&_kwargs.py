"""
in function we can accept arbitrary no of argument.
*args & **kwargs
*args -> holds arbitary no of positional arhuments
*kwargs -> holds arbitrary no of Keyword arguments.


"""


def arbitrary_arguments(*args, **kwargs):
    print(args)
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(key, value)
    print(kwargs)


# arbitrary_arguments(1,2,3,4,5,6,7,8, a=10, b=20, c=30, d=40)


def check_weather(location, day, **filter_param):
    temprature_now = 38.0
    unit = filter_param.get("unit", "celsius")
    if unit != "celsius":
        temprature_now = (temprature_now * 9 / 5) + 32
    print(f"weather of {location} on {day} is {temprature_now} {unit}")


check_weather("pune", "today")


def arbitrary_with_others(a, b, c, *args, z="JKL", **kwargs):
    print(f"{a} ,{b}, {c}")
    print(args)
    # print(f"x={x}, y={y}, z={z}")
    print(kwargs)


arbitrary_with_others(False, 10, 45.6, [1, 2], (2, 3), {3, 4}, {1: 2}, k={6: "six"})
