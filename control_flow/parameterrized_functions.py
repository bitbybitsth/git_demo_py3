def sample_function(age, heigth, weight, temp, bmi):
    print(f"age={age}")
    print(f"height={heigth}")
    print(f"weight={weight}")
    print(f"temp={temp}")
    print(f"bmi={bmi}")
print("test1")


# sample_function(23, 5.4, 55, 37, "GOOD") # positional
# print("")
# sample_function(age=23, heigth=5.5, weight=55, temp=45, bmi="not good")  # keyword
# print("")
# sample_function("not good", 55, 5.5, 23, 37.5)  # positional
# print("")
# sample_function(bmi="not good", weight=55, heigth=5.5, age=23, temp=37.5)  # keyword


##########------------------------
# Rules  - should be passed with required no of parameter, no less no more.


# sample_function(23, 4.9, 45)
# sample_function(23, 4.9, 45, 34, "good")
# sample_function()

#-----------------------------------------------------
# Default parameter

def default_parameterized(age, weight, height, temp=37.5, bmi="good"):
    print(f"age={age}")
    print(f"height={height}")
    print(f"weight={weight}")
    print(f"temp={temp}")
    print(f"bmi={bmi}")


default_parameterized(23, 55, 5.5)
print("")
default_parameterized(23, 55, 5.5, 40.5)
print("")
default_parameterized(23, 55, 5.5, 40.5, "not good")


default_parameterized(weight=56, height=5.6, age=35, temp=50.6)
default_parameterized(weight=56, height=5.6, age=35, bmi="not good")

default_parameterized(23, 56, height=5.6, bmi="Good")
