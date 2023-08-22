# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 22:28:52 2023

@author: Sandesh Gajendra Pol
"""

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np



cars_data = pd.read_csv('Toyota.csv',index_col=0,na_values=["??","????"])

cars_data.dropna(axis = 0,inplace = True)


plt.scatter(cars_data['Age'], cars_data['Price'], c = 'red')

plt.title("Scarretered ploat of Price vs Age of the cars")

plt.xlabel('Age(months)')

plt.ylabel('Price (Euros)')

plt.show()



plt.hist(cars_data['KM'], color='green',edgecolor = 'white', bins= 5)

plt.xlabel('Kilometer')

plt.ylabel("Frequency")

plt.show()




counts = [979, 120, 12] 

fuelType = ('Petrol', 'Diesel', 'CNG')

index = np.arange(len(fuelType))


plt.bar(index, counts, color=['red', 'blue', 'cyan'])

plt.title('Bar plot of fuel types')

plt.xlabel('Fuel Types')

plt.ylabel('Frequency')

plt.xticks(index, fuelType, rotation = 90) 

plt.show()






