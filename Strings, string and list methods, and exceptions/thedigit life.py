print("enter you Birthdau date please:")

BDay= int(input("Day of birth: "))
if BDay <=0 or BDay >31 or BDay == "":
    print("Invalid date")
    
BMonth= int(input("Month of birth: "))
if BMonth <= 0 or BMonth >12 or BMonth == "":
    print("invalide Month")
    
BYear= int(input("Year of birth: "))
if BYear <=0 or BYear < 1900 or BYear == "":
    print("invalide year: ")

BD = str(BDay) + str(BMonth) + str(BYear)

count = 0
count1= 0
for n in BD:
    count = int(n) + count
strcount = str(count)
for c in strcount:
    count1 = int(c) + count1
print(count1)

        