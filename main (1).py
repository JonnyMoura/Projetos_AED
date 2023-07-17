from sys import stdin


class Card:
    def __init__(self, ncard, date):
        self.date = date
        self.ncard = int(ncard)


class User:
    def __init__(self, username, card):
        self.username = username
        self.card = []
        self.card.append(card)


class No:

    def __init__(self, user, height, parent, left, right):
        self.user = user
        self.left = left
        self.right = right
        self.height = height
        self.parent = parent


class AVLTree:
    def __init__(self):
        self.root = None

    def find(self, username, no):
        if no is None:
            return None
        if username > no.user.username:
            return self.find(username, no.right)
        elif username < no.user.username:
            return self.find(username, no.left)
        return no

    def Consulta(self, username):
        no = None
        if self.root is None:
            return None
        elif self.root:
            no = self.find(username, self.root)
        for i in no.user.card:
            print(str(i.ncard) + i.date)
        print("FIM")
        return no

    def left_rotate(self, child, no):
        if child.left:
            no.right = child.left
            no.right.parent = no
        else:
            no.right_child = None
        if no != self.root:
            child.parent = no.parent
            no.parent.right = child
        else:
            child.parent = None
            self.root = child
        child.left = no
        no.parent = child
        no.height = no.height - 1

    def right_rotate(self, child, no):
        if child.right:
            no.left = child.right
            no.left.parent = no
        else:
            no.left = None
        if no != self.root:
            child.parent = no.parent
            no.parent.left = child
        else:
            child.parent = None
            self.root = child
        child.right = no
        no.parent = child
        no.height = no.height - 1

    def rotate(self, no):
        global left_height, right_height
        if no.left:
            left_height = no.left.height
        if no.right:
            right_height = no.right.height
        if abs(left_height - right_height) > 1:
            if left_height < right_height:
                self.left_rotate(no, no.right)
            else:
                self.right_rotate(no, no.left)
        else:
            no.height = max(left_height, right_height) + 1

    def insert(self, username, ncard, date, no):
        if username < no.user.usernam:
            if not no.left:
                no.left = No(User(username, Card(ncard, date)), None, no, no.left, None)
                return no.left
            return self.insert(username, ncard, date, no.lefte)
        elif username > no.user.username:
            if not no.right:
                no.right = No(User(username, Card(ncard, date)), None, no, None, no.right)
                return no.right
            return self.insert(username, ncard, date, no.right)

    def grow(self, no):
        if not no:
            return None
        else:
            self.rotate(no)
            return self.grow(no.parent)

    def Acrescenta(self, username, ncard, date):
        global no, assist
        if self.Consulta(username) is None:
            if not self.root:
                self.root = No(User(username, Card(ncard, date)), None, None, None, None)
            else:
                new_no = self.insert(username, ncard, date, self.root)
                self.grow(new_no)
            print("NOVO UTILIZADOR CRIADO”")
        else:
            no = self.Consulta(username)
            for i in no.user.card:
                if i.ncard == ncard:
                    i.date = date
                    assist = assist + 1
                    print("CARTAO ATUALIZADO")
                else:
                    assist = 0
            if assist == 0:
                no.user.card.add(Card(ncard, date))
                print("NOVO CARTAO INSERIDO")

    def listagem(self, no):
        if no.right:
            no = no.right
            print(no.user.username, end='')
            for i in no.user.card:
                print(str(i.ncard) + i.date, end='')
            print("\n")
            self.listagem(no)
        if no.left:
            no = no.left
            print(no.user.username, end='')
            for i in no.user.card:
                print(str(i.ncard) + i.date, end='')
            print("\n")
            self.listagem(no)
        print("FIM")

    def Listagem(self):
        self.listagem(self.root)

    def Apaga(self):
        self.root = None
        print("LISTAGEM APAGADA")


def read():
    instruction = [str(i) for i in stdin.readline()]
    for i in instruction:
        i.split(" ")
    return instruction


def readln():
    return stdin.readline().rstrip()


def Instructions(instruction):
    tree = AVLTree()
    for i in instruction:
        print(i[0])
        if i[0] == "ACRESCENTA":
            tree.Acrescenta(i[1], i[2], i[3])
        elif i[0] == "CONSULTA":
            tree.Consulta(i[1])
        elif i[0] == "LISTAGEM":
            tree.Listagem()
        elif i[0] == "APAGA":
            tree.Apaga()
    print("FIM")


instruction = [str(i) for i in readln().split(" ")]
for j in instruction:
    for i in range(len(instruction)):
        print(j[i])

Instructions(instruction)
