import time

# Estrutura da Árvore Binária de Busca (BST)
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert(data, node.right)

    def delete(self, data):
        self.root = self._delete(data, self.root)

    def _delete(self, data, node):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete(data, node.left)
        elif data > node.data:
            node.right = self._delete(data, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._get_min(node.right)
            node.data = min_larger_node.data
            node.right = self._delete(min_larger_node.data, node.right)
        return node

    def _get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, data):
        return self._search(data, self.root)

    def _search(self, data, node):
        if node is None or node.data == data:
            return node is not None
        if data < node.data:
            return self._search(data, node.left)
        return self._search(data, node.right)

    def find_similar(self, key):
        result = DoublyLinkedList()
        self._find_similar(key.lower(), self.root, result)
        return result

    def _find_similar(self, key, node, result):
        if node:
            if key in node.data.lower():
                result.insert(node.data)
            self._find_similar(key, node.left, result)
            self._find_similar(key, node.right, result)

    def display(self):
        elems = []
        self._inorder_traversal(self.root, elems)
        return elems

    def _inorder_traversal(self, node, elems):
        if node:
            self._inorder_traversal(node.left, elems)
            elems.append(node.data)
            self._inorder_traversal(node.right, elems)

# Estrutura da Lista Duplamente Encadeada
class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        new_node = DoublyLinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        elems = []
        current = self.head
        while current:
            elems.append(current.data)
            current = current.next
        return elems

# Interface de Usuário
def main():
    bst = BinarySearchTree()

    while True:
        print("\n------------------------- \nMenu:")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Buscar Contato")
        print("4. Mostrar Todos os Contatos")
        print("5. Sair\n")

        choice = input("Escolha uma opção: ")

        # Opção 1. Adicionar Contato:
        if choice == '1':
            while True:
                name = input("Digite o nome do contato: ")
                if bst.search(name):
                    print(f"Contato {name} já existe. Não é possível adicionar duplicado.")
                else:
                    bst.insert(name)
                    print(f"Contato {name} adicionado.")
                
                while True:
                    another = input("Gostaria de adicionar mais algum contato? (s/n): ").lower()
                    if another == 'n':
                        break
                    elif another == 's':
                        break
                    else:
                        print("Valor incorreto, por favor escolha novamente:")

                if another == 'n':
                    break
                
        # Opção 2. Remover Contato:       
        elif choice == '2':
            name = input("Digite o nome do contato para remover: ")
            similar_contacts = bst.find_similar(name).display()
            if not similar_contacts:
                print(f"Contato {name} não encontrado.")
            else:
                print("Contatos encontrados:")
                for idx, contact in enumerate(similar_contacts, start=1):
                    print(f"{idx}. {contact}")
                try:
                    contact_idx = int(input("Digite o número do contato que deseja remover: ")) - 1
                    if 0 <= contact_idx < len(similar_contacts):
                        contact_to_remove = similar_contacts[contact_idx]
                        bst.delete(contact_to_remove)
                        print(f"Contato {contact_to_remove} removido.")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Entrada inválida.")
        
        # Opção 3. Buscar Contato:
        elif choice == '3':
            name = input("Digite o nome do contato para buscar: ")
            similar_contacts = bst.find_similar(name).display()
            if similar_contacts:
                print("Contatos encontrados:")
                for idx, contact in enumerate(similar_contacts, start=1):
                    print(f"{idx}. {contact}")
                    time.sleep(0.75)  # Pausa de 0.75 segundos antes de sair
            else:
                print(f"Contato {name} não encontrado.")
                time.sleep(0.75)  # Pausa de 0.75 segundos antes de sair

        # Opção 4. Exibir contatos:
        elif choice == '4': 
            contatos = bst.display() 
            if contatos:
                print("Contatos na Árvore Binária de Busca:")
                for idx, contact in enumerate(contatos, start=1):
                    print(f"{idx}. {contact}") 
                    time.sleep(0.75)  # Pausa de 0.75 segundos antes de sair
            else:
                print("Não existe nenhum contato cadastrado no momento.") 
                time.sleep(0.75)  # Pausa de 0.75 segundos antes de sair

        # Opção 5. Sair:
        elif choice == '5':
            print("Saindo...") 
            time.sleep(1)  # Pausa de 1 segundos antes de sair
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()