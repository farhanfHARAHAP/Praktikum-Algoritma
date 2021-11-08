# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 15:06:53 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""

def hasil(x,info):
    if x == True:
        print('adalah bilangan prima')
    else:
        print('bukan bilangan prima',info)
        

def tentukan(x):
    if x == 1 or x == 2 or x == 3:
        hasil(True,0)
    else:
        for i in range (2,x):
            if x%i == 0:
                info = str(f'karena {x//i} x {i} = {x}') 
                hasil(False,info)
                break
            else:
                hasil(True,0)
                break
            
while True:
    try:
        print()
        tentukan(int(input('Masukkan bilangan >> ')))
    except ValueError:
        print()
