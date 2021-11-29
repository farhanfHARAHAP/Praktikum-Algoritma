# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 14:05:04 2021

@author: HP
Nama: Farhan Fadillah Harahap
NIM: 064002100017
"""


# Its 12 PM btw :)
# Bismillah


def newfile():
    skip()
    try:
        hapname = str(input(new_askname))
    except:
        input(error)
        return
    hap = open(f'{hapname}.txt','w')
    num = 0
    input(new_info)
    start(hap,num)
    hap.close()
    
def openfile():
    skip()
    try:
        hapname = str(input(open_askname))
    except:
        input(error)
        return
    hap = open(f'{hapname}.txt','r+')
    text = [str(x) for x in hap]
    num = 0
    input(new_info)
    print('\n\n\n')
    for i in text:
        num += 1
        print(f'     {num}:> {i}')
    start(hap,num)
    hap.close

def readonly():
    skip()
    hapname = str(input(read_askname))
    try:
        hap = open(f'{hapname}.txt','r+')
    except:
        input(error)
        return
    text = [str(x) for x in hap]
    num = 0
    input(read_info)
    print('\n\n\n')
    for i in text:
        num += 1
        print(f'     {num}:> {i}')
        ops = input('*')
        if ops == '/quit':
            break
            return
    input(endline)
    hap.close

def start(hap,num):
    while True:
        num += 1
        line = str(input(f'     {num}:> '))
        if line == '/quit':
            input(saved)
            break
        else:
            hap.write(line)
            hap.write('\n')

def skip():
    for i in range(50):
        print()
            
    
new_askname=('''
    
    [NEW FILE]________________
    File name: ''')
new_info=('''
         
    HELP: Teruslah menulis, /quit untuk keluar!
    
    PRESS ENTER''')
open_askname=('''
    
    [OPEN FILE]________________
    File name: ''')
read_askname=('''
    
    [READER]________________
    File name: ''')
read_info=('''
         
    HELP: Teruslah membaca dengan menekan ENTER, 
    ketik /quit untuk keluar!
    
    PRESS ENTER''')
error=('''
    
    ==[ERROR]========
    *Input wrong
    *Try again
    
    PRESS ENTER!''')
saved=('''
    
    ==[SAVED]========
    *Text anda telah disimpan!
    
    PRESS ENTER!''')
endline=('''
    
    ==[END-LINE]========
    *Akhir text!
    
    PRESS ENTER!''')
    

# ALURR 1:34 AM

while True:
    skip()
    menu=('''
             
        TEXT READER, EDITOR, AND WRITER!__________
        Pilih menu dibawah, untuk memulai sesuatu:
            a. NEW FILE (Buat file baru!)
            b. EDIT FILE (Buka dan edit file)
            c. READER (Fitur membaca keren)
            e. QUIT / EXIT
            
        >> ''')
        
    mulai = str.lower(input(menu))
    if mulai == 'a':
        newfile()
    elif mulai == 'b':
        openfile()
    elif mulai == 'c':
        readonly()
    elif mulai == 'e':
        print('\n\nPROGRAMS ENDS HERE. THANK YOU!')
        break 
    else:
        input(error)
    
