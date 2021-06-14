import time
import six
import datetime
from collections import defaultdict
encontrado=0
duracion=0
start_ms=0
op=0
patron=""
#Fuerza bruta
def fuerza_bruta(txt,pat,tlen,plen):
    global start_ms,encontrado
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
                    encontrado+=1
                    break
                if(txt[tj]!=pat[pi]):
                    break
        ti+=1

#BMP
def BMP(txt,pat,tlen,plen):
    global start_ms
    global encontrado
    start =  time.time()
    start_ms=int(round(start*1000))
    lps=[0]*plen
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
            encontrado+=1
            j=lps[j-1]
        elif((i<tlen) and (pat[j] != txt[i])):
            if(j!=0):
                j=lps[j-1]
            else:
                i+=1

#KMP

def KMP(txt,pat,tlen,plen):
    global encontrado,start_ms
    i=0
    j=0
    start =  time.time()
    start_ms=int(round(start*1000))
    while i<tlen:
        while j<plen and (i+j)<tlen:
            if (txt[i+j]!=pat[j]):
                break
            j+=1
    
        if j==plen:
            encontrado+=1
        j=0
        i+=1

#BMH    
def boyer_moore_horspool(text, pattern ,n,m):
    global encontrado,start_ms
    start =  time.time()
    start_ms=int(round(start*1000))
    if m > n:
        return -1

    skip = defaultdict(lambda: m)

    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1

    k = m - 1

    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            encontrado+=1

        k += skip[ord(text[k])]
#BMHS
def boyer_moore_horspool_sunday(text, pattern ,n,m):
    global encontrado,start_ms
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

def getIndex(pat, c,plen):
    i=plen-1
    while(i>=0):
        if(pat[i]==c):
            return i
        i-=1
    return -1
#Imprimir todo
def imprimir():
    global encontrado,duracion,op,patron
    if(op==1):
        print("Ocurrencias encontradas con el patron ->"+ patron + "<- En el algoritmo Fuerza bruta")
        print("Tiempo de respuesta      Cantidad de ocurrencias     ")
        print(str(duracion) +"                   "+ str(encontrado))
    if(op==2):
        print("Ocurrencias encontradas con el patron ->"+ patron + "<- En el algoritmo Knuth-Morris-Pratt")
        print("Tiempo de respuesta      Cantidad de ocurrencias     ")
        print(str(duracion) +"                   "+ str(encontrado))
    if(op==3):
        print("Ocurrencias encontradas con el patron ->"+ patron + "<- En el algoritmo Boyer-Moore-Horspool")
        print("Tiempo de respuesta      Cantidad de ocurrencias     ")
        print(str(duracion) +"                   "+ str(encontrado))
    if(op==4):
        print("Ocurrencias encontradas con el patron ->"+ patron + "<- En el algoritmo Boyer-Moore-Horspool-sunday")
        print("Tiempo de respuesta      Cantidad de ocurrencias     ")
        print(str(duracion) +"                   "+ str(encontrado))    


#Main
def Main():
    global start_ms,encontrado,duracion,op,patron
    f = open("C:\Users\USUARIO\Downloads\La fiesta del chivo.txt","r", encoding="cp437")
    texto = f.read()
    print("Analisis de algoritmos, Busqueda en textos")
    print ("1-Brute Force")
    print ("2-KMP")
    print ("3-BMH")
    print ("4-BMS")
    print ("5-Salir")
    op=float(raw_input("Digite su opcion:  "))
    patron=(raw_input("Digite su patron:  "))
    if(op==1):
        fuerza_bruta(texto,patron,len(texto),len(patron))
        finish =  time.time()
        finish_ms=int(round(finish*1000))
        duracion = (finish_ms-start_ms)
        imprimir()
    elif(op==2):
        KMP(texto,patron,len(texto),len(patron))
        finish =  time.time()
        finish_ms=int(round(finish*1000))
        duracion = (finish_ms-start_ms)
        imprimir()
    elif(op==3):
        boyer_moore_horspool(texto,patron,len(texto),len(patron))
        finish =  time.time()
        finish_ms=int(round(finish*1000))
        duracion = (finish_ms-start_ms)
        imprimir()
    elif(op==4):
        boyer_moore_horspool_sunday(texto,patron,len(texto),len(patron))
        finish =  time.time()
        finish_ms=int(round(finish*1000))
        duracion = (finish_ms-start_ms)
        imprimir()
    

Main()
