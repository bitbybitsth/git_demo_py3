import os
from datetime import datetime
# used to interact with underlying operating system

# get current working directory

current_directory = os.getcwd()
print(current_directory)

# change directory
# os.chdir("D:/3BP3/pycharm/intervierw_assignments")
print(os.getcwd())

# list dirs
print(os.listdir(os.getcwd()))
curret_dirs = os.listdir(os.getcwd())
print(type(curret_dirs))

# creating directories

# single
# os.mkdir("modules_eg")
# os.mkdir("modules_eg/test")
# os.mkdir("modules_eg/test/demo")


# nested
# os.makedirs("demo/test/intro")

########-------------------------
# remove dirs / deleteing directory

# remove single dir
# os.rmdir("modules_eg")

# remove multiple directories
# os.removedirs("demo/test/intro")

# rename a file -----------------

# os.rename("time_module.py", "time_library.py")

# stat = os.stat("date_and_time.py")
# print(stat.st_ctime)
# print(datetime.fromtimestamp(stat.st_ctime))
# print(stat.st_size)
# # print(stat["st_ctime"])
# print(stat)

# environment
env = os.environ
print(env)

print(env.get("APPDATA"))
if "win" in env.get("OS").lower():
    print("welcome windows user")

# os.chdir(env.get("HOMEPATH").replace("\\", "/"))
# os.mkdir("test")

tree = os.walk("D:/3BP3")
print(tree)

for cdir, folders, files in tree:
    if "os_module.py" in files:
        print(f"it is in {cdir}")

# path
print(os.path.isfile("D:/3BP3/pycharm/important_modules/date_and_time.py"))

print(os.path.basename("D:/3BP3/pycharm/important_modules/date_and_time.py"))

print(os.path.dirname("D:/3BP3/pycharm/important_modules/date_and_time.py"))

# s = "D:/3BP3/pycharm/important_modules/date_and_time.py"
# x = s.split("/")
# print(x[-1])
# print("/".join(x[:-1:]))




print(os.path.exists("D:/3BP3/pycharm/important_modules/date_a_time.py"))


path_join = os.path.join(os.getcwd(), "test.py")
print(path_join)

