# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 14:11:58 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""


class mahasiswa:
    
    jumlah = 0
    
    def __init__(self,nama,nim,tahun):
        self.nama = str.upper(nama)
        self.nim = str(nim)
        self.tahun = str(tahun)
        mahasiswa.jumlah += 1
        
    def biodata(self):
        return str(f'{self.nama} ; {self.nim} ; {self.tahun}')
    
    def cetak(self):
        print()
        print('Nama:',self.nama)
        print('NIM:',self.nim)
        print('Tahun:',self.tahun)
        print()
        input(f'Jumlah mahasiswa sekarang adalah {mahasiswa.jumlah} orang\nPRESS ENTER')


while True:
    print(f'\nMAHASISWA {(mahasiswa.jumlah)+1}\nKetik -1 untuk mengakhiri!')
    x = str(input('Nama: '))
    if x == '-1':
        break
    y = str(input('NIM: '))
    z = str(input('Tahun: '))
    n = mahasiswa(x,y,z)
    
    n.cetak()
