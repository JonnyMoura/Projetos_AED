from random import randint
if __name__ == '__main__':

    n = 1000000
    numeroInsercoes = int(n / 2)
    numeroConsulta = int(n / 2)
    artigos05 = int(numeroConsulta * 0.05) # 5% dos artigos
    listaInsercoes = []
    lista5 = []

    ficheiro = open("teste1000000.txt", "w")

    for i in range(numeroInsercoes):
        numeroRandom = randint(0, n)
        if i < artigos05:
            lista5.append(f"Pintura{numeroRandom}")
            ficheiro.write(f"ARTIGO Pintura{numeroRandom} {randint(100000, 999999)} {randint(1000, 9999)}\n")
        else:
            ficheiro.write(f"ARTIGO Pintura{numeroRandom} {randint(100000, 999999)} {randint(1000, 9999)}\n")
            listaInsercoes.append(f"Pintura{numeroRandom}")


    _90percentInsercoes = int(numeroConsulta * 0.9)
    for i in range(numeroConsulta):
        if i < _90percentInsercoes:
            ficheiro.write(f"CONSULTA {lista5[randint(1,len(lista5)-1)]}\n")
        else:
            ficheiro.write(f"CONSULTA {listaInsercoes[randint(1,len(listaInsercoes)-1)]}\n")

    ficheiro.write("FIM\n")
