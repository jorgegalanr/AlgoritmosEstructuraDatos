class Heap:
    def __init__(self, comparison_func):
        self.heap = []
        self.compare = comparison_func
    
    # Saber el índice del padre de un nodo dado. Salida -> índice del nodo padre
    def _parent(self, index):
        return (index - 1) // 2
    
    # Saber el índice del hijo izquierdo del nodo dado. Salida -> índice del hijo izquierdo
    def _left_child(self, index):
        return 2 * index + 1
    
    # Saber el índice del hijo derecho del nodo dado. Salida -> índice del hijo derecho
    def _right_child(self, index):
        return 2 * index + 2
    
    # Mueve un nodo hacía arriba en el montículo  hasta reestablecer las propiedad del montículo (operación flotación).
    # Salida -> índice del nodod que está flotando
    def _bubble_up(self, index):
        parent = self._parent(index)
        while index > 0 and self.compare(self.heap[parent], self.heap[index]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self._parent(index)

    # Mueve un nodo hacia abajo en el montículo hasta que se restablecen las propiedades del montículo. 
    # Salida -> ínide del nodo que se está hundiendo.
    def _sink_down(self, index):
        size = len(self.heap)
        element = index

        while True:
            left = self._left_child(index)
            right = self._right_child(index)

            if left < size and self.compare(self.heap[element], self.heap[left]):
                element = left
            
            if right < size and self.compare(self.heap[element], self.heap[right]):
                element = right

            if element != index:
                self.heap[element], self.heap[index] = self.heap[index], self.heap[element]
                index = element
            else:
                break

    # inserta un nuevo elemento en el montículo. Salida -> Elemento a insertar en el montículo.
    def push(self, item):
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)
    
    # Elimina y devuelve el elemento en la cima del montículo. Salida -> Elemento en la cima del montículo. Si está vacío, devuelve None.
    def pop(self):
        if not self.heap:
            return None
    
        item = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._sink_down(0)
    
        return item

    # Devuelve el elemento en la cima del montículo sin eleminarlo. Salida -> Elemento en la cima del montículo. Si está vacío, devuelve None. 
    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]
    
    # Devuelve el número de elementos en el montículo. Salida -> Número de elementos en el montículo. 
    def size(self):
        return len(self.heap)

    # Verifica si el monticulo está vacío. Salida -> True, si está vacío, False, si no lo está.
    def is_empty(self):
        return len(self.heap) == 0
    
    # Devuelve una representación string del objeto Montículo. 
    def __str__(self):
        return str(list(self.heap))
    
# Clase MaxHeap para impelementar un montículo máximo, donde cada nodo padre es mayor que sus hijos. 
# Hereda de la clase Heap. 
class MaxHeap(Heap):

    def __init__(self):
        super().__init__(lambda parent, child: parent.valor < child.valor)

# Clase MinHeap para implementar un montículo mínimo, donde cada nodo padre es menor que sus hijos.
# Hereda de la clase Heap. 
class MinHeap(Heap):

    def __init__(self):
        super().__init__(lambda parent, child: parent.valor > child.valor)

