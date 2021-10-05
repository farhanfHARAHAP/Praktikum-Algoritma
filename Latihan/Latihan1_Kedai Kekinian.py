# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 11:19:34 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""

harga = int()
total = int()
topping = str()

## Menu
print('Selamat Datang di Segar Drink!\n')
print('Menu hari ini: \n1. Teh Tarik 1$\n2. Capucino 1.5$\n3. Teh Susu 1$')

## User pilih
x = int(input('\nMasukkan angka untuk memilih minuman: '))
if x == 1:
    harga += 1
    minuman = 'Teh Tarik'
elif x == 2:
    harga += 1.5
    minuman = 'Capucino'
elif x == 3:
    harga += 1
    minuman = 'Teh Susu'

##Topping minuman
print('Mau tambah topping, cuma 0.5$ aja? (y/n)')
y = str(input('>> '))

if y == 'n':
    total = harga
else:
    print('Topping tersedia:\n1. Bubuk Coklat\n2. Vanilla Cream')
    z = int(input('\nMasukkan angka untuk memilih topping: '))
    if z == 1:
        topping = 'Bubuk Coklat'
    elif z == 2:
        topping = 'Vanilla Cream'
    total = harga + 0.5
    
##Masa satu doang_-
stok = int(input('\nKamu mau pesen ini berapa?\n>> '))
total = total * stok
        
print ('\nKamu memesan:', stok, 'x', minuman, topping, '\nTotal:', total, '$')
konfir = str(input('Konfirmasi?(y/n)\n>>'))
if konfir == 'y':
    print ('\nTerimakasih! Silahkan lanjutkan ke kasir ya!')
else:
    exit()


