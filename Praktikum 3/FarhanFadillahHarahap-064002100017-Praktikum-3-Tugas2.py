# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:00:43 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""
# Rumus akar2 persamaaan kuadrat:
# ax2 + bx + c = 0

# Rumus determinan:
# D = b2 - 4 a.c

# Rumus x1,x2:
# x1,x2 = -b +- akar(b^2-4ac)/2a
# a. D > 0, merupakan bilangan riil x1 != x2
# b. D = 0, akar kembar x1 == x2
# c. D < 0, tidak memiliki akar riil

# bismillah

from math import sqrt as akar

#Di loop ajehh
ulang = True
while ulang == True:
    for i in range(100):
        print()

    #1. Input data ke rumus
    
    x,y,z = input('''
            Masukkan angka untuk (a,b,c):
             ax2 + bx + c = 0 dengan a bukan 0
             
            >> ''').split(',')
    a=float(x)
    b=float(y)
    c=float(z)
    
    print (('''
            Diketahui.
            %sX^2 + %sX + %s = 0''')%(x,y,z))
    
    # 2. Cari nilai determinan
    
    if a == 0:
        print(('''
             a. Determinan: INVALID'''))
    else:
        determinan = ((b**2)-(4*a*c))
        print(('''
             a. Determinan: %s''')% determinan)
    
    # 3. rumus abc
    x1 = float()
    x2 = float()
    
    def tidakriil():
        global x1
        global x2
        
        k = -b 
        l = ((b**2)-(4*a*c))
        m = (2*a)
        x1 = str((' %s + √%s / %s')%(k,l,m))
        x2 = str((' %s + √%s / %s')%(k,l,m))
        
    def xsama():
        global x1
        global x2
        
        abc = (-b +- akar((b**2)-(4*a*c)))/(2*a)
        x1 =  "{:.2f}".format(abc)
        x2 = x1
    
    def xbeda():
        global x1
        global x2
        
        k = -b 
        l = ((b**2)-(4*a*c))
        akarl = akar(l)
        m = (2*a)
        che = (k + akarl)/m
        cho = (k - akarl)/m
        x1 = "{:.2f}".format(che)
        x2 = "{:.2f}".format(cho)
    
    if a == 0:
        print(('''
            b. INVALID
               x1 = INVALID
               x2 = INVALID'''))
        input('PRESS ENTER')
    else:    
        if determinan == 0:
            xsama()
            jenis = 'Akar Sama'
        elif determinan < 0:
            tidakriil(); 
            jenis = 'Akar Tidak riil / Imaginer'
        elif determinan > 0:
            xbeda()
            jenis = 'Akar Beda'
        else:
            exit()
            
        print(('''
                b. %s
                   x1 = %s
                   x2 = %s''')%(jenis,x1,x2))
        input('PRESS ENTER')
