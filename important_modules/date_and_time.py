import datetime
from datetime import date, time, timedelta


# dt = date.today()
# print(dt)
#
# back_date = date(year=2020, month=2, day=29)
# print(back_date)
#
# print(back_date.strftime("%y/%m/%d"))
#
# back_date.replace(month=6)
#
# print(date.max)
# print(date.min)
#
# now = date.today()
#
# print(now.weekday()) # Mon starts week
# print(now.isoweekday()) # sunday starts week


# ti = time(10,10,10)
# print(ti)

our_min = "9:00:00:PM"
our_max = "11:59:59:PM"

def create_time(hours, minute, second):
    d = our_min.split(":")
    if hours < d[0] and d[-1]=="AM":
        return "False"

    if minute>59 or minute<0:
        return False
    t = time(hour=hours,minute=minute, second=second)

d_now = datetime.datetime.today()
c_now = datetime.datetime(2021,5,24,7)

print(d_now)
print(c_now)

if d_now > c_now:
    print("true")

sum_now = d_now - c_now
print(type(d_now))
print(type(c_now))
print(type(sum_now))
print(sum_now)

token_gen_dt = datetime.datetime.now()
valid_dt = token_gen_dt + timedelta(seconds=3)
def share_resources():
    global valid_dt
    if datetime.datetime.now() < valid_dt:
        print("giving data")
        return True
    else:
        print("get new token")
        return False

#
# print(token_gen_dt)
# print(valid_dt)


while True:
    x = share_resources()
    if not x:
        break
