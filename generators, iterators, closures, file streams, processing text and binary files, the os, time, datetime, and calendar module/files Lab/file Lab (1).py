from os import strerror

srcname = input("Enter the source file name: ")
try:
    f = open(srcname, 'r')
    
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
    exit()

cnt = 0    
content = f.read()

for ch in content:
    #if ch.isalpha()== True:
    cnt += 1
    print(ch.lower(),'-->' , cnt)
f.close()
    

