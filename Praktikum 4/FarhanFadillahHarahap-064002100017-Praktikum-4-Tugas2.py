# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:38:14 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""
#bismillah

x = True
while x == True:
    # 1. Input bulan dan tahun
    
    bulan = int(input('Masukkan Bulan(angka): '))
    if bulan == 0 or bulan > 12:
        print('INVALID')
    else:
        tahun = int(input('Masukkan Tahun(angka): '))
        hari = ['none']
        for i in range(6):
            hari.append(31)
            hari.append(30)
        
        # 2. Tentukan hari dalam bulan tsb.
        
        tahunstr = str(tahun)
        
        
        if tahunstr[-1] == '0' and tahunstr[-2] == '0':
            tahun = tahun/100
            sisa = tahun % 4
            if sisa == 0:
                print('\nKabisat')
                hari[4] = 28
            else:
                print('\nNormal')
        
        else:
            sisa = tahun % 4
            if sisa == 0:
                print('\nKabisat')
            else:
                print('\nNormal')
            
        print(('Jumlah hari pada bulan {0}: {1}').format(bulan,hari[bulan]))
        ops = input('Press ENTER(lanjut) atau masukkan "n" untuk berhenti ')
        if ops == 'n':
            x = False


