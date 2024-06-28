# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 20:33:26 2023

@author: Sandesh Gajendra Pol
"""


import pandas as pd

cars_data = pd.read_csv('Toyota.csv')

cd = cars_data.copy()
'''
cd.insert(10, "Price_Class", "")
cd.insert(11, "Age_Converter", 0)
cd.insert(12, 'Km_Per_Month', 0)

def c_convert(val1, val2):
    val1_numeric = pd.to_numeric(val1, errors='coerce')  # Convert 'Age' column to numeric
    val2_numeric = pd.to_numeric(val2, errors='coerce')  # Convert 'KM' column to numeric
    
    val_converter = val1_numeric / 12
    ratio = val2_numeric / val1_numeric
    
    return [val_converter, ratio]

cd["Age_Converter"], cd["Km_Per_Month"] = c_convert(cd["Age"], cd["KM"])

print(cd)



'''


'''
# function

cd.insert(11,"Age_Converter",0)

def converter(val):
    res = val/12
    return res


cd['Age_Converter'] = converter(cd['Age'])

cd['Age_Converter'] = round(converter(cd['Age']),1)


print(cd['Age_Converter'])

'''
# looping

'''
cd.insert(10, "Price_Class", "")


for i in range(len(cd['Price'])):
    if cd['Price'][i] <= 8450:
        cd.loc[i, 'Price_Class'] = "LOW"
    elif cd['Price'][i] > 11950:
        cd.loc[i, 'Price_Class'] = "HIGH"
    else:
        cd.loc[i, 'Price_Class'] = "MID"


a = cd['Price_Class'].value_counts()


print(a)

'''



"""
cars_data = pd.read_csv('Toyota.csv',index_col=0)

print(cars_data.index)  # give index

print(cars_data.columns)

print(cars_data.size)

print(cars_data.memory_usage)

print(cars_data.ndim)  # dmonstion

cars_data.head(6)



"""

"""
a = cars_data.at[4,'FuelType']

b = cars_data.iat[5,6]

print(a,b)



print(cars_data.dtypes)



cars_data.info()

print(np.unique(cars_data['HP']))


cars_data['MetColor'] = cars_data['MetColor'].astype('object')


print(np.unique(cars_data['Doors']))

to repalce it we use 
"""



"""cars_data['Doors'].replace('three','3',inplace = True)

cars_data['Doors'].replace('four','4',inplace = True)

cars_data['Doors'].replace('five','5',inplace = True)


cars_data['Doors'] = cars_data['Doors'].astype('int64')

print(np.unique(cars_data['Doors']))

"""















