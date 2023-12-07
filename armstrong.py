#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      USER
0
#
# Created:     29-09-2023
# Copyright:   (c) USER 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
digits=[]
sum1 = 0
temp=0
number=int((input("n: ")))
temp=number
while(temp!=0):
    digits.append(temp%10)
    temp=temp//10
power = len(digits)
for x in digits:
    sum1 = sum1+x**power
print("sum of powers: ",sum1)
if(sum1==number):
    print("armstrong number")
else:
    print("not an armstrong number")