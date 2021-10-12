# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:21:25 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""
#Bismillah
input('PoemMakerProPython 1.0 by Harahap:)\nPRESS ENTER')

# Tulislah sebuah Puisi yang disimpan dalam sebuah file.
# 1. Puisi harus ditulis per baris dari input user

print('\nKetik -1 dimana saja untuk MENGAKHIRI DAN SIMPAN\n')

ulang = True
while ulang == True:
    name = str(input('Masukkan nama file yang ingin dibuat atau diedit!\n>> '))
    filename = name+'.txt'
    poem = open(filename,'w')
    
    title = str()
    while title != '-1':
        title = str(input('''
            title:  ''')) # Judul
        
        if title[-1] == '.': # Gak boleh titik
            title = title.rstrip(title[-1])
            titlel = list(title.split(' '))
            cek = []
            for i in range(len(titlel)): # Kecilin kata :)
                cek.append(str.lower(titlel[i]))
            for i in range(len(cek)): # Penulisan judul yg baik :)
                if cek[i] == 'yang' or cek[i] == 'dan' or cek[i] == 'atau' or cek[i] == 'dari' or cek[i] == 'di' or cek[i] == 'pada' or cek[i] == 'kepada' or cek[i] == 'jika':
                    poem.write(cek[i])
                    poem.write(' ')
                else:
                    poem.write(str.capitalize(cek[i]))
                    poem.write(' ')
            poem.write('\n\n')
            # 2. Jumlah baris puisi tergantung keinginan user (-1 quit)
            line = ''    # Baris
            while line != '-1':
                line = str(input('''
                                 
                    ...     '''))
                cek = []
                baris = []
                
                if line[-1] == '.':
                    line = line.rstrip(line[-1])
                    linel = list(line.split(' '))
                    for i in range(len(linel)):
                        cek.append(str.lower(linel[i]))
                    lineresult = ' '.join(map(str, cek))
                    poem.write(str.capitalize(lineresult))
                    poem.write('\n')
                elif line != '-1':
                    linel = list(line.split(' '))
                    for i in range(len(linel)):
                        cek.append(str.lower(linel[i]))
                    lineresult = ' '.join(map(str, cek))
                    poem.write(str.capitalize(lineresult))
                    poem.write('\n')
                else:
                    title = '-1'
            
        elif title != '-1': # Proceed
            titlel = list(title.split(' '))
            cek = []
            for i in range(len(titlel)):
                cek.append(str.lower(titlel[i]))
            for i in range(len(cek)): # Penulisan judul yg baik :)
                if cek[i] == 'yang' or cek[i] == 'dan' or cek[i] == 'atau' or cek[i] == 'dari' or cek[i] == 'di' or cek[i] == 'pada' or cek[i] == 'kepada' or cek[i] == 'jika':
                    poem.write(cek[i])
                    poem.write(' ')
                else:
                    poem.write(str.capitalize(cek[i]))
                    poem.write(' ')
            poem.write('\n\n')
            # 2. Jumlah baris puisi tergantung keinginan user (-1 quit)
            line = ''    # Baris
            while line != '-1':
                line = str(input('''
                                 
                    ...     '''))
                cek = []
                baris = []
                
                if line[-1] == '.':
                    line = line.rstrip(line[-1])
                    linel = list(line.split(' '))
                    for i in range(len(linel)):
                        cek.append(str.lower(linel[i]))
                    lineresult = ' '.join(map(str, cek))
                    poem.write(str.capitalize(lineresult))
                    poem.write('\n')
                elif line != '-1':
                    linel = list(line.split(' '))
                    for i in range(len(linel)):
                        cek.append(str.lower(linel[i]))
                    lineresult = ' '.join(map(str, cek))
                    poem.write(str.capitalize(lineresult))
                    poem.write('\n')
                else:
                    title = '-1'
            
        
        else: # -1 means quit
            print('''
            PROGRAM QUITS''')
        print(('''
        SAVED, FIND "{0}.txt"''').format(name))
    
    # 3. Buka file dan cetak isi puisi dalam file tersebut (SAVED)
    poem.close()
    
    
    # Open and read
    opsi = input('''
        Mau di baca disini? (y/n) >> ''')
    if opsi == 'y':
        for i in range(100):
            print()
        baca = open(filename,'r')
        print()
        print(baca.read())
        print('END ~')
        baca.close()
    opsi2 = input('''
        Mau membuat atau mengedit file lagi? (y/n) >> ''')
    if opsi2 == 'n':
        print('''
        TERIMAKASIH TELAH MEMAKAI PROGRAM INI!''')
        ulang = False