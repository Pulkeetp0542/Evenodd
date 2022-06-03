a=int(input("Enter the Number"))
if a>1:
    for x in range(2,a):
        if(a%x==0):
            print("Number is Not Prime")
            break
        else:
            print("Number is Prime")
            break
else:
    print("Number is Prime")
