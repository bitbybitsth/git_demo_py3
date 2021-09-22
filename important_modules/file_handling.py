# file_ob = open("test.txt", 'w')
# file_ob.write("test")
# file_ob.close()
#
# file_ob1 = open("test.txt")
# print(file_ob1.read())
# file_ob1.close()

# with open("test.txt", "w") as file_ob:
#     file_ob.write("test")
#
# with open("test.txt") as file_ob1:
#     print(file_ob1.read())
#     # file_ob1.write("5")


# mode r (read only mode) - opens file in readonly mode, if does not exists error is thrown FileNotFoundError.
# pointer is placed at the beginning of the file. this is the default mode of file opening.
#
# with open("team_india.txt") as rf:
#     openener_1 = rf.readline()
#     openener_2 = rf.readline()
#     print(openener_1)
#     print(openener_2)
#     others = rf.readlines()
#     for player in others:
#         pass
#     print(others)
#     # rf.write("test")
#     print(rf.read())
#
# # mode w (write only mode), opens file for writing, if file does not exists creates the file, pointer is at the starting of the file
# with open("new team.txt", "w") as f:
#     f.write("New team for Test World championship\n")
#     x = ["kohli\n", "rohit\n", "shikhar\n"]
#     f.writelines(x)
#     # f.read()
#
# with open("team_india.txt") as rf:
#     with open("new team.txt", "w") as wf:
#         data = rf.read()
#         wf.write(data)

# mode  w+  r+, opens file in read and write mode , pointer is placed at start
import tempfile

count = 0
with open("team_india.txt", "r") as rwf:
    with open("team_india.txt", "w") as wf:
        for _ in range(1, 10):
            line = rwf.readline()
            line = line.upper()
            wf.write(line)

# a = opne sthe file in append mode, pointer is placed at the end of the file.
with open("new team.txt", "a") as af:
    af.writelines("Final team scheduled\n")


with open("3b.jpg", "rb") as f:
    with open("test/BBB.jpg", "wb") as wf:
        data = f.read()
        print(type(data))
        print(data)
        wf.write(data)

# with open("sample.pdf", "rb") as rbf:
#     with open("test/sample.pdf", "wb") as wbf:
#         data  =rbf.read()
#         wbf.write(data)
#         print(data)

with tempfile.NamedTemporaryFile(mode="w+") as fileob:
    fileob.write("writing data to a file without opening any file.")
    fileob.seek(1, 0)
    print(fileob.read())
    print(fileob.name)

    ("sample.txt", fileob.read())






















