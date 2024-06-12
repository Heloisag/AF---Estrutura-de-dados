## DynamicDataManager - python project

Para o projeto final, desenvolvemos uma árvore binária de busca (BST) que interage com uma lista duplamente encadeada como estrutura de dados auxiliar. 
Essa combinação permite armazenar e manipular os contatos na árvore, além de listar contatos similares utilizando a lista duplamente encadeada.


### Estrutura da Árvore Binária de Busca (BST)

#### TreeNode:
Esta classe representa um nó na árvore binária de busca (BST). Cada nó contém um dado e referências para seus nós filhos esquerdo e direito.

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

- **data:** O valor armazenado no nó.
- **left:** Referência ao filho esquerdo do nó.
- **right:** Referência ao filho direito do nó.


#### BinarySearchTree:
Esta classe representa a árvore binária de busca e contém métodos para inserir, deletar, buscar e exibir elementos na árvore.

```python
class BinarySearchTree:
    def __init__(self):
        self.root = None
```

- **root:** O nó raiz da árvore. Inicialmente, é None (árvore vazia).


### Métodos

#### insert:
Insere um novo dado na árvore.

```python
def insert(self, data):
    if self.root is None:
        self.root = TreeNode(data)
    else:
        self._insert(data, self.root)
```

Se a árvore estiver vazia, o novo nó se torna a raiz. Caso contrário, o método privado `_insert` é chamado para encontrar a posição correta na árvore.

```python
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
```

Este método recursivo insere o novo nó no lugar apropriado, comparando o dado a ser inserido com o dado do nó atual e movendo-se para a esquerda ou para a direita conforme necessário.


#### delete:
Remove um dado da árvore.

```python
def delete(self, data):
    self.root = self._delete(data, self.root)
```

O método `_delete` é recursivo e encontra o nó a ser deletado, ajustando as referências dos nós pais conforme necessário.

```python
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
```

Se o nó a ser deletado tiver dois filhos, encontramos o menor nó na subárvore direita (`_get_min`), substituímos o valor do nó a ser deletado pelo valor desse nó mínimo, e então deletamos o nó mínimo.

```python
def _get_min(self, node):
    current = node
    while current.left is not None:
        current = current.left
    return current
```

Este método encontra o nó com o menor valor na subárvore dada.


#### search:
Busca um dado na árvore.

```python
def search(self, data):
    return self._search(data, self.root)
```

O método `_search` é recursivo e verifica se o dado está no nó atual ou se deve continuar a busca na subárvore esquerda ou direita.

```python
def _search(self, data, node):
    if node is None or node.data == data:
        return node is not None
    if data < node.data:
        return self._search(data, node.left)
    return self._search(data, node.right)
```


#### find_similar:
Encontra nós que contêm uma substring específica e armazena esses resultados em uma lista duplamente encadeada.

```python
def find_similar(self, key):
    result = DoublyLinkedList()
    self._find_similar(key.lower(), self.root, result)
    return result
```

O método `_find_similar` é recursivo e adiciona os nós que contêm a substring na lista de resultados.

```python
def _find_similar(self, key, node, result):
    if node:
        if key in node.data.lower():
            result.insert(node.data)
        self._find_similar(key, node.left, result)
        self._find_similar(key, node.right, result)
```


#### display:
Retorna uma lista com os dados em ordem crescente (in-order traversal).

```python
def display(self):
    elems = []
    self._inorder_traversal(self.root, elems)
    return elems
```

O método `_inorder_traversal` é recursivo e percorre a árvore em ordem crescente.

```python
def _inorder_traversal(self, node, elems):
    if node:
        self._inorder_traversal(node.left, elems)
        elems.append(node.data)
        self._inorder_traversal(node.right, elems)
```


### Estrutura da Lista Duplamente Encadeada


#### DoublyLinkedListNode:
Esta classe representa um nó na lista duplamente encadeada.

