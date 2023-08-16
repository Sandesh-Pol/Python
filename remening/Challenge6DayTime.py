# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 23:34:31 2023

@author: Sandesh

Q. The city bus system carries 1200000 people each day how many people bus dose 

carry per year solve without using oprator


"""

def mul(p,d):
    if(d==0):
        return 0
    
    if(d>0):
        return (p + mul(p, d-1))
    
    if(d<0):
        return -mul(p, -d)

    
    
p = 1200000

d = 365

result = mul(p,d)

print(result)

print(p*d)
    