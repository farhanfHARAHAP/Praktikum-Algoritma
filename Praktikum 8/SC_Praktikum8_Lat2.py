# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 16:03:22 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""

def positif(x,y):
    if y <= 1:
        return x
    else:
        return positif(x,y-1) * positif(x,1)
    
def negatif(x,y):
    b = abs(y)
    hasil = float(1/positif(x,b))
    return hasil 

def tentukan(x,y):      
    if y == 0:
        return 1
    elif x == 0:
        return 0
    elif y > 0:
        if x > 0:
            return positif(x,y)
        elif x < 0:
            return -abs(positif(x,y))
    elif y < 0:
        if x > 0:
            return negatif(x,y)
        elif x < 0:
            return -abs(negatif(x,y))

while True:
    try:        
        angka = int(input('Masukkan bilangan: '))
        pangkat = int(input('Masukkan pangkat: '))
    except ValueError:
        print('Masukkan angka bulat!')
    else:
        print('Hasilnya yaitu',tentukan(angka,pangkat))
        print('==============================================')
