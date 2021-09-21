import

# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
#
# gen_obj = simple_generator()
# print(gen_obj)
#
# x = next(gen_obj)
# # y = next(gen_obj)
# # z = next(gen_obj)
#
# print(x)
#
# print(next(gen_obj))
# print(next(gen_obj))
# # print(next(gen_obj))
#
#
# gen = simple_generator()
# for item in gen:
#     print(item)

def thousand_number_list():
    return list(range(1,10001))

x = thousand_number_list()
print(x)

def thouand_value_generator():
    for i in range(1, 10001):
        yield i

y = thouand_value_generator()

print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
for _ in range(5,500):
    print(next(y))



