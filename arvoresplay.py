# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 18:26:38 2022

@author: joanm
"""

from sys import stdin,stdout
import time

class Artigo:
    def __init__(self,nome,ash,valor):
        self.nome=nome
        self.ash=ash
        self.valor=int(valor)
class Node:
    def __init__(self, Artigo):
        self.key = Artigo
        self.left = self.right = None

    
    
class SplayTree:
    def __init__(self):
        self.root = None
        self.header = Node(None) #For splay()

    def insert(self, nome,ash,valor):
        if (self.root == None):
            self.root = Node(Artigo(nome,ash,valor))
            return
        self.splay(nome)
        if self.root.key.nome == nome:
            # If the key is already there in the tree, don't do anything.
            return

        n = Node(Artigo(nome,ash,valor))
        if nome < self.root.key.nome:
            n.left = self.root.left
            n.right = self.root
            self.root.left = None
        else:
            n.right = self.root.right
            n.left = self.root
            self.root.right = None
        self.root = n
        
    def find(self, nome):
        if self.root == None:
            return None
        self.splay(nome)
        if self.root.key.nome != nome:
            return None
        return self.root
    
    def splay(self, nome):
        l = r = self.header
        t = self.root
        self.header.left = self.header.right = None
        while True:
            if nome < t.key.nome:
                if t.left == None:
                    break
                if nome < t.left.key.nome:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left == None:
                        break
                r.left = t
                r = t
                t = t.left
            elif nome > t.key.nome:
                if t.right == None:
                    break
                if nome > t.right.key.nome:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right == None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break
        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t
        
    def artigo(self,nome,ash,valor):
        if not self.find(nome):
            self.insert(nome, ash, valor)
            #stdout.write("NOVO ARTIGO INSERIDO\n")
            
        else:
            x=0
            #stdout.write("ARTIGO JA EXISTENTE\n")
    
    def oferta(self,nome,valor):
        if not self.find(nome):
            x=0
            #stdout.write("ARTIGO NAO REGISTADO\n")
        else:
            no=self.find(nome)
            no.key.valor=int(valor)
            #stdout.write("OFERTA ATUALIZADA\n")
    def listagem(self,no):
        if no!= None:
            self.listagem(no.left)
            #stdout.write(no.key.nome+" "+no.key.ash+" "+str(no.key.valor)+"\n")
            self.listagem(no.right)
    def Apaga(self):
        self.root = None
        #stdout.write("CATALOGO APAGADO\n")
        
def readln(test_file):
    return test_file.readline().rstrip().split(" ")

def main(x):
    splay_tree = SplayTree()
    user_in = [""]
    try:
            while(user_in[0] != "FIM"):
                user_in = readln(x)
                if user_in[0] == "ARTIGO":
                        splay_tree.artigo(user_in[1], user_in[2], user_in[3])
    
                if user_in[0] == "OFERTA":
                     splay_tree.oferta(user_in[1],user_in[2])       
                    
                if user_in[0] == "LISTAGEM":
                    splay_tree.listagem(splay_tree.root)
                    #stdout.write("FIM\n")
    
                if user_in[0] == "APAGA":
                    splay_tree.Apaga()   
                if user_in[0] == "CONSULTA":
                    if not splay_tree.find(user_in[1]):
                        x=0
                        #stdout.write("ARTIGO NAO REGISTADO\n")
                    else:
                        no=splay_tree.find(user_in[1])
                        #stdout.write(no.key.nome+" "+no.key.ash+" "+str(no.key.valor)+"\n")
                        #stdout.write("FIM\n")
    except EOFError:
        pass        
if __name__=='__main__': 
    times=[]
    test_number = [100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000]
    test_files = ["teste100000.txt", "teste200000.txt", "teste300000.txt", "teste400000.txt", "teste500000.txt","teste600000.txt","teste700000.txt","teste800000.txt","teste900000.txt","teste1000000.txt"]
    for i in range(len(test_number)):
        with open(test_files[i], "r") as test_file:
            start_time = time.time()
            main(test_file)
            times+=[(time.time() - start_time)]
    for i in times:
        print(i)