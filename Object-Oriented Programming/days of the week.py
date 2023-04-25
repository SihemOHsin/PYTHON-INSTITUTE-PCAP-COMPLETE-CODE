﻿class WeekDayError(Exception):
    pass
	

class Weeker:
    __week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        try:
            self.__cuurentDay = self.__week.index(day)
        except ValueError:
            raise WeekDayError

    def __str__(self):
        return Weeker.__week[self.__cuurentDay]

    def add_days(self, n):
        self.__cuurentDay = (self.__cuurentDay + n)%7

    def subtract_days(self, n):
        self.__cuurentDay = (self.__cuurentDay - n)%7

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
