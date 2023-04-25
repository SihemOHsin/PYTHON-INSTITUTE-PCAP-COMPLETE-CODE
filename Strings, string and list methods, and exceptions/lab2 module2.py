ListPattern =[
"###\n"+("# #\n"*3)+"###",
"#\n"*5,
"###\n  #\n###\n# \n###",
"###\n  #\n###\n  #\n###",
"# #\n# #\n###\n  #\n  #",
"###\n#  \n###\n  #\n###",
"###\n#  \n###\n# #\n###",
"###\n"+("  #\n")*4,
("###\n"+"# #\n")*2+"###",
"###\n# #\n###\n  #\n###"
]

def sevenDisplayDigit(digit):
    digit= abs(digit)
    digit = str(digit)
    digitlist = list(digit)
    pattern = ''
    
    for i in digitlist:
        print(i)
        i =int(i)
        pattern += ListPattern[i]+"\n\n"
    
    return pattern
print(sevenDisplayDigit(986))