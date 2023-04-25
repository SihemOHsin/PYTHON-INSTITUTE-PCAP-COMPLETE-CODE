text = input("enter a text: ")
text = text.upper()
#if text == text[::-1] and text !="":
    #print("it's a palindrome" ) 
#else: 
    #print("it's not a palindrome" ) 
    
newtext=""
for i in text:
    newtext = i + newtext
if (newtext == text):
    print("it's a palindrome" ) 
else: 
    print("it's not a palindrome" ) 