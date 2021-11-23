# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 15:41:56 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""

def edit():
    haphap = open('Biodata.txt','w')
    
    p1 = str(input('Nama Anda: '))
    p1 = list(p1.split(' '))
    p1c = [str.capitalize(x) for x in p1]
    p1x = ' '.join(p1c)
    p2 = str(input('Umur Anda: '))
    p3 = str.upper(input('Alamat lengkap: '))
    p4 = str(input('Email Anda: '))
    p5 = str(input('Dosen Wali Anda: '))
    p5 = list(p5.split(' '))
    p5c = [str.capitalize(x) for x in p5]
    p5x = ' '.join(p5c)
    
    text = str(f'''
    Nama: {p1x}
    Umur: {p2}
    Alamat: {p3}
    Email: {p4}
    Dosen Wali: {p5x}
    ''')
    
    haphap.write(str(text))
    
    haphap.close()

    print('File tersimpan dengan nama "Biodata.txt" !')

def baca():
    hap = open('Biodata.txt','r')
    for i in hap:
        print(i)
        
    hap.close()
    
while True:
    opsi = str.lower(input('\n\nSelamat datang di Biodata Editor:\na. Mau edit!\nb. Mau baca!\n\n>> '))
    if opsi == 'a':
        edit()
    elif opsi == 'b':
        baca()
        input('Press Enter')
    else:
        print('Saya tidak mengerti!')


