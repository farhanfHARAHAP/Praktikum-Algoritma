# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 11:20:47 2021

@author: HP
"""

# Buatlah sebuah program yang mencetak hasil dari fungsi faktorial
# dengan menggunakan fungsi rekursif.

def cek(x):
    if x == 0:
        return 1
    elif x < 0:
        return 'INVALID'
    else:
        return fungsi(x)

def fungsi(x):
    if x == 1:
        return x
    else:
        return x*fungsi(x-1) # Rekursif
    
def skip():
    for i in range(100):
        print()

print('Created by Farhan Fadillah Harahap')
while True:
    try:
        input('PRESS ENTER')
        skip()
        mulai = int(input('Masukkan Bilangan: '))
        print('Faktorial', mulai, 'adalah', cek(mulai))
    except ValueError:
        print('INVALID INPUT!')
