# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 16:43:07 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""
def convert(list):
    x = sum(d * 10**i for i, d in enumerate(list[::-1]))
    return x

def tentukan2(x):
    if x == 2:
        return 'nd'
    elif x == 3:
        return 'rd'
    elif x == 1:
        return 'st'
    else:
        return 'th'
    
def tentukan1(x):
    res = [int(x) for x in str(angka)]
    if len(res) >= 2:
        akhir2 = list()
        akhir2.append(res[-2])
        akhir2.append(res[-1])
        che = convert(akhir2)
        if che == 11 or che == 12 or che == 13:
            return 'th'
        else:
            return tentukan2(res[-1])
    else:
        return tentukan2(x)


while True:    
    try:  
        print()
        angka = int(input('Masukkan angka: '))
    except ValueError:
        print('INVALID')
    else:
        hasil = tentukan1(angka)
        print(str(angka)+hasil)
