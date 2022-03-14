#armstrong number
n=int(input("Enter the digit:"))
s=0
m=n
order=len(str(n))
while n>0:
    r=n%10
    s=r**order+s
    n=n//10
if s==m:
    print("Number is Armstrong.")
else:
    print("Number is not Armstrong.")
input()          
