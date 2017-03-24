"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""

#Define our months for readability
class Month:
    Jan = 1
    Feb = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    Sept = 9
    October = 10
    Nov = 11
    Dec = 12

#7 is a prime number, thus we will count sunday as day 7 in the week and test if a day is sunday
#by moduling by 7, 1 jan 1901 started on a tuesday so first day is 2
current_day = 2

def days_in_month(start_year, stop_year):
    year = start_year
    month = Month.Jan
    day = 0
    while year < stop_year:
        if month in [Month.Jan, Month.May, Month.March, Month.July, Month.October, Month.Dec, Month.August]:
            yield (year, month, 31)
            day = day + 31
        elif month in [Month.Sept, Month.April, Month.June, Month.Nov]:
            yield (year, month, 30)
            day = day + 30
        elif month == Month.Feb:
            days_in_feb = 28 if year % 4 != 0 else 29
            yield (year, month, days_in_feb)
            day = day + days_in_feb
        if day >= 365:
            year = year + 1
            day = 0
            month = Month.Jan
        else:
            month = month + 1

count = 0
current_day = 2
for (year, month, days) in days_in_month(1901, 2001):
    if current_day % 7 == 0:
        count = count + 1
    current_day = current_day + days
print count