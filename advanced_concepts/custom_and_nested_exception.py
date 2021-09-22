class MedicineExpired(Exception):

    def __init__(self, message):
        self.message = message
        self.status = True


class TooOldException(Exception):

    def __init__(self, age, message):
        self.age = age


class TooYoungException(Exception):

    def __init__(self, age, message):
        self.age = age

#
# class Matrimony:
#
#     def __init__(self, age, gender):
#         if age<21 and gender=="M":
#             raise TooYoungException(age, "you are to young to register")
#         if age<18 and gender=="F":
#             raise TooYoungException(age, "you are to young to register")
#         if age>60:
#             raise TooOldException(age, "We don't have suitable matches for you")
#         self.age = age
#         self.gender = gender
#
#
#     def save_multiple(self, multiples):
#         pass
#
# user1 = Matrimony(age=20,gender="M")


try:
    try:
        print("**")
        try:
            pass
        except IndexError:
            print("7")
    except StopIteration:
        pass
except:
    try:
        pass
    except:
        pass
    else:pass
else:
    try:pass
    except: pass
    finally:pass
finally:
    try:pass
    except: pass
    else: pass
    finally:pass
