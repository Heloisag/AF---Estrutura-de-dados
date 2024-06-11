import time


# Definição da Lista Encadeada
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def search(self, key):
        current = self.head

        while current != None:
            if current.data == key:
                return True
            current = current.next

        return False

    def display(self):
        elems = []
        current = self.head
        while current:
            elems.append(current.data)
            current = current.next
        print(elems)


    # Definição da Árvore Binária de Busca
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.val:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._minValueNode(root.right)
            root.val = temp.val
            root.right = self._delete(root.right, temp.val)
        return root

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    

# Interface de Usuário
def main():
    linked_list = LinkedList()
    bst = BinarySearchTree()

    while True:
        print("\nMenu:")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Buscar Contato")
        print("4. Mostrar Todos os Contatos")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Digite o nome do contato: ")
            linked_list.insert(name)
            bst.insert(name)
            print(f"Contato {name} adicionado.")
            time.sleep(1) #Pausa de 1 segundo antes de sair

        elif choice == '2':
            name = input("Digite o nome do contato para remover: ")
            linked_list.delete(name)
            bst.delete(name)
            print(f"Contato {name} removido.")
            
            time.sleep(1) #Pausa de 1 segundo antes de sair

        elif choice == '3':
            name = input("Digite o nome do contato para buscar: ")
            found_in_list = linked_list.search(name)
            found_in_bst = bst.search(name) is not None
            if found_in_list and found_in_bst:
                print(f"Contato {name} encontrado.")
            else:
                print(f"Contato {name} não encontrado.")
                time.sleep(1) #Pausa de 1 segundo antes de sair

        elif choice == '4':
            contatos = linked_list.display()
            if contatos:
                print("Contatos na Lista Encadeada:")
                print(contatos)
            else:
                print("Não existe nenhum contato cadastrado no momento.")
                time.sleep(1) #Pausa de 1 segundo antes de sair

        elif choice == '5':
            print("Saindo...")
            time.sleep(1) #Pausa de 1 segundo antes de sair
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()    