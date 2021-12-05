'''
Nama: Farhan Fadillah Harahap
NIM: 064002100017
'''

def bubbleSort(x):
    count = 0
    for idx in range(len(x)-1):
        if x[idx] > x[idx + 1]:
            x[idx],x[idx + 1] = x[idx + 1],x[idx]
            count += 1
    if count == 0:
        return x
    else:
        bubbleSort(x)

while True:
    while True:
        try:        
            urutkan = str(input('Masukkan angka: (x,y,z,...)\n>> ')).split(',')
            urutkan = [int(i) for i in urutkan]
        except:
            print('\nError:\n* Syntax Error\n* Non Bilangan-Bulat')
        else:
            break
    
    print(f'\n\nList: {urutkan}')
    
    bubbleSort(urutkan)
    
    print(f'\n\nList*: {urutkan}')
