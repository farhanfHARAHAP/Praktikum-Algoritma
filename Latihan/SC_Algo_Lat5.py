# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:35:05 2021

@author: HP
Name: Farhan Fadillah Harahap
NIM: 064002100017
"""
def polyn(n):
    for x in range(n):
        print(f"x^{n} +", end=" ")
        n -= 1
        if n == 1:
            print("x + 1")
            break
        
polyn(int(input("Masukan Angka : ")))
