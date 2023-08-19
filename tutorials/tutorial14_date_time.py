"""
Here we got some new terms related to day and time:
    1, Tick ->> Time intervals which are floating point numbers in units of sec. Particular instance in time is expressed
             in secs since 00:00:00 hrs January 1, 1970(epoch)
    2, Func time.time() returns the current system time in ticks
    3, Time-tuple:

"""
import calendar
import time;    # This is required to include time module.
if __name__ == '__main__':
    ticks = time.time()     # This is the number of ticks since 00:00:00 hrs January 1, 1970(epoch)
    print(ticks)    # 1690649016.220059 (11:42pm Jul 29 2023)/  1690649147.949353 (11:45pm Jul 29 2023)

    # get local time
    local_time = time.localtime()
    print(local_time)   # time.struct_time(tm_year=2023, tm_mon=7, tm_mday=29, tm_hour=23, tm_min=49, tm_sec=9,
    #                     tm_wday=5, tm_yday=210, tm_isdst=0)

    # get formatted time
    local_time = time.asctime()
    print(local_time)   # Sat Jul 29 23:51:10 2023

    # get calendar for a month
    cal = calendar.month(2023, 3)
    print(cal)
    """
        March 2023
    Mo Tu We Th Fr Sa Su
           1  2  3  4  5
     6  7  8  9 10 11 12
    13 14 15 16 17 18 19
    20 21 22 23 24 25 26
    27 28 29 30 31
    """
    time = calendar.firstweekday()
    print(time)



