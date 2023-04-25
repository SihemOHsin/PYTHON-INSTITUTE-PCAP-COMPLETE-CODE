
text = input("print a text : ")
text = text.upper()

text1 = input("print a text1 : ")
text1 = text.upper()
#if sorted(text) == sorted(text1) :

count = count1 = 0

for char in text:
    count += ord(char)
for char1 in text1:
    count1 += ord(char1)
if count == count1:
    print("anagram" ) 
else: 
    print("not anagram" ) 