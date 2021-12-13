# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 07:45:33 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""

input('PROGRAM by Harahap :) 064002100017\nPRESS ENTER')

class mahasiswa:
     def __init__(self):
          self._nama = str()
          self._umur = 0
          self._nim = str()
          self._jurusan = str()

     #nama
     def get_nama(self):
         print("\nMenampilkan nama!")
         return self._nama
       
     def set_nama(self, a):
         print("Nama diubah!")
         self._nama = str.upper(a)
  
     def del_nama(self):
         del self._nama
     
     nama = property(get_nama, set_nama, del_nama) 
     
     # umur
     def get_umur(self):
         print("\nMenampilkan umur!")
         return self._umur
       
     def set_umur(self, a):
         print("Umur diubah!")
         self._umur = a
  
     def del_umur(self):
         del self._umur
     
     umur = property(get_umur, set_umur, del_umur) 
     
     # nim
     def get_nim(self):
         print("\nMenampilkan NIM!")
         return self._nim
       
     def set_nim(self, a):
         print("NIM diubah!")
         self._nim = str(a)
  
     def del_nim(self):
         del self._nim
     
     nim = property(get_nim, set_nim, del_nim) 
     
     # jurusan
     def get_jurusan(self):
         print("\nMenampilkan jurusan!")
         return self._jurusan
       
     def set_jurusan(self, a):
         print("Jurusan diubah!")
         self._jurusan = str.upper(a)
  
     def del_jurusan(self):
         del self._jurusan
     
     jurusan = property(get_jurusan, set_jurusan, del_jurusan) 
  
p = mahasiswa()
p.nama = input('Masukkan nama mahasiswa: ')
p.nim = input('Masukkan NIM mahasiswa: ')
p.umur = input('Masukkan umur mahasiswa: ')
p.jurusan = input('Masukkan jurusan mahasiswa: ')

while True:
    while True:
        ops = str.upper(input('''
                              
                              
Menu:
a. Edit informasi Biodata
b. Tampilkan informasi Biodata
c. KELUAR PROGRAM

>> '''       ))
        
        if ops == 'A':
            mode = 'edit'
            break
        elif ops == 'B':
            mode = 'baca'
            break
        elif ops == 'C':
            mode = 'keluar'
            break
        else:
            input('\nProgram tidak mengerti!\nPRESS ENTER')
            
    if mode == 'edit':
        while True:
            ops = str.lower(input('''
                                  
                                  
Edit:
a. Nama
b. NIM
c. Umur
d. Jurusan
e. SELESAI

>> '''                      ))
            
            if ops == 'a':
                p.nama = input('Masukkan nama mahasiswa: ')
            elif ops == 'b':
                p.nim = input('Masukkan NIM mahasiswa: ')
            elif ops == 'c':
                p.umur = input('Masukkan umur mahasiswa: ')
            elif ops == 'd':
                p.jurusan = input('Masukkan jurusan mahasiswa: ')
            elif ops == 'e':
                break
            else:
                input('\nProgram tidak mengerti!\nPRESS ENTER')
                
                
    elif mode == 'keluar':
        input('\n\nTerimakasih! \nPROGRAM ENDS PLEASE PRESS ENTER')
        break 
           
    elif mode == 'baca':
        while True:
            ops = str.lower(input('''
                                  
                                  
Tampilkan:
a. Nama
b. NIM
c. Umur
d. Jurusan
e. SELESAI

>> '''                      ))
            
            if ops == 'a':
                input(f'{p.nama}\nPRESS ENTER')
            elif ops == 'b':
                input(f'{p.nim}\nPRESS ENTER')
            elif ops == 'c':
                input(f'{p.umur}\nPRESS ENTER')
            elif ops == 'd':
                input(f'{p.jurusan}\nPRESS ENTER')
            elif ops == 'e':
                break
            else:
                input('\nProgram tidak mengerti!\nPRESS ENTER')
                


  
