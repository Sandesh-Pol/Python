# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 20:33:26 2023

@author: Sandesh Gajendra Pol
"""

import pandas as pd

import numpy as np

cars_data = pd.read_csv('Toyota.csv')

"""
cars_data = pd.read_csv('Toyota.csv',index_col=0)

print(cars_data.index)  # give index

print(cars_data.columns)

print(cars_data.size)

print(cars_data.memory_usage)

print(cars_data.ndim)  # dmonstion

cars_data.head(6)



"""
#a = cars_data.at[4,'FuelType']

#b = cars_data.iat[5,6]

#print(a,b)



#print(cars_data.dtypes)



#cars_data.info()

#print(np.unique(cars_data['HP']))


# cars_data['MetColor'] = cars_data['MetColor'].astype('object')


print(np.unique(cars_data['Doors']))

# to repalce it we use 

cars_data['Doors'].replace('three','3',inplace = True)

cars_data['Doors'].replace('four','4',inplace = True)

cars_data['Doors'].replace('five','5',inplace = True)


cars_data['Doors'] = cars_data['Doors'].astype('int64')

print(np.unique(cars_data['Doors']))












