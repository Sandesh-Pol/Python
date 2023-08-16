# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 16:13:36 2023

@author: Sandesh Pol
"""

milDis = 2052

days = 6

stop = 2

totalStop = days * stop

disKm = milDis * 1.60934

_1daydist = disKm / days

res  = _1daydist / stop

print(res) 
