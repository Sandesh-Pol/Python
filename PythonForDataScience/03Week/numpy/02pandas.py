# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 19:53:18 2023

@author: Sandesh Gajendra Pol
"""

import pandas as pd
import numpy as np


ser = pd.Series()
print("Pandas Series: ", ser)


data = np.array(['g', 'e', 'e', 'k', 's'])
	
ser = pd.Series(data)
print("Pandas Series:\n", ser)

	

df = pd.DataFrame()
print(df)


lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
	

df = pd.DataFrame(lst)
print(df)
