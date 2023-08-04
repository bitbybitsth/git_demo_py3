import time

def is_balanced(st):
    # time.sleep(1)
    brackets = {"{": "}", "[": "]", "(": ")"}
    open_brackets = list(brackets.keys())
    close_brackets = list(brackets.values())
    stack = []
    for s in st:
        if s in open_brackets:
            stack.append(s)
        if s in close_brackets:
            s_open = open_brackets[close_brackets.index(s)]
            if len(stack) > 0:
                if s_open != stack.pop():
                    return False
            else:
                return False
    if len(stack) > 0:
        return False
    else:
        return True

st = "{[{()}]}}"
t1 = time.perf_counter()
check = is_balanced(st)
t2 = time.perf_counter()

print(f"function took {t2-t1} seconds to execute")

# print("before sleep")
# time.sleep(3)
# print("after sleep")


t1 = time.perf_counter()
