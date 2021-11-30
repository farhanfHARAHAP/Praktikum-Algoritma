'''
Nama: Farhan Fadillah Harahap
NIM: 064002100017
'''


input('CREATED BY HARAHAP\nPRESS ENTER')

def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
def binarySearch(arr, l, r, x):
 

    if r >= l:
 
        mid = l + (r - l) // 2
 
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        else:
            return binarySearch(arr, mid + 1, r, x)
 
    else:

        return -1
    
def createarray():
    y = []
    input('Terus tambahkan elemen bilangan bulat di list\nJika sudah ketik huruf apa saja!\n\nPRESS ENTER')
    while True:
        try:
            x = int(input('\n>> '))
        except:
            break
        else:
            y.append(x)
    
    return y



arr = createarray()
print(f'\nList sebelum di-sort:\n{arr}')
bubble(arr)
print(f'List setelah di-sort:\n{arr}')

while True:
    try:
        x = int(input('Mau cari angka berapa?(Ketik huruf untuk menyudahi!)\n\n>> '))
    except:
        print('\nTERIMAKASIH!')
        break
    else:
        result = binarySearch(arr, 0, len(arr)-1, x)
        if result == -1:
            input('\nAngka tidak dtemukan!\nPRESS ENTER')
        else:
            input(f'\nDitemukan! Angka {x} cari ada di urutan ke-{result+1}\nPRESS ENTER')
        
        

            
            
