# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:41:13 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""
import math
from math import sqrt as akar

hal=True

input('''
      ================================
      
      Cek jenis segitigamu! Ada 4 jenis
      segitiga, yaitu:
          
          1. Sama Sisi
          2. Sama Kaki
          3. Siku-siku
          4. Sembarang
      
        ================================
                 PRESS ENTER''')
while(hal==True):      
    for i in range(100):
        print()
    x,y,z = input('''
                  Masukkan ketiga sisi! (a,b,c)
                  >> ''').split(",")
                  
    a = int(x)
    b = int(y)
    c = int(z)
    
    
    if (a == b == c):
        print('Ini Segitiga Sama Sisi!')
    elif (a+b <=c) or (a+c<=b) or (b+c<=a):
        print('BUKAN SEGITIGA SAMASEKALI!')
    elif (a==b) or (a==c) or (b==c):
        print('Ini Segitiga Sama Kaki!')
    elif (a == akar((b*b)+(c*c))) or (b == akar((c*c)+(a*a))) or (c == akar((b*b)+(a*a))):
        print('Ini Segitiga Siku-siku')
    else:
        print('\n\nIni Segitiga Sembarang')
    input('Press ENTER!')
    

              
