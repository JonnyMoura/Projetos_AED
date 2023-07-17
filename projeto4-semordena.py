# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 16:14:22 2022

@author: joanm
"""

from sys import stdin,stdout
import math,time,random



def readln(x):
    return x.readline().rstrip().split(" ")

def amp(array):
    maior=0
    menor=array[0]
    for i in array:
            if(i>maior):
                maior=i
            if(i<menor):
                menor=i
    aux=maior-menor
    #print(str(aux))

def percentil(array,perc):
        soma=0
        for k in array:
                if(k<perc):
                    soma+=1
        return math.floor((soma/len(array))*100)
        

def raster(n,m,array,x):
    for i in range(n):
        aux=readln(x)
        for i in aux:
            array+=[int(i)]
    #stdout.write("RASTER GUARDADO\n")

def mediana(l):
    if l:
        if len(l) % 2 != 0:
            for i in range(len(l)):
                direita = esquerda = 0
                numerosIguais = 0
                for j in range(len(l)):
                    if l[i] > l[j]:
                        esquerda += 1
                    elif l[i] < l[j]:
                        direita += 1
                    else:
                        numerosIguais += 1

                if direita == esquerda or math.floor(len(l) / 2) == direita or math.floor(
                        len(l) / 2) == esquerda or numerosIguais > math.floor(len(l) / 2):
                    median = l[i]
                    #print(median)
                    
                    break

        else:
            lista = []
            for i in range(len(l)):
                esquerda = direita = 0
                numerosIguais = 0
                for j in range(len(l)):
                    if l[i] > l[j]:
                        esquerda += 1
                    elif l[i] < l[j]:
                        direita += 1
                    elif l[i] == l[j] and i != j:
                        numerosIguais += 1


                if (abs(direita - esquerda) == 1 or esquerda == direita or esquerda == len(l) / 2 or direita == len(l)/2) and len(lista) < 2:
                    lista.append(l[i])

                if len(lista) == 2:
                    median = math.floor((lista[0] + lista[1]) / 2)
                    #print(median)
                    break

def main(x):
    user_in = [""]
    array=[]
    try:
            while(user_in[0] != "TCHAU"):
                user_in = readln(x)
                if user_in[0] == "RASTER":
                      raster(int(user_in[1]), int(user_in[2]),array,x)
              
                if user_in[0] == "PERCENTIL":
                    percentil(array,int(user_in[1]),x)
                if user_in[0] == "AMPLITUDE":
                    amp(array)
                if user_in[0]=="MEDIANA":
                    mediana(array)
    
                  
    except EOFError:
        pass                            
                
lista = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
for NUM in lista:
    print("--- Valores pra %d ---" % NUM)
    raster1 = [random.randrange(0, 10000) for _ in range(NUM)]
    perc = [random.randrange(0, 10000) for _ in range(NUM)]
    tic = time.perf_counter()
    for i in range(NUM):
        percentil(raster1, perc[i])
    toc = time.perf_counter()
    print("--- %f seg ---" % (toc - tic))
print()    
  
                