"""Write a function that accepts a number as a input and returns the sum of the digits of the given number"""


def sum_of_digits(number):
    # if number<0:
    #     number = abs(number)
    sum = 0
    while number > 0:
        last_digit = number % 10
        sum += last_digit
        number = number // 10
    return sum

# 54321 = 15
# sum = sum_of_digits(-34567455454356)
# print(sum)
#
# """write a function that checks whether the number is armstrong or not, 153 = 1^3+5^3+3^3  = 1+125+27 =153"""
#
# # 370 = 27+343+0 = 370
#
# def is_armstrong(number):
#     sum = 0
#     original_number = number
#     while number > 0:
#         last_digit = number%10
#         sum += last_digit**3
#         number = number//10
#     # if sum == original_number:
#     #     return True
#     # else:
#     #     return False
#     return sum == original_number

# print(is_armstrong(370))


# """write a program to reverse a number 54321 = 12345"""
#
# def







