# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 23:12:20 2023

@author: Sandesh Pol
"""

red = 5000000

white = 8000

def greatestCommonFactor(w,r):
    return w if(r==0) else greatestCommonFactor(r, w % r)

factor = greatestCommonFactor(white,red)

wR = int(white/factor)

rR = int(red/factor)

print(factor)

print('Aspect Ratio : ',wR,":",rR)



