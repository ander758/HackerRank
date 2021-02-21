import calendar

"""
https://www.hackerrank.com/challenges/python-time-delta/problem
github.com/ander758/HackerRank

Print the absolute difference (t1 - t2) in seconds.
"""

import re
import datetime
from time import strptime


# Complete the time_delta function below.
def get_datetime(str):
    """
    :param str:E.g. 'Sun 10 May 2015 13:54:36 -0700'
    :return: datetime object with timezone
    """
    ls = str.split(' ')
    dd, mm, yy = ls[1], strptime(ls[2], '%b').tm_mon, ls[3]
    HH, MM, SS = ls[4][:2], ls[4][3:5], ls[4][6:9]
    tz_sign, tz_hours, tz_minutes = re.match('([+\-]?)(\d{2})(\d{2})', ls[5]).groups()
    tz_sign = -1 if tz_sign == '-' else 1
    tz_hours, tz_minutes = int(tz_hours), int(tz_minutes)
    tzinfo = datetime.timezone(tz_sign * datetime.timedelta(hours=tz_hours, minutes=tz_minutes))
    return datetime.datetime(year=int(yy), month=int(mm), day=int(dd), hour=int(HH), minute=int(MM), second=int(SS), tzinfo=tzinfo)


def time_delta(t1, t2):
    return round((get_datetime(t1) - get_datetime(t2)).total_seconds())
    # first = datetime.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    # second = datetime.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    # return str(abs(int((first - second).total_seconds())))


if __name__ == '__main__':

    t = 2
    times = ['Sun 10 May 2015 13:54:36 -0700',
             'Sun 10 May 2015 13:54:36 -0000',
             'Sat 02 May 2015 19:54:36 +0530',
             'Fri 01 May 2015 13:54:36 -0000']

    for i in range(0, len(times), t):  # Iterate times and t-items a time
        for j in range(i, i + 1):
            print(time_delta(times[j], times[j + 1]))
