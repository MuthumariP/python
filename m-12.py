N=int(input("NUMBER="))
t=N
rev=0
while N>0:
   rem=N%10
   rev=rev*10+rem
   N=N//10
if(t==rev):
   print("polindrome")
else:
   print("not a polindrome")
