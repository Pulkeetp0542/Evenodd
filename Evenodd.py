a=int(input("Enter"))
if a>1:
    for x in range(2,a):
        if(a%x==0):
            print("Not Prime")
            break
        else:
            print("Prime")
            break
else:
    print("Prime")
