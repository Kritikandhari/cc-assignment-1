n=int(input("Enter no."))
if n<2:
    print("not prime")
elif n==2:
    print("prime")    
else:    
    for i in range(2,int(n/2)+1):
        if n%i==0:
            print("not prime")
            break
        else:
            print(" prime")    
            