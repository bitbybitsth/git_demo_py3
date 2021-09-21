# import logging
#
# try:
#     x = 10/1
#     f = open("exception_handling_intro.py")
#     print(f.read())
#     print(next(f))
# except (ZeroDivisionError, FileNotFoundError, StopIteration, Exception) as e:
#     # logging.CRITICAL("error", e)
#     print(e.__class__)

data = {"today": "Friday", "date": "25"}

def function():
    # print(data["today"])
    f = open("kkkk.txt")
    print(f.read())
    # print(next(f))
    # print(10+"10")
    # print(10/0)
    x = [2,3,4]
    print(x[5])


# try:
#     function()
# except KeyError as ke:
#     print(ke.__doc__)
#     data["month"]= "jun"
#     print(data)
# except IndexError:
#     print("overflow")
# except ZeroDivisionError as ze:
#     print("you cannot divide a number by zero")
# except FileNotFoundError:
#     print("no file exists with the name")
# except StopIteration:
#     print("file content is already displayed")
# except TypeError:
#     print("you cannot add to objets of different type except float an int")
# except Exception as e:
#     print(e.__class__)


try:
    function()
except (KeyError, IndexError, ZeroDivisionError, FileNotFoundError,StopIteration,TypeError) as ke:
    print(ke.__doc__)
    data["month"]= "jun"
    print(data)
# except IndexError:
#     print("overflow")
# except ZeroDivisionError as ze:
#     print("you cannot divide a number by zero")
# except FileNotFoundError:
#     print("no file exists with the name")
# except StopIteration:
#     print("file content is already displayed")
# except TypeError:
#     print("you cannot add to objets of different type except float an int")
# # except Exception as e:
#     print(e.__class__)

# #
# try:
#     function()
# except (KeyError, IndexError) as ke:
#     print("Sorry we don't have that infpormation with us")
# except (ZeroDivisionError, TypeError) as ze:
#     print("Invalid arithmetic operation")
# except (FileNotFoundError, StopIteration):
#     print("Some invalid opeartion with file")
# except Exception as e:
#     print(e.__class__)


# try:
#     pass
# except:
#     pass

# try:
#     pass
# except:
#     pass
# else:
#     pass


# try:
#     pass
# except:
#     pass
# else:
#     pass
# finally:
#     pass

# try:
#     pass
# # except:
# #     pass
# # finally:
# #     pass
# f = open("kkk.txt")
#
# try:
#     line = f.readline()
#     print(10+int(line))
# except (StopIteration, TypeError, ValueError):
#     print("6")
# finally:
#     f.close()
#
# print("is file closed", f.closed)


try:
    f = open("kkk.txt")
    line1 = f.readline()
    lin2 = f.readline()
    # print(next(f))
except (FileNotFoundError, StopIteration, ValueError):
    print("****")
else:
    print("####")
    print(int(line1) + int(lin2))
finally:
    f.close()





