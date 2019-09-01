#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This program is designed to manage drug dispensal in hospitals/pharmacies, but can be readily modified to accomodate a wide array of different business models.
# © xMA3STRO 2019

import numpy as np
import pandas as pd

class PharmARC:
    def __init__(self, price, stock):
        self.price = price
        self.stock = stock


# In[2]:


# Insert data as comma-separated-values [Medicine Name, Price Per Unit, Avaliable Stock], save as mdimport.txt.
# Missing data values will be displayed as NaN and will not impact data analysis.
# Prices and stock avaliability have been randomised in this example.

df = pd.read_csv("mdimport.csv", na_values = [' '])
df.columns = ['Medicine', 'Price/Unit', 'Stock']


# In[ ]:


while True:
    
    med = input("Please insert the name of the medicine you would like to purchase, or type 'LIST' for a directory of avaliable medicines:")
    med = med.capitalize()

    if df.Medicine.isin([med]).any():
        a = df.loc[df['Medicine'] == med]['Price/Unit']
        b = df.loc[df['Medicine'] == med]['Stock']
        print(df[df.eq(med).any(1)])
        c = input(f"There are currently {int(b)} units of {med} avaliable at £{int(a)}/unit, how many would you like to purchase?")
        
        while True:
            
            try:
                
                int(c)
                if int(c) <= int(b):
                    x = (int(c)*int(a))/100
                    x = "{:.2f}".format(x)
                    d = input(f"This will cost £{x}, proceed with this transaction? (Enter Y to accept, or any other key to cancel the transaction)")
                    d = d.capitalize()
                    
                    try:
                        
                        if d == "Y":                                       
                            df.loc[df['Medicine'] == med,'Stock'] = (int(b) - int(c))
                            print(f"Successfully purchased {c} unit(s) of {med}, {int(b) - int(c)} units remaining, the database has been updated.")
                            print(f"Returning to main menu, please wait...")
                            break
                            continue
                        else:
                            print("Cancelling transaction, please wait...")
                            break
                            continue
                    except NameError:
                        print("Cancelling transaction, please wait...")
                        break
                        continue
                            
                elif int(c) > int(b):
                    c = input(f"ERROR: Please input a numerical value less than or equal to {int(b)} units:")
                    continue
            except ValueError:
                print (f"ERROR: Please input a numerical value when selecting unit quantity.")
                break
                continue
            
    elif med == "List":     
        print("List of medicine currently listed within the directory:")
        print(df.Medicine.unique())
        continue

    else:
        print ("ERROR: Please insert the name of the medicine you would like to purchase (type LIST for a list of avaliable medicines):")
        continue


# In[ ]:




