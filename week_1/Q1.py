str = input("Enter any Word: ")

def diagonal(string):
    space=''
    for charIndex in range(len(string)):
    
        if charIndex==0:
            print(string[charIndex])
        
        else:
            print(space,string[charIndex]) 
            space=space+' '
 
 diagonal(str)
 
