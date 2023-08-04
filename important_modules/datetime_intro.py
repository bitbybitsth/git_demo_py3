import datetime

# datetime now

dt_now = datetime.datetime.now()
# print(dt_now)
# print(type(dt_now))
# #
# print("Time", dt_now.time())
# print("hour", dt_now.hour)
# print("date", dt_now.date())
# print("day", dt_now.day)
# print("month", dt_now.month)
#
# print("minutes", dt_now.minute)
#
# cust_dt = datetime.datetime(2021,5,15,10,10,10,10)
# cust_dt = datetime.datetime(2021,5,15,10)
# cust_dt = datetime.datetime(minute=45, hour=9, year=2021, day=13, month=4)
# cust_dt = datetime.datetime(month=5, year=2020, day=10)
# #
# print("back dated", cust_dt)
# print(type(cust_dt))
#
# posix/epoch time
# dt_test = datetime.datetime.today()
# print("****", dt_test)
# time_stamp = dt_test.timestamp()
# print("time stamp", time_stamp)
# #
# dt_from_timestamp = datetime.datetime.fromtimestamp(time_stamp)
# print("date from timestamp", dt_from_timestamp)
#
# current date current time
# print("current date", dt_now.date())
# print("current Time", dt_now.time())
# #
# curr_dt = dt_now.date()
# curr_time = dt_now.time()
# print(type(curr_dt))
# print(type(curr_time))
#
# combined datetime
# combined_datetime = datetime.datetime.combine(curr_dt,curr_time)
# print(combined_datetime)
#
# # replace
#
# replaced_dt = combined_datetime.replace(year=2020, day=4)
# print("cusst dt", combined_datetime)
# print("replaced dt", replaced_dt)
#

now = datetime.datetime.now()
# st_dt = str(now)
# print(now)
# print(type(now))
baked_Date = datetime.datetime(2020,8,23,23,10,10)

DT_FORMAT = "%a %d-%b-%y %I:%M:%S %p"

date_to_str = baked_Date.strftime(DT_FORMAT)
dt_to_str = now.strftime(DT_FORMAT)
date_to_str1 = baked_Date.strftime(DT_FORMAT)
dt_to_str1 = now.strftime(DT_FORMAT)
date_to_str2 = baked_Date.strftime(DT_FORMAT)

# dt_to_st2r = now.strftime("%A %d-%b-%y %I:%M:%S %p")
# date_to_str4 = baked_Date.strftime("%A %d-%b-%y %I:%M:%S %p")
# dt_to_str5 = now.strftime("%A %d-%b-%y %I:%M:%S %p")
# date_to_str6 = baked_Date.strftime("%A %d-%b-%y %I:%M:%S %p")
# dt_to_str8 = now.strftime("%A %d-%b-%Y %I:%M:%S %p")
# date_to_str9 = baked_Date.strftime("%A %d-%b-%y %I:%M:%S %p")
# dt_to_str4 = now.strftime("%A %d-%b-%y %I:%M:%S %p")
# date_to_str4f = baked_Date.strftime("%A %d-%b-%y %I:%M:%S %p")
# dt_to_strfgh= now.strftime("%A %d-%b-%y %I:%M:%S %p")
# date_to_strj = baked_Date.strftime("%A %d-%b-%y %I:%M:%S %p")
# dt_to_strk = now.strftime("%A %d-%b-%y %I:%M:%S %p")


print(date_to_str)
print(dt_to_str)
# print(type(date_to_str))


st_dt2 = "2021-5-24 10:10:10"

str_to_dt = datetime.datetime.strptime(st_dt2,"%Y-%m-%d %H:%M:%S")



str_to_dt.date()
str_to_dt.time()
# print(str_to_dt)
# print(type(str_to_dt))