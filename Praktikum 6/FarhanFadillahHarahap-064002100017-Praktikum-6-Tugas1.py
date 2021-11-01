# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:23:48 2021

@author: HP
"""

nilai = [ 4.00 , 3.75 , 3.50 , 3.00 , 2.75 , 2.50 , 2.00 , 1.75 , 1.50 , 1.25]

def vartoscore(x):
    
    if x == 'A':
        score = float(nilai[0])
    elif x == 'A-':
        score = float(nilai[1])
    elif x == 'B+':
        score = float(nilai[2])
    elif x == 'B':
        score = float(nilai[3])
    elif x == 'B-':
        score = float(nilai[4])
    elif x == 'C+':
        score = float(nilai[5])
    elif x == 'C':
        score = float(nilai[6])
    elif x == 'C-':
        score = float(nilai[7])
    elif x == 'D':
        score = float(nilai[8])
    elif x == 'E':
        score = float(nilai[9])
    else:
        print('INVALID SCORE!')
        score = 0
    return score
        
def rata2kan(datanya):
    total = sum(datanya)
    rata2 = float(total / len(datanya))
    return rata2

def masukkandata():
        varnilai = str.upper(input('"exit" untuk berhenti!\nMasukkan nilai siswa: '))
        return varnilai
    
def hasil():    
    print(('''
          
          
          Nilai siswa:
          {0}
          
          Jumlah siswa: {1}
          
          Total nilai: {2}
          
          Rata-rata nilai = {3}
          
          
          ''').format(datanilai,len(datanilai),sum(datanilai),rata2kan(datanilai)))
    
datanilai = []
# User Interface
ulang = 0
nomor = 0
while ulang == 0:
    nomor += 1
    nilaivar = masukkandata()
    s = vartoscore(nilaivar)
    if nilaivar == 'EXIT':
        ulang = 1
    elif s == 0:
        print()
    else:
        print(('Siswa ke-{0} = {1}').format(nomor,s))
        datanilai.append(s)
          
hasil()
input('\nPRESS ENTER')
