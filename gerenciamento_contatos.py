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
        prev = None

        while temp is not None:
            if temp.data == key:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                return temp.data
            prev = temp
            temp = temp.next

        return None

    def search(self, key):
        current = self.head

        while current is not None:
            if current.data == key:
                return True
            current = current.next

        return False

    def find_similar(self, key):
        current = self.head
        similar = []
        key_lower = key.lower()

        while current is not None:
            if key_lower in current.data.lower():
                similar.append(current.data)
            current = current.next

        return similar

    def display(self):
        elems = []
        current = self.head
        while current:
            elems.append(current.data)
            current = current.next
        return elems

# Interface de Usuário
def main():
    linked_list = LinkedList()

    while True:
        print("\n------------------------- \nMenu:")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Buscar Contato")
        print("4. Mostrar Todos os Contatos")
        print("5. Sair\n")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            while True:
                name = input("Digite o nome do contato: ")
                if linked_list.search(name):
                    print(f"Contato {name} já existe. Não é possível adicionar duplicado.")
                else:
                    linked_list.insert(name)
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
                
        elif choice == '2':
            name = input("Digite o nome do contato para remover: ")
            similar_contacts = linked_list.find_similar(name)
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
                        linked_list.delete(contact_to_remove)
                        print(f"Contato {contact_to_remove} removido.")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Entrada inválida.")
        
        elif choice == '3':
            name = input("Digite o nome do contato para buscar: ")
            similar_contacts = linked_list.find_similar(name)
            if similar_contacts:
                print("Contatos encontrados:")
                for idx, contact in enumerate(similar_contacts, start=1):
                    print(f"{idx}. {contact}")
                    time.sleep(0.75)  # Pausa de 0.75 segundos antes de sair
            else:
                print(f"Contato {name} não encontrado.")
                time.sleep(0.75)  # Pausa de 0.75 segundos antes de sair

        elif choice == '4':
            contatos = linked_list.display()
            if contatos:
                print("Contatos na Lista Encadeada:")
                for idx, contact in enumerate(contatos, start=1):
                    print(f"{idx}. {contact}")
                    time.sleep(0.75)  # Pausa de 0.75 segundos antes de sair
            else:
                print("Não existe nenhum contato cadastrado no momento.")
                time.sleep(0.75)  # Pausa de 0.75 segundos antes de sair

        elif choice == '5':
            print("Saindo...")
            time.sleep(1)  # Pausa de 1 segundos antes de sair
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()