# Caesar cipher second scenario

text = input("Enter your message: ")
try:
    shift = int(input("Enter a number: "))
except:
    print("Enter an integer!")
if text != "" and shift <26 and shift >0:
    cipher = ''
    for char in text:
        ordre = ord(char)
        if char== " " or char.isdigit():
            code = ordre
        else :
            code = ordre + shift
        if code > ord('Z') and ordre >=65 and ordre < 91 :
            code = ord('A')
        if code > ord('z') and ordre >=97 and ordre <= 122:
            code = ord('a')
        cipher += chr(code)

    print(cipher)
else:
    print("We don't accept empty messages and shift inferieur a zero et plus de 25: ")
