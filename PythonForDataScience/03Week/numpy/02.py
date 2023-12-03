# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:14:33 2023

@author: Sandesh Pol
"""
'''
import pandas as pd

# crosstab is used to get frequency


cars_data = pd.read_csv('Toyota.csv')

cd = cars_data.copy()
'''

'''
pd.crosstab(index=cd['FuelType'],columns='count',dropna=True)


a = pd.crosstab( index = cd['Automatic'], columns = cd['FuelType'], dropna = True)


print(a)
'''


# joint probabiliry for that normalize is used


'''

b = pd.crosstab(index = cd['Automatic'], columns = cd['FuelType'],dropna=True,normalize=True)

print(b)

'''
'''
# marginal probabiliry for that normalize is used




d = pd.crosstab(index = cd['Automatic'], columns = cd['FuelType'],dropna=True,normalize=True,margins=True)

print(d)
'''


'''
# conditional probabiliry for that normalize is used

e = pd.crosstab(index = cd['Automatic'], columns = cd['FuelType'],dropna=True,normalize='index',margins=True)

print(e)

'''
'''
f = pd.crosstab(index = cd['Automatic'], columns = cd['FuelType'],dropna=True,normalize='index',margins=True)

print(f)

'''
'''
import pandas as pd


cars_data = pd.read_csv('Toyota.csv')

cd = cars_data.copy()


corr_matrix = cd.corr(method='pearson')

numerical_data = cd.select_dtypes(include=[object])


corr_matrix = numerical_data.corr()

print(corr_matrix)
<<<<<<< HEAD
'''

x = True
y = 6
if not x:
    print("ok")
else:
    print("not ok")
=======

'''




>>>>>>> 0b9e251ca57be5caf6464ca1a56242950904fb13



