num=int(input("Enter the number: "))
temp=num
rem,sum=0,0
digit=len(str(num))
while(num!=0):
    rem=num%10
    sum+=rem**digit
    num//=10
if(sum==temp):
    print("armstrong")
else:
    print("not amrstrong")