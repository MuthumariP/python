s=int(input("s="))
e=int(input("e="))
if(s<=100000)&(e<=100000):
    for y in range(s+1,e):
     if(y%2!=0):
        print(y)

else:
    print("input is invalid")

