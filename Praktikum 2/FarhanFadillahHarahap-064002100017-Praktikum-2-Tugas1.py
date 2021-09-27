"""
Created on Tue Sep 21 12:51:13 2021

@author: HP
nama: Farhan Fadillah Harahap
NIM: 064002100017
"""

#Bismillah
import math

print('''
Selamat datang! Program ini akan mengolah 2 angka (a,b) menjadi
1. Jumlah a dan b
2. Selisih antara b dengan a
3. Hasil kali a dan b
4. Sisa pembagian a dengan b
5. Pembagian a dengan b
6. Hasil dari log(a)
7. a pangkat b
      ''')
      
a = float(input('Masukkan nilai a!\n>> '))
b = float(input('Masukkan nilaib!\n>> '))
print('\n1. Jumlah a dan b:', a + b)
if b >=a:
    print('2. Selisih antara b dengan a:', b - a)
else: 
    print('2. Selisih antara b dengan a:', a - b)
print ('3. Hasil kali a dan b:', a*b)
print('4. Sisa pembagian a dengan b:', a % b)
print('5. Pembagian a dengan b:', a / b)
print('6. Hasil dari log(a):', math.log10(a))
print('7. a pangkat b:', a**b)
