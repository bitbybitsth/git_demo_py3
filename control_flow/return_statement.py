# return is used to return a value from the function
# by default return None is executed at the end if no return statement present or no return statement in execute
# as return gets executed the execution is returned form the function to the calling position

# function can have multiple return statements but only one will be execute at a time.
# we can return multiple value from one function, it would be returned as tuple with elements we are trying to return


def is_prime(num):
    d= {1:2}
    if 2 > num > 0:
        return True, "as num is less tahn 2 and greater than 0", [1,2]

    if num <= 0:
        return False, "cannot process negative numbers", (1,2)

    for divisor in range(2,(num//2+1)):
        if num % divisor == 0:
            return False, f"{num} got divided by {divisor} hence not prime", {1,2}
    else:
        return True, f"{num} was not divided by any number less than its half", d

result = is_prime(23)

if result[0]:
    print(result[1])
else:
    print(result[1])

