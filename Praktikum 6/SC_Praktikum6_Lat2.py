# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 22:45:21 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""

def createData(x):
    for i in range(6):
        x.append(31)
        x.append(30)

def bulan():
    while True:
        try:
            x = int(input('Masukkan Bulan(angka): '))
        except ValueError:
            print('INVALID')
        else:
            if x <= 0 or x > 12:
                print('INVALID')
            else:
                return x
                break

def tahun():
    global hari
    while True:
        try:
            x = int(input('Masukkan Tahun(angka): '))
        except ValueError:
            print('INVALID')
        else:
            y = str(x)
            if y[-1] == '0' and y[-2] == '0':
                x = x/100
                sisa = x % 4
                if sisa == 0:
                    print('\nKabisat')
                    hari[4] = 28
                else:
                    print('\nNormal')
            else:
                    sisa = x % 4
                    if sisa == 0:
                        print('\nKabisat')
                        hari[4] = 28
                    else:
                        print('\nNormal')  
            break

def main():
    while True:
        hari = ['none']
        createData(hari)
        bln = bulan()
        tahun()
        print(('Jumlah hari pada bulan {0}: {1}').format(bln,hari[bln]))
        ops = input('Press ENTER(lanjut) atau masukkan "n" untuk berhenti ')
        if ops == 'n':
            break
        
main()


