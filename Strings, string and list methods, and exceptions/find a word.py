text= input("write a text: ")
text2 = input("write a word: ")

def Convert(string):
    list1 = []
    list1[:0] = string
    return list1
    
#print(Convert(text))

list1= Convert(text)
#list2= Convert(text2)
count =0
for i in list1:
    found = text2.find(i)
    while found != -1:
        found = text2.find(i, found+1)
        count +=1
        
if count == len(list1):
    print("Yes")
else:
    print("No")