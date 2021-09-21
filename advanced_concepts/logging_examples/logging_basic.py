import logging
"""
# debug - 10 - details information, traceback, which would help to diagnose a problem

# info - 20 - info states the status of the operations

# warning - 30 - an indication is that something is working now as expected but in future it may not, disk space low

# error - 40 - if code breaks due to some error we should log error with this level

# critical - 50 - serious errors which will stop execution of programs should be logged using critical

"""

# by default level of logging is WARNING, hence logs will be logged from warning and above

logging.basicConfig(level=10, filename="sample.log",
                    format="%(asctime)s -> %(message)s ->at line no %(lineno)d in %(funcName)s, file=%(filename)s ")


def add(a,b):
    logging.info("Addition Called")
    try:
        return a+b
    except:
        logging.info("database conneciton errro")
        logging.debug("configuartions=")

def sub(a,b):
    logging.debug(f"Subtraction called with a={a}, b={b}")
    return a-b

def mul(a,b):
    if b==0:
        logging.warning(f"b={b} and zero multiplied by zero is zero")
    return a*b

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        logging.error(f"b is given a zero so cannot divide by zero")
        return 1

def mod(a,b):
    try:
        return a%b
    except:
        logging.critical("some error occoured")

# print("add called with 10, 20 and result is =", add(10,20))
# print("sub called with 10, 20 and result is =", sub(10,5))
# print("mul called with 10, 20 and result is =", mul(10,2))
# print("div called with 10, 20 and result is =", div(10,2))
# print("mod called with 10, 20 and result is =", mod(10,2))


# logging.warning(f"add called with 10, 20 and result is ={add(10,20)}" )
# logging.warning(f"sub called with 10, 20 and result is ={sub(10,5)}" )
# logging.warning(f"mul called with 10, 20 and result is ={mul(10,2)}" )
# logging.warning(f"div called with 10, 20 and result is ={div(10,2)}")
# logging.warning(f"mod called with 10, 20 and result is ={mod(10,'4')}")

add(10,20)
sub(10,5)
mul(4,0)
div(5,0)
mod(3,"4")
