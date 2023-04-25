from datetime import datetime

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%B %-d,%Y %H:%M:%S"))

print("********")
print(dt.strftime("%Y/%m/%d %H:%M:%S"))
print()
print(dt.strftime("%y/%B/%d %H:%M:%S %p"))
print()
print(dt.strftime("%a, %Y %b %d "))
print()
print(dt.strftime("%A, %Y %B %d "))
print()
print(dt.strftime("weekday: %w "))
print()
print(dt.strftime("day of the year: %j "))
print()
print(dt.strftime("day of the year: %U "))
