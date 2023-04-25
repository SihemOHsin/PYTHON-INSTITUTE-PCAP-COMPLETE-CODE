from calendar import Calendar

class MyCalendar(Calendar):
    def count_weekday_in_year(self, year, weekday):
        count = 0
        for month in range(1, 13):
            for _, wd in self.itermonthdays2(year, month):
                if _!=0 and wd == weekday:
                    count += 1
        return count

cal = MyCalendar()
print(cal.count_weekday_in_year(2019, 0)) # 52