```python
class DoublyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

- **data:** O valor armazenado no nó.
- **prev:** Referência ao nó anterior.
- **next:** Referência ao próximo nó.


#### DoublyLinkedList:
Esta classe representa a lista duplamente encadeada e contém métodos para inserir e exibir elementos.

```python
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
```

- **head:** O primeiro nó da lista.
- **tail:** O último nó da lista.


### Metodos

#### insert:
Insere um novo dado na lista.

```python
def insert(self, data):
    new_node = DoublyLinkedListNode(data)
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
```
Se a lista estiver vazia, o novo nó se torna a cabeça e a cauda. Caso contrário, ele é adicionado ao final da lista.


#### display:
Retorna uma lista com os dados armazenados na lista duplamente encadeada.

```python
def display(self):
    elems = []
    current = self.head
    while current:
        elems.append(current.data)
        current = current.next
    return elems
```
Este método percorre a lista e coleta os dados em uma lista Python.


### Interface de Usuário

A interface de usuário permite que o usuário interaja com a árvore binária de busca para adicionar, remover, buscar e exibir contatos.
É implementada na função main(), que fica no final do código e é executada quando o script é iniciado.

```python
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
```


### Inicialização da Árvore Binária de Busca (BST):

Uma instância de BinarySearchTree é criada para armazenar os contatos. Esta árvore será responsável por gerenciar a estrutura e as operações dos contatos.
Loop Principal:

O programa entra em um loop while True, o que significa que continuará executando até que o usuário escolha a opção "Sair" (opção 5).
Menu de Opções:

A cada iteração do loop, um menu é exibido na tela para que o usuário escolha uma das opções disponíveis:
1. Adicionar Contato: Permite ao usuário adicionar novos contatos à árvore.
2. Remover Contato: Permite ao usuário remover contatos da árvore.
3. Buscar Contato: Permite ao usuário buscar contatos na árvore.
4. Mostrar Todos os Contatos: Exibe todos os contatos atualmente armazenados na árvore.
5. Sair: Encerra o programa e sai do loop.


### Opção 1: Adicionar Contato

**Funcionamento:**
•	O usuário pode inserir o nome de um contato.
•	O programa verifica se o contato já existe na árvore usando o método *search* da BST.
•	Se o contato não existe, ele é inserido na árvore usando o método *insert* da BST.
•	Após cada inserção, o programa pergunta se o usuário deseja adicionar mais contatos.
•	Se o usuário digitar *'n'*, o programa retorna ao menu principal.


```python
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
```


### Opção 2: Remover Contato

```python
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
```

- **Funcionamento:**
  - O usuário digita o nome de um contato que deseja remover.
  - O programa usa `find_similar` da BST para encontrar contatos similares ao nome fornecido (caso haja correspondências parciais).
  - Se contatos similares são encontrados, são exibidos na tela com números de índice para seleção.
  - O usuário pode escolher um contato para remover digitando o número correspondente.
  - O programa usa `delete` da BST para remover o contato escolhido.


### Opção 3: Buscar Contato

```python
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
```

- **Funcionamento:**
  - O usuário digita o nome de um contato que deseja buscar.
  - O programa usa `find_similar` da BST para encontrar contatos cujos nomes contenham a substring fornecida.
  - Se contatos são encontrados, eles são exibidos na tela.
  - O programa faz uma pausa de 0.75 segundos entre cada contato encontrado antes de sair.


### Opção 4: Mostrar Todos os Contatos

```python
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
```

- **Funcionamento:**
  - Todos os contatos atualmente armazenados na árvore são exibidos usando o método `display` da BST.
  - Se não houver contatos, uma mensagem informando que nenhum contato está cadastrado é exibida.
  - O programa faz uma pausa de 0.75 segundos entre cada contato exibido antes de sair.


### Opção 5: Sair

```python
elif choice == '5':
    print("Saindo...") 
    time.sleep(1)  # Pausa de 1 segundo antes de sair
    break
```

- **Funcionamento:**
  - O programa exibe uma mensagem indicando que está saindo.
  - Uma pausa de 1 segundo é feita antes de encerrar o programa completamente (`break` termina o loop `while True`).


### Considerações Finais

A interface do usuário proporciona uma interação intuitiva com a árvore binária de busca para gerenciar contatos, usando operações de inserção, remoção, busca e exibição. A lista duplamente encadeada é usada internamente para armazenar e exibir contatos similares encontrados durante operações de busca. Essa combinação de estruturas de dados oferece eficiência e funcionalidade no gerenciamento de informações de contato.