"""
Slicing  - used to slice some part of data from sequence types like string, list and tuple

There are two ways to implement slicing

slice(start,stop,step)
seq_ref[start:stop:step]

start - starting index from where the slice will start, if not given by default it will be zero
stop - stop index for the slice, if not given default value len(seq_ref), and slice will consider 1 index less tha stop.
step - denotes the step value is used to determine the next element to be picked, by default +1
"""

sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
weekdays = tuple((["mon", "tue", "wed", "thu", "fri", "sat", "sun"]))
quote = "your limitation is your imagination"
dt = "2020-04-30T8:30:00Z"
dt_new = "2020-04-30T8:30:00Z"

# print("all seq", sizes[::])
# print("all seq", sizes[:])
# print("start fro 4th index", sizes[4:])
# print("stop at 6th index", sizes[:6])
# print("take 2 steps", sizes[::3])
#
# print("slice", sizes[3:8:2])
# # [8, 32, 128]
# print("slice", quote[5:30:5])
# # print("slice", quote[5:15])
#
# word = quote[5:15]
# print(word)
# # print("slice tuple", weekdays[2:5])
# days = weekdays[2:5]
#
# print(days)


# -------------------------------------------
# negetive indexs

# sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
print(sizes[-1:-5:-1])
print(sizes[-1:-5:-2])

print(sizes[::-1])

print(sizes[-5:8])
print(sizes[-5:-9:-2])

print(sizes[4:-10])

# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
print(len(sizes))
print("_______________________________")
print(sizes[4:8:-2])  # []
print(sizes[-3:5:-1]) # []
print(sizes[-4:10]) # []
print(sizes[5:-5:-1]) # [32, 64], [32,128], []
print(sizes[4:5]) # [16]

# -------------------------------------------

slice_ob = slice(2,8,2)

print("using Slice() ", sizes[slice_ob])

dt = "2020-04-30T8:30:00Z"

date_only = dt[:10]
time_only = dt[11:-1]

print(date_only)
print(time_only)





