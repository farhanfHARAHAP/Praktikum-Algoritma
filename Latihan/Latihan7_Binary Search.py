# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:09:33 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""

input('CREATED BY FARHAN HARAHAP :)\nPRESS ENTER!')

# Variabel
nomor = []
nim = []
nama = []

# Create data part 1 :)
file = open('mahasiswa_gasal_2021.csv','r')
data = []
x = 0
baris = []
for line in file:
    x += 1
    baris = line.split(',')
    if x == 35:
        break
    else:
        if x == 1:
            nomor.append(baris[0])
            nim.append(baris[1])
            nama.append(baris[2])
        else:
            nomor.append(int(baris[0]))
            nim.append(int(baris[1]))
            nama.append(baris[2])
nama = [line.strip() for line in nama]
file.close()

       
# Create data part 2 :))
file = open('mahasiswa_gasal_2021.csv','r')
data2 = []
x = 0
for line in file:
    data2.append(line)
    x+=1
    if x >= 34:
        break
    else:
        pass    
     
file.close()

# Kategori

def vnama(x,y):
    m = (len(x)-1) // 2
    # persis
    if x[m] == y:
        return m
    # belakang
    l = 0
    while True:
        if x[l] == y:
            return l
        elif l == m:
            break
        else:
            l += 1
    # depan
    l = (len(y)-1)
    while True:
        try:
            if x[l] == y:
                return l
            elif l == m:
                break
            else:
                l -= 1
        except IndexError:
            return -1
    
def vnomor(arr, l, r, x):
 
    if r >= l:
 
        mid = l + (r - l) // 2

        if mid == x:
            return mid

        elif mid > x:
            return vnomor(arr, l, mid-1, x)

        else:
            return vnomor(arr, mid + 1, r, x)
 
    else:
        return -1
    
def vadv(farhanstan,cari):
    r = []
    for nama in farhanstan:
        for kata in nama.split(' '):
            temp = []
            for k in range(len(kata)):
                temp.append(kata[k])
                cek = ''.join(temp)
                temp2 = []
                for l in range(k,len(kata)):
                    temp2.append(kata[l])
                    cek2 = ''.join(temp2)
                if cek == cari:
                    if nama in r:
                        pass
                    else:
                        r.append(nama)
                elif cek2 == cari:
                    r.append(nama)
    
    if r == 0:
        print('Hasil tidak ditemukan!')
    else:
        r = sorted(r)
        print('====================')
        for i in r:
            print (i)

def vabjad(farhanstan,cari):
    farhanstan = sorted(farhanstan)
    skip = {'A':0}
    skip2 = [0]
    
    data = []
    start = 0
    cache = 'A'
    for a in farhanstan:
        fullname = list(a.split(' '))
        data.append(fullname)
        fname = fullname[0]
        letter = fname[0]
        if cache != letter:
            cache = letter
            skip[f'{letter}'] = start
            skip2.append(start)
        start += 1
    skip['end'] = len(farhanstan)
    skip2.append(len(farhanstan))
      
         
    cari = cari
    try:
        n = skip[f'{cari[0]}']
    except KeyError:
        print('Hasil tidak ditemukan!')
    except IndexError:
        print('Hasil tidak ditemukan!')
    else:
        for i in range(len(skip2)):
            if skip2[i] == n:
                m = skip2[i+1]
                break
        
        r = []
        print(f'\nDengan awal huruf {cari[0]}:')
        for i in range(n,m):
            r.append(farhanstan[i])
            print(farhanstan[i])
        return r

# ALURRR
while True:
    # Alur
    opsi = str.lower(input('\nCari via:\na.Nama\nb.NIM\nc.Nomor absen\nd.Nama (Advanced)\ne.Nama (Abjad)\n\n>> '))
    if opsi == 'a':
        cari = str.upper(input('Pencarian: '))
        result = vnama(nama,cari)
        if result == -1:
            print('Yang anda cari tidak ditemukan!')
        else:
            print(data2[result])
    elif opsi == 'b':
        cari = str.upper(input('Pencarian: '))
        if len(cari) >= 2:
            digitl = [cari[-2],cari[-1]]
        else:
            digitl = [cari[-1]]
        digit = ''.join(digitl)
        digit = int(digit)
        result = vnomor(nomor,0,len(nomor)-1,int(digit))
        if result == -1:
            print('Yang anda cari tidak ditemukan!')
        else:
            print('>>',data2[result])

    elif opsi == 'c':
        cari = str.upper(input('Pencarian: '))
        try:
            result = vnomor(nomor,0,len(nomor)-1,int(cari))
        except ValueError:
            print('Masukkan BILANGAN BULAT!')
        else:
            if result == -1:
                print('Yang anda cari tidak ditemukan!')
            else:
                print('>>',data2[result])
            
    elif opsi == 'd':
        cari = str.upper(input('Pencarian: '))
        vadv(nama,cari)
    elif opsi == 'e':
        cari = str.upper(input('Pencarian: '))
        r = vabjad(nama,cari)
    else:
        print('Masukkan sesuai opsi yang tersedia!')

        
