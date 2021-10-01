# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 09:01:49 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""

#bismillah
import math
x = True

while x == True:
    for i in range(100):
        print()
    a,b = (input('''
                 Masukkan koordinat 1 (x,y): ''').split(","))
    c,d = (input('''
                 Masukkan koordinat 2 (x,y): ''').split(","))
    x1 = float(a)
    y1 = float(b)
    x2 = float(c)
    y2 = float(d)
    
    #euclidean
    euclidean = (math.sqrt( ((x2-x1)**2) + ((y2-y1)**2)))*111.319
    h_euclidean = '{0:.2f}'.format(euclidean)
    print(('''
                  Jarak (Euclidean): ±%s Km''') % (h_euclidean))
                  
    #haversine
    earth_radius = 6371
    dLat = ((x2 - x1)*math.pi)/180
    dLon = ((x2 - x1)*math.pi)/180
    p1 = math.sin(dLat/2) * math.sin(dLat/2) + math.cos((x1*math.pi)/180) * math.cos((x2*math.pi)/180) * math.sin(dLon/2) * math.sin(dLon/2) 
    p2 = 2 * math.asin(math.sqrt(p1)); 
    p3 = earth_radius * p2; 
    h_haversine = '{0:.2f}'.format(p3)
    print(('''
                  Jarak (Haversine): ±%s Km''') % (h_haversine))
                  
    opt = input('''
                  
                  *Ketik n untuk menyudahi ''')
    if opt == 'n':
        x = False
