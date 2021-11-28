'''
Nama: Farhan Fadillah Harahap
NIM: 064002100017
'''

# funcsss
def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def selection(A):    
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j     
        A[i], A[min_idx] = A[min_idx], A[i]
        
def newfile(): # Buat list baru
    print(new_info)
    lis = []
    while True:
        try:
            angka = int(input(new_ask))
        except ValueError:
            break
        else:
            lis.append(angka)
    return lis
            
def openfile(): # Impor dari .txt
    buka = str(input(impor_askfilename))
    try:
        harahap = open(f'{buka}.txt','r')
    except:
        input(impor_failed)
        return False
    data = harahap.read()
    data = data.split(' = ')
    try:
        lis = data[1].split(',')
    except:
        input(impor_failed)
        return False
    else:
        try:
            lis = [int(x) for x in lis]
        except:
            input(impor_failed)
            return False
        else:
            return lis
        
def savefile(x,arr,arrs):
    file = open(f'{x}.txt','w')
    file.write('list = ')
    R = len(arrs)
    for i in arrs:
        R = R-1
        file.write(str(i))
        if R <= 0:
            break
        else:
            file.write(',')
    file.write('\n')
    file.write('list* = ')
    R = len(arr)
    for i in arr:
        R = R-1
        file.write(str(i))
        if R <= 0:
            break
        else:
            file.write(',')
    file.close()

def skip():
    for i in range(100):
        print()

# All diaolog   
errormsg=('''
          
    Input tidak dimengerti, mohon maaf!
    PRESS ENTER!''')
 
new_info=('''
          
    NEW
    ===========================      
    Masukkan angka untuk dimasukkan ke list! 
    Ketik selain angka untuk berhenti!''')
new_ask=('''
     >> ''')
new_error=('''
    Isi list harus lebih dari 1, coba lagi!
    PRESS ENTER!''')


impor_askfilename=('''
                   
    OPEN
    ============================               
    Nama file yang ingin dibuka: ''')
impor_failed=('''
             
    Mungkin kamu salah memasukkan nama file! Tidak berhasil!
    PRESS ENTER!''')
    
home_ask=('''
    
    PROGRAM SORTING (Mengurutkan list dan menyimpan hasilnya!)      
    Pilih opsi dibawah:
        a. NEW (saya belum punya file)
        b. OPEN (saya sudah pernah buat)
        
        >> ''')
home_listupdated=('''
     
    List kamu telah di-update! Berhasil!
    PRESS ENTER!''' )

saved=('''
     
    Disimpan! Berhasil!
    PRESS ENTER!''' )

# Alurr
input('Dibuat oleh Farhan F. Harahap\nPRESS ENTER!')
neverend = 1
while neverend == 1:
    while True:
        skip()
        opsi1 = str.lower(input(home_ask))
        if opsi1 == 'a':
            arr = newfile()
            if len(arr) <= 1:
                input(new_error)
            else:
                print(home_listupdated)
                break
        elif opsi1 == 'b':
            arr = openfile()
            if arr != False:
                print(home_listupdated)
                break
        else:
            input(errormsg)
    
    method_ask=(f'''
                
        List = {arr}
        List* = ???
        
        Sekarang, mau diurutkan pakai metode apa?
           a. BUBBLE SORT
           b. INSERTION SORT
           c. SELECTION SORT
           
           >> ''')
    arrs = [str(i) for i in arr]
    arrs = [int(i) for i in arr]
    while True:        
        skip()
        opsi2 = str.lower(input(method_ask))
        if opsi2 == 'a':
            bubble(arr)
            break
        elif opsi2 == 'b':
            insertion(arr)
            break
        elif opsi2 == 'c':
            selection(arr)
            break
        else:
            input(errormsg)
      
    hasil=(f'''
        
        List = {arrs}
        List* = {arr}
        
        Mau disimpan?(y/n) >> ''')
    asktosave=('''
        
        Buat nama file: ''')
        
    save = str.lower(input(hasil))
    if save == 'y':
        namafile = str(input(asktosave))
        savefile(namafile, arr, arrs)
        input(saved)
    else:
        pass
    

    

    

