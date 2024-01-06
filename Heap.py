class Heap:
    def __init__(self):
        self.heap = []
    
    # Movimiento hacia arriba del nodo del montículo
    def _bubble_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self._compare(self.heap[index], self.heap[parent_index]):
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break
    
    # Movimiento hacía abajo del nodo del montículo. 
    def _sink_down(self, index):
        size = len(self.heap)
        while index * 2 + 1 < size:
            child_index = self._get_child_index(index, size)
            if self._compare(self.heap[child_index], self.heap[index]):
                self.heap[index], self.heap[child_index] = self.heap[child_index], self.heap[index]
                index = child_index
            else:
                break
    
    # verifica cual si es mayor el indice hijo izquierdo o derecho.
    def _get_child_index(self, index, size):
        left_child_index = index * 2 + 1
        right_child_index = left_child_index + 1
        if right_child_index < size and self._compare(self.heap[right_child_index], self.heap[left_child_index]):
            return right_child_index
        return left_child_index
    
    # método de comparación entre padre e hijo, en caso de error, sale un mensaje
    def _compare(self, child, parent):
        raise print("Error de Implementación")
    
    # Inserta un nuevo elemento
    def push(self, item):
        self.heap.append(item)
        self._bubble_up(len(self.heap) - 1)

    # Elimina y devuelve el elemento de encima, si está vacío saldrá un None.
    def pop(self):
        if not self.heap:
            return None
        top_item = self.heap[0]
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self._sink_down(0)
        return top_item
    
    # Nos muestra el elemento de arriba del montículo.

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]
    
    # Nos muestra el tamaño del montículo.

    def size(self):
        return len(self.heap)
    
    # Verificación si está vacío.
    def is_empty(self):
        return len(self.heap) == 0
    
# Definimos las clases MaxHeap(Montículo máximo) y MinHeap(Montículo mínimo) 
# heredando de la Clase padre Heap.

# compara si nodo hijo es mayor a nodo padre, condición necesaria para cumplir que es un montículo.   
class MaxHeap(Heap):
    def _compare(self, child, parent):
        return child > parent
    
# compara si nodo hijo es menor a nodo padre, condición necesaria para cumplir que es un montículo.
class MinHeap(Heap):
    def _compare(self,child, parent):
        return child < parent
