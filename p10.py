a=int(input("enter number"))
if(a%2==0):
    print("number is even")
else:
    print("number is odd")  


a=int(input("enter day"))      
if(a==366):
    print("leap year")
else:
    print("not leap year")


a=(input("the married drivers enter y/n"))  
if(a=='y'):
    print("you are insured" ) 
else: 
    b=int(input("enter your age if male"))       
    if(a=='n'and b>30):
        print("you are insured")
    else:    
        c=int(input("enter your age if female(if not female enter 1)"))    
    if(a=='n' and c>25):
        print("you are insured")
    else:
        print("you are not insured")    
