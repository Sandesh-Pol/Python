# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 20:33:26 2023

@author: Sandesh Gajendra Pol
"""

import pandas as pd

cars_data = pd.read_csv('Toyota.csv',index_col=0)

"""
cars_data = pd.read_csv('Toyota.csv',index_col=0)

print(cars_data.index)  # give index

print(cars_data.columns)

print(cars_data.size)

print(cars_data.memory_usage)

print(cars_data.ndim)  # dmonstion

cars_data.head(6)



"""
a = cars_data.at[4,'FuelType']

b = cars_data.iat[5,6]

print(a,b)







