# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:35:49 2019

@author: GOGUT
"""

file=r"Y:\ressim\lavani-deep\dg2\simu2\box_cases\Compdat_test.txt"
with open(file) as f:
    data = f.read()
#print(data)
data2=data.replace("0.0000","7.0000")
print(data2)
