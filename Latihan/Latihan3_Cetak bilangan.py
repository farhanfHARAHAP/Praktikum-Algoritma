# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:23:43 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""

#Bismillah
x = True

while x==True:
    greater = []
    lower = []
    hasil = []
    for i in range(100):
        print()
    bil = int(input('Masukkan angka bebas: '))
    bila,bilb = bil,bil
    #greater.append(bil)
    #lower.append(bil)
    
    for i in range(9):
        bila += 1
        greater.append(bila)
    for i in range(9):
        bilb -= 1
        lower.append(bilb)
    lower.reverse()
    
    print()#greater
    print ('==========================>')
    print (bil,end=' ')
    for n in greater:
        print (n,end=' ')
        
    print()#lower
    print ('<==========================')
    for n in lower:
        print (n,end=' ')
    print (bil,end=' ')
    
    print()#all
    print ('<=====================================================>')
    for n in lower:
        print (n,end=' ')
    print (bil,end=' ')
    for n in greater:
        print (n,end=' ')
    opt = input('''
          
          PRESS ENTER atau Ketik n untuk keluar
          >>> ''')
    if opt == 'n':
        x = False
    
