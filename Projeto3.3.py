from sys import stdin,stdout


class Cartao:
    def __init__(self,num,data):
        self.num=num
        self.data=data




class Utilizador:
    def __init__(self,user,cartao):
        self.user=user
        self.cartoes=[]
        self.cartoes.append(cartao)
    


class Node:
    def __init__(self, Utilizador):
        self.utilizador = Utilizador
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1


class AVLTree(object):

    def __init__(self):
        self.root = None
    
    def _insert(self, node, utilizador,cartao,date):
        if utilizador < node.utilizador.user:
            if not node.left:
                node.left = Node(Utilizador(utilizador,Cartao(cartao,date)))
                node.left.parent = node
                return node.left
            return self._insert(node.left, utilizador, cartao, date)
        elif utilizador > node.utilizador.user:
            if not node.right:
                node.right = Node(Utilizador(utilizador,Cartao(cartao,date)))
                node.right.parent = node
                return node.right
            return self._insert(node.right, utilizador, cartao, date)
    
    def find(self, utilizador, node):
        if node is None:
            return False
        if node.utilizador.user > utilizador:
            return self.find(utilizador, node.left)
        elif node.utilizador.user < utilizador:
            return self.find(utilizador, node.right)
        return node
    
    def _check_node(self, no):
         left_height = -1
         right_height = -1
         if no.left:
             left_height = no.left.height
         if no.right:
            right_height = no.right.height
         if abs(left_height - right_height) > 1:
            if left_height < right_height:
                if no.right:
                    self.left_rotate(no, no.right)
                else:
                    self.right_rotate(no, no.left)
            else:
                if no.left:
                    self.right_rotate(no, no.left)
                else:
                    self.left_rotate(no, no.right)
         else:
            no.height = max(left_height, right_height) + 1
    
    def left_rotate(self, node, child_node):
        if child_node.left:
            node.right = child_node.left
            node.right.parent = node
        else:
            node.right = None

        if node != self.root:
            child_node.parent = node.parent
            if node.parent.right == node:
                node.parent.right = child_node
            else:
                node.parent.left = child_node
        else:
            child_node.parent = None
            # because we are not replacing the parent node('node') with the
            # child node('child_node'), self.root is still pointing at the parent node.
            self.root = child_node

        child_node.left = node
        node.parent = child_node

        node.height -= 1

    def right_rotate(self, node, child_node):
        if child_node.right:
            node.left = child_node.right
            node.left.parent = node
        else:
            node.left = None

        if node != self.root:
            child_node.parent = node.parent
            if node.parent.right == node:
                node.parent.right = child_node
            else:
                node.parent.left = child_node
        #
        else:
            child_node.parent = None
            self.root = child_node

        child_node.right = node
        node.parent = child_node

        node.height -= 1
        
    def _walk_up(self, node):
        if not node:
            return
        else:
            self._check_node(node)
            return self._walk_up(node.parent)
        
        
    def insert(self, user,cartao,date):
        if not self.root:
            self.root = Node(Utilizador(user,Cartao(cartao,date)))
        else:
            new_node = self._insert(self.root, user,cartao,date)
            self._walk_up(new_node)
        
    def acrescenta(self,user,card,data):
        if not self.find(user,self.root):
            self.insert(user, card, data)
            stdout.write("NOVO UTILIZADOR CRIADO\n")
            
        else:
            no=self.find(user,self.root)
            flag=0
            for i in no.utilizador.cartoes:
                if(i.num==card):                    
                    i.data=data
                    flag+=1
                    no.utilizador.cartoes.sort( key=lambda Cartao: Cartao.num)
                    stdout.write("CARTAO ATUALIZADO\n")
            if(flag==0):
                no.utilizador.cartoes.append(Cartao(card, data))
                no.utilizador.cartoes.sort( key=lambda Cartao: Cartao.num)
                stdout.write("NOVO CARTAO INSERIDO\n")
             
    
            
 # passa pela arvore    
    def traverse_tree(self):
        if not self.root:
            return iter(())
        return self.traverse_inorder(self.root)




    # da yield a todos os nos da esquera para a direita
    def traverse_inorder(self, node):
        if node.left:
            yield from self.traverse_inorder(node.left)
        yield node
        if node.right:
            yield from self.traverse_inorder(node.right)
   
     
    def Apaga(self):
        self.root = None
        stdout.write("LISTAGEM APAGADA\n")
        
def list_users(avl_tree):
    tree = avl_tree.traverse_tree()
    for node in tree:
        stdout.write(node.utilizador.user)
        for i in node.utilizador.cartoes:
           stdout.write(" "+str(i.num) +" "+ i.data)
        stdout.write("\n")
    stdout.write("FIM\n")  

      
def readln():
        return stdin.readline().rstrip().split(" ")



            
        
def main():
    avl_tree = AVLTree()
    user_in = [""]
    try:
            while(user_in[0] != "FIM"):
                user_in = readln()
                if user_in[0] == "ACRESCENTA":
                        avl_tree.acrescenta(user_in[1], user_in[2], user_in[3])
    
                if user_in[0] == "CONSULTA":
                    if not avl_tree.find(user_in[1],avl_tree.root):
                        stdout.write("NAO ENCONTRADO\n")
                    else:
                        for i in avl_tree.find(user_in[1],avl_tree.root).utilizador.cartoes: 
                            stdout.write(str(i.num) +" "+ str(i.data)+"\n")
                        stdout.write("FIM\n")
                if user_in[0] == "LISTAGEM":
                    list_users(avl_tree)
    
                if user_in[0] == "APAGA":
                    avl_tree.Apaga()   
    except EOFError:
        pass        
if __name__=='__main__': 
    main()
               
    
    
        
    
       
    