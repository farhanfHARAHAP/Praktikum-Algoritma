# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 18:25:11 2021

@author: HP
Nama: Farhan F Harahap
NIM: 064002100017
"""
from IPython.display import Image, display

def skip():
    for i in range(100):
        print()
        
mamalia = str()
karnivora = str()
berenang = str()
x = 1    
 
while x == 1:        
    skip()
    input('''
          Pikirkan antara ayam, bebek, beruang, dan kuda!
          ===============================================
                      >>> PRESS ENTER <<<''')
          
   
    skip()
    mamalia = input('''
                    apakah hewan mamalia?(y/n)
                    >> ''')
    if mamalia =='y':
        skip()
        karnivora = input('''
                     apakah hewan karnivora?(y/n)  
                     >> ''')
        if karnivora =='y':
            skip()
            display(Image(filename='beruang.jpg')) 
            input('''
                  Itu pasti hewan beruang!
                  =========================
                  Press ENTER!''')
        elif karnivora =='n':
            skip()
            display(Image(filename='kuda.jpg')) 
            input('''
                  Itu pasti hewan kuda!
                  =========================
                  Press ENTER!''')
    else:
        skip()
        berenang = input('''
                         apakah hewan ini bisa berenang?(y/n)
                         >> ''')
        if berenang =='y':
            skip()
            display(Image(filename='bebek.jpg')) 
            input('''
                  Itu pasti hewan bebek!
                  =========================
                  Press ENTER!''')
        elif berenang =='n':
            skip()
            display(Image(filename='ayam.jpg')) 
            input('''
                  Itu pasti hewan ayam!
                  =========================
                  Press ENTER!''')
    skip()
    y = input('''
              masih ingin bermain?(y/n)
              >> ''')
    if y != 'y':
       x = 2; skip()
    
    

      
      
