# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 06:49:13 2021

@author: HP
Nama: Farhan F. Harahap
NIM: 064002100017
"""
input('TicketZooPay by F Harahap :)\nPRESS ENTER')

# User Interface

formopsi = str('''
    =============================
    Tiket yang ada di keranjang: {0}
    
    Total yang harus dibayar: ${1}
    =============================
    
    Ketik huruf untuk perintah!
    a. Tambah Tiket
    b. Lihat Tiket (Cek)
    c. Book Tiket (Selesai)
    z. Keluar
    
    >> ''')

formawal = str('''
    ==================================
    SELAMAT DATANG DI KEBUN BINATANG!
    ==================================
    
    Ketik angka untuk perintah!
    a. Beli Tiket
    b. Bantuan
    z. Keluar
    
    >> ''')
    
formbayar = str('''
                =========================
                Invoice: {1}
                Total: ${0}
                =========================
                Uang anda: $ ''')
                
ticket = str('''
            ===================================
            No. TKB00{0}
            Total: {1}
            Status: LUNAS
            
            TUKARKAN DI GERBANG! TERIMAKASIH
            ===================================''')
            
formnama = str('''
    ======================           
    Masukkan nama: 
    
        >> ''')
    
formumur = str('''
    Masukkan umur: 
        
        >> ''')
                
# Program

def nama(masuk,num):
    global data
    nomor = str(num)
    nama = str.capitalize(masuk)
    nonama = str('nama'+nomor)
    data[nonama] = nama
def umur(masuk,num):
    global data
    nomor = str(num)
    umur = int(masuk)
    noumur = str('umur'+nomor)
    data[noumur] = umur
def harga(masuk,num):
    global data
    nomor = str(num)
    harga = int(masuk)
    noharga = str('harga'+nomor)
    data[noharga] = harga
    
    
def tambahtiket(i):
    nama(str.lower(input(formnama)),i)
    while True:
        try:
            age = int(input(formumur))
            break
        except ValueError:
            print("Tolong masukan angka saja!")  
    umur(age,i)
    if age > 65:
        p = 18
    elif age >= 3 and age <= 12:
        p = 14
    elif age <= 2:
        p = 0
    else:
        p = 23     
    harga(p,i)

def lihattiket(awal):
    print('''
    ==========================
    DAFTAR KERANJANG TIKET ANDA
    ==========================''')
    if awal == True:
        num = 1
        nomor = str(num)
        print(str(('''
    Tiket {0}
    Nama: {1}
    Umur: {2}
    Harga: ${3}
    ''').format(nomor,data['nama'+nomor],data['umur'+nomor],data['harga'+nomor])))
        totalkan()
        print(('''
    ==========================
    Total: ${0}''').format(total))
    else:
        for i in range((len(data)//3)):
            num = i+1
            nomor = str(num)
            print(str(('''
    Tiket {0}
    Nama: {1}
    Umur: {2}
    Harga: ${3}
        ''').format(nomor,data['nama'+nomor],data['umur'+nomor],data['harga'+nomor])))
        totalkan()
        print(('''
    ==========================
    Total: ${0}''').format(total))
    
    
def totalkan():
    global total
    a = list()
    for i in range((len(data)//3)):
        num = i+1
        nomor = str(num)
        a.append(data['harga'+nomor])
        total = sum(a)
        

# Alur
program = True
inv = 0
while program == True:
    data = {}
    total = int()
    def space():
        for i in range(100):
            print()
            
    space()
    
    main = True
    while main == True:
        start = str.lower(input(formawal))
        if start == 'a':
            space()
            mulai = True
            tambahtiket(1)
            totalkan()
            main = False
            lanjut = True
            space()
        elif start == 'b':
            print('\nBELUM ADA BANTUAN') # add help later!
            input('TEKAN ENTER')
            space()
        elif start == 'z':
            print('\n\nTERIMAKASIH ~')
            main = False
            mulai = False
            book = False
            isi = False
            bayar = False
            tiket = False
            lanjut = False
            keluar = True
            input()
        else:
            print('\nERROR!')
            space()
    
    if lanjut == True:
        isi = True
    else:
        isi = False
    while isi == True:
        if lanjut == True:
            nomor = 1
        while mulai == True:
            opsi = str.lower(input(formopsi.format(nomor,total)))
            if opsi == 'a':
                space()
                nomor += 1
                tambahtiket(nomor)
                totalkan()
                space()
            elif opsi == 'b':
                space()
                if nomor == 1:
                    lihattiket(True)
                else:
                    lihattiket(False)
                input('Tekan Enter untuk kembali ke menu!')
                space()
            elif opsi == 'c':
                space()
                book = True
                mulai = False
            elif opsi == 'z':
                book = False
                mulai = False
                bayar = False
                tiket = False
                isi = False
                keluar = False
            else:
                print('\nERROR!')
                
            
        while book == True:
            inv += 1
            totalkan()
            lihattiket(False)
            opsi = str.lower(input('\nKonfirmasi pembayaran? (y/n)\n>> '))
            if opsi == 'y':
                bayar = True
                book = False
                isi = False
                space()
            elif opsi == 'n':
                book = False
                mulai = True
                lanjut = False
                space()
            else:
                print('\nSaya tidak mengerti!')
                input('Tekan Enter!')
            
    while bayar == True:
        totalkan()
        uang = int(input(formbayar.format(total,inv)))
        if uang < total:
            print('\nMaaf uang anda tidak cukup!')
            bokek = str.lower(input('ulang lagi? (y/n)\n>> '))
            if bokek == 'n':
                bayar = False
                tiket = False
                keluar = False
            else:
                bayar = True
        else:
            uang = uang - total
            if uang == 0:
                print('\nUang anda pas, terimakasih!')
                input('Tekan ENTER!')
                tiket = True
                bayar = False
            else:
                duit = str(uang)
                print('\nKembalian anda: $'+duit,'Terimakasih!')
                input('Tekan ENTER!')
                tiket = True
                bayar = False         
    if tiket == True:
        space()
        print(ticket.format(inv,total))
        input('Tekan ENTER! (PRINT)')
        keluar = False
    if keluar == True:
        break
    
