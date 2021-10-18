# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:43:14 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""

nilai = [ 4.00 , 3.75 , 3.50 , 3.00 , 2.75 , 2.50 , 2.00 , 1.75 , 1.50 , 1.25]
score = 0

def vartoscore(x):
    global score
    
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
        
datanilai = []
# User Interface
ulang = 0
nomor = 0
while ulang == 0:
    nomor += 1
    varnilai = str.upper(input('"exit" untuk berhenti!\nMasukkan nilai siswa: '))
    if varnilai == 'EXIT':
        ulang = 1
    else:
        vartoscore(varnilai)
        print(('Siswa ke-{0} = {1}').format(nomor,score))
        datanilai.append(score)
    
rata2 = sum(datanilai) / len(datanilai)
print(('''
      
      
      Nilai siswa:
      {0}
      
      Jumlah siswa: {1}
      
      Total nilai: {2}
      
      Rata-rata nilai = {3}
      
      SAVED AS 'nilai siswa.txt', CHECK YOUR DIRECTORY :)
      
      ''').format(datanilai,len(datanilai),sum(datanilai),rata2))
      
# Pemanis (Bonus) tadi gak ditampilin soalnya buru2 :D

file = open('nilai siswa.txt','w')
num = 0
for i in range (len(datanilai)):
    num += 1
    form = (('{0}. Siswa ke-{1} = {2}\n').format(num,num,datanilai[i]))
    file.write(form)
    
file.write('\n\n')
rata2form = (('''
             
      Jumlah siswa: {0}
      
      Total nilai: {1}
      
      Rata-rata nilai = {2}
      '''
      ).format(len(datanilai),sum(datanilai),rata2) )   
file.write(rata2form)
file.close()
