#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      USER
#
# Created:     21-09-2023
# Copyright:   (c) USER 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
ch=input("ch: ")
if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    print("Aplhabets")
elif((ch >= '0' and ch<='9')):
    print("Digit")
else:
    print("Not an alphabet nor digit")



    nb: or can use ch.isdigit  ch.isnumeric