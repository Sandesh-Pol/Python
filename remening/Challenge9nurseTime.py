# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 23:56:09 2023

@author: Sandesh Pol
"""

hr = [8,10,9,8,7,12]

for i in range(len(hr)):
    hr[i] = hr[i] * 60
    
    
total_sum = sum(hr)

average = total_sum / len(hr)

print(average/60)