"""
Created on Mon Nov 15 13:24:58 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""

def fibbo(n):
   if n <= 1:
       return n
   else:
       return(fibbo(n-1) + fibbo(n-2))
   
def cetak(x):
    if x <= 0:
        print("Hanya angka postif!")
    else:
       print('Bilangan FIBBONCAI ke-'+str(x),'adalah',fibbo(x))

while True:
    try:
        bil = int(input('Masukkan bilangan >> '))
    except ValueError:
        print('Invalid input, masukkan angka bulat!\n')
    else:
        cetak(bil)
