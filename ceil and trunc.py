#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      USER
#
# Created:     27-09-2023
# Copyright:   (c) USER 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
num= float(input("num: "))
if num-int(num)>=0.5:
    print("result:",math.ceil(num))
    print("result:",math.trunc(num))