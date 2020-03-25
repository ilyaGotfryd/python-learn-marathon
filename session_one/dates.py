"""
In this section we will explore a subset of Python's date time capabilities
Using https://howchoo.com/g/ywi5m2vkodk/working-with-datetime-objects-and-timezones-in-python
for reference
Print:
https://www.programiz.com/python-programming/datetime/strftime
"""
from datetime import datetime, timedelta
# crate datetime
first_date = datetime(2020, 3, 20, 15, 25,37, 123456)
print(first_date)
# now
now = datetime.now()
print(now)
utcnow = datetime.utcnow()
print(utcnow)

# time delta and time math
an_hour_from_now = datetime.now() + timedelta(hours=1)
print(f"An hour from now is {an_hour_from_now}")

# replace elements to look at start and end of periods
current_hour = datetime.now().replace(minute=0, second=0, microsecond=0)
print(f"Current Hour is {current_hour}")

next_day_same_hour = datetime.now().replace(minute=0, second=0, microsecond=0) + timedelta(days=1)
print(next_day_same_hour)

check_date = datetime.now() + timedelta(hours=36)

now = datetime.now()
day_start = now.replace(hour = 0, minute=0, second=0, microsecond=0)
day_end = day_start + timedelta(days=1, seconds=-1)
print(f"Day Start {day_start}, Day End {day_end}")
print(f"{check_date} is {'' if check_date<=day_end and check_date >= day_start else 'NOT'} today")

# print
print("=========== DATE FORMAT ==============")
print(check_date.strftime("%m/%d/%Y %H:%M:%S"))
print(check_date.strftime("%b %d, %Y"))

# parse
from dateutil.parser import parse
from dateutil.tz import gettz

test_date = parse("March 05 10:25PM")
print(test_date)
test_date = parse("20/11/2011 23:50")
print(test_date)

# timezone and localization, possibly try replacing TZ with LA tz and look at the time

tzinfos = {"BRST": -7200, "CST": gettz("America/Chicago")}
tz_date = parse("2012-01-19 17:21:00 CST", tzinfos=tzinfos)
print(tz_date)
 
# time_diff = datetime.now() - tz_date -can not subtract tz-naive and tz-aware dates

# import failed
# import pytz
# from pytz import timezone
# eastern = timezone('US/Eastern')
# local_date = eastern.localize(datetime.now())
# print(local_date)