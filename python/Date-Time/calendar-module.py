import calendar
"""
https://www.hackerrank.com/challenges/calendar-module/problem
github.com/ander758/HackerRank

You are given a date. Your task is to find what the day is on that date.
"""


input_list = list(map(int, '08 05 2015'.split(' ')))
mm, dd, yy = input_list[0], input_list[1], input_list[2]
print(calendar.day_name[calendar.weekday(year=yy, month=mm, day=dd)].upper())
