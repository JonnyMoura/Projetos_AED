from random import randint


def generate_tests(num, show=False, lvl=0):
    def generate_tests_util(num, show=False, lvl=0):
        temp = []
        while num != 1:
            a = randint(1, num - 1)
            num -= a
            temp.append(a)
            print(f"Utilizador{randint(0, 10000)} {randint(0, 1000)} {randint(1000, 9999)}")
        for i in temp:
            generate_tests_util(i, show, lvl + 1)

    generate_tests_util(num, show, lvl)


if __name__ == '__main__':

    n = 1000000
    numeroInsercoes = int(n / 2)
    numeroConsulta = int(n * 0.05)

    ficheiro = open("teste1000000.txt", "w")

    listaInsercoes = []
    listaAlpha = []
    for i in range(numeroInsercoes):
        numeroRandom = randint(0, n)
        listaAlpha.append(randint(100000, 999999))
        ficheiro.write(f"ARTIGO Pintura{numeroRandom} {listaAlpha[i]} {randint(1000, 9999)}\n")
        listaInsercoes.append(f"Pintura{numeroRandom}")

    # for i in range(numeroOfertas):
    #   numeroRandom = randint(0,n)
    #    ficheiro.write(f"OFERTA Pintura{numeroRandom} {listaAlpha[i]} {randint(1000, 9999)}\n")

    for i in range(len(listaInsercoes)):
        ficheiro.write(f"CONSULTA {listaInsercoes[i]}\n")
        numeroConsulta -= 1

    # for i in range(numeroConsulta):
    #    ficheiro.write(f"CONSULTA {i}\n")
    ficheiro.write("FIM\n")
