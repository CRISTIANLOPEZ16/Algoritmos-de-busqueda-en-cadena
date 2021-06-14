import time
import datetime
from collections import defaultdict

print("Este programa se usa para búsqueda")

bandera = True
#ruta=input("Ingrese la ruta del txt que contiene el texto ")
#texto=open(ruta,"r")
start =  time.time()
start_ms=int(round(start*1000))
texto=open(r"fichero","r", encoding="utf8")
txt = texto.read()
texto.close()

def patron():
    global patron2
    patron2=input("Ingrese el patron a buscar  ")
    global pat
    pat=list(patron2)
patron()


def fuerzaBruta(txt,pat):
    print()
    plen=len(pat)
    tlen=len(txt)
    start =  time.time()
    start_ms=int(round(start*1000))
    #Inicia el proceso
    ti = 0
    enc=0
    while(ti<=tlen-plen):
        if(txt[ti]==pat[0]):
            pi=0
            tj=ti
            while True:
                tj+=1
                pi+=1
                if(pi==plen):
                    enc+=1
                    break
                if(txt[tj]!=pat[pi]):
                    break
        ti+=1
    #Finaliza el proceso
    finish =  time.time()
    finish_ms=int(round(finish*1000))
    duracion = (finish_ms-start_ms)
    print()
    print('{:^10}{:^10}{:^10}{:^15}'.format('Patron', 'Cantidad', 'Tiempo en ms','Algoritmo'))
    print('{:^10}{:^10}{:^10}{:^20}'.format(patron2, enc, duracion, 'Brute Force'))
    print()

def kmp(txt,pat):
    print()
    plen=len(pat)
    tlen=len(txt)
    start =  time.time()
    start_ms=int(round(start*1000))
    lps=[0]*plen
    #Inicia el preproceso
    tama=0
    enc=0
    lps[0]
    i=1
    while(i<plen):
        if(pat[i]==pat[tama]):
            tama+=1
            lps[i]=tama
            i+=1
        else:
            if tama!=0:
                tama=lps[tama-1]
            else:
                lps[i]=0
                i+=1
    #Finaliza el preproceso
    #Inicia el proceso
    j=0
    i=0
    while(i<tlen):
        if(pat[j]==txt[i]):
            i+=1
            j+=1
        if(j==plen):
            enc+=1
            j=lps[j-1]
        elif((i<tlen) and (pat[j] != txt[i])):
            if(j!=0):
                j=lps[j-1]
            else:
                i+=1
    #Finaliza el proceso
    finish =  time.time()
    finish_ms=int(round(finish*1000))
    duracion = (finish_ms-start_ms)
    print()
    print('{:^10}{:^10}{:^10}{:^15}'.format('Patron', 'Cantidad', 'Tiempo en ms','Algoritmo'))
    print('{:^10}{:^10}{:^10}{:^20}'.format(patron2, enc, duracion, 'KMP'))
    print()



def bmh(txt, pat):
    print()
    enc=0
    plen=len(pat)
    tlen=len(txt)
    start =  time.time()
    start_ms=int(round(start*1000))
    if plen > tlen:
        return -1

    skip = defaultdict(lambda: plen)
    found_indexes = []

    for k in range(plen - 1):
        skip[ord(pat[k])] = plen - k - 1

    k = plen - 1

    while k < tlen:
        j = plen - 1
        i = k
        while j >= 0 and txt[i] == pat[j]:
            j -= 1
            i -= 1
        if j == -1:
            enc+=1

        k += skip[ord(txt[k])]
    #Finaliza el proceso
    finish =  time.time()
    finish_ms=int(round(finish*1000))
    duracion = (finish_ms-start_ms)
    print()
    print('{:^10}{:^10}{:^10}{:^15}'.format('Patron', 'Cantidad', 'Tiempo en ms','Algoritmo'))
    print('{:^10}{:^10}{:^10}{:^20}'.format(patron2, enc, duracion, 'BMH'))
    print()


def b(text, pattern):
    m=len(pat)
    n=len(txt)
    encontrado=0
    start =  time.time()
    start_ms=int(round(start*1000))
    if m > n:
        return -1

    skip = defaultdict(lambda: m)

    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1

    k = m - 1
    step=-1
    i=0
    while(i<=n-m):
        j=0
        while(j<m):
            if(text[i+j]!=pattern[j]):
                if(i==n-m):
                    break
                step=m-getIndex(pattern, text[i+m],m)
                break
            j+=1
        if(j==m):
            encontrado+=1
        i+=step
    encontrado-=1
    return-1
    finish =  time.time()
    finish_ms=int(round(finish*1000))
    duracion = (finish_ms-start_ms)
    print()
    print('{:^10}{:^10}{:^10}{:^15}'.format('Patron', 'Cantidad', 'Tiempo en ms','Algoritmo'))
    print('{:^10}{:^10}{:^10}{:^20}'.format(patron2, encontrado, duracion, 'NUEVO'))
    print()

    
def getIndex(pat, c,plen):
    i=plen-1
    while(i>=0):
        if(pat[i]==c):
            return i
        i-=1
    return -1

def bmhs(txt, pat):
    print()
    enc=0
    plen=len(pat)
    tlen=len(txt)
    start =  time.time()
    start_ms=int(round(start*1000))
    if plen > tlen:
        return -1

    skip = defaultdict(lambda: plen)

    for k in range(plen - 1):
        skip[ord(pat[k])] = plen - k - 1

    k = plen - 1
    step=-1
    i=0
    while(i<=tlen-plen):
        j=0
        while(j<plen):
            if(txt[i+j]!=pat[j]):
                if(i==tlen-plen):
                    break
                step=plen-getIndex(pat, txt[i+plen],plen)
                break
            j+=1
        if(j==plen):
            enc+=1
        i+=step
    #enc-=1
    #return-1
    #Finaliza el proceso
    finish =  time.time()
    finish_ms=int(round(finish*1000))
    duracion = (finish_ms-start_ms)
    print()
    print('{:^10}{:^10}{:^10}{:^15}'.format('Patron', 'Cantidad', 'Tiempo en ms','Algoritmo'))
    print('{:^10}{:^10}{:^10}{:^20}'.format(patron2, enc, duracion, 'BMHS'))
    print()



while bandera:   
    print ("Qué algoritmo desea usar?")
    print ("1-Brute Force")
    print ("2-KMP")
    print ("3-BMH")
    print ("4-BMHS")
    print ("5-Cambiar patron")
    print ("6-Salir")
    opcion_menu=float(input("Digite su opción:  "))

    #Fuerza Bruta
    if opcion_menu == 1:
        fuerzaBruta(txt,pat)
    if opcion_menu == 2:
        kmp(txt,pat)
    if opcion_menu== 3:
        bmh(txt,pat)
        
    if opcion_menu == 4:
        bmhs(txt,pat)
        
    if opcion_menu == 5:
        patron()
        
    if opcion_menu == 6:
        break