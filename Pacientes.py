# Fase Implementación
import Heap import MaxHeap, MinHeap

# creamos un clase Paciente donde se recogerán los datos de las personas que lleguen a urgencias
class Paciente:
    def __init__(self,Id_Paciente, nombre, nivel_urgencia, horas_espera):
        self.Id_Paciente = Id_Paciente
        self.nombre = nombre
        self.nivel_urgencia = nivel_urgencia
        self.horas_espera = horas_espera
    
    def __lt__(self, other):
        return self.nivel_urgencia > other.nivel_urgencia
    
    def __gt__(self,other):
        return self.horas_espera < other.horas_espera
    
    def __str__(self):
        return f"{self.Id_Paciente} - {self.nombre}: Urgencia {self.nivel_urgencia}, Espera {self.horas_espera} horas"

# creamos un clase SalaEmergencias en la que gestionará el orden de prioridad
class SalaEmergencias:
    def __init__(self):
        self.max_heap = MaxHeap()       # esta parte se define para la urgencia
        self.min_heap = MinHeap()       # esta parte se define para los tiempos de espera
    
    # método para agregar a los pacientes que llegan
    def add_paciente(self, paciente):
        self.max_heap.push(paciente)
        self.min_heap.push(paciente)

    # método para ir sacando de la lista a los pacientes atendidos
    def atender_paciente(self):
        if not self.max_heap.is_empty() and self.max_heap.peek().nivel_urgencia == 10:
            return self.max_heap.pop()
        
        if not self.min_heap.is_empty() and self.max_heap.peek().horas_espera > 5:
            paciente_espera = self.min_heap.pop()
            self.max_heap.remove(paciente_espera)
            return paciente_espera
        
        return None
    
    # método para sacar el listado de pacientes ya atendidos
    def reportes(self, num_pacientes):
        reporte = []

        for p in range(num_pacientes):
            paciente = self.atender_paciente()
            if paciente:
                reporte.append(str(paciente))
            return reporte
    



