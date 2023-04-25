def read_int(prompt, min, max):
    #
    # Write your code here.
        
    try:  
        value = int(input(prompt))
        if (value <= min and value >= max):
            assert value!= None
            return value
            
            
    except ValueError:
        print("Error: Wrong Input")
        
    except:
        print("Error: The value is not within range(" + str(min) + ".." + str(max) + ")")
        
    
v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
