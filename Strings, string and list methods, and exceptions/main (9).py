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
    digit_list = list(digit)
    pattern = ''
    for i in range(len(digit_list)):
        
        if int(digit_list[i]) == ListPattern.index([i]):
            pattern+=ListPattern[digit_list[i]]
            
    return pattern
print(sevenDisplayDigit(9))

        
    
