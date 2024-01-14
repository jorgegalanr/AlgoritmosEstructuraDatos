# Fase Implementación
from Heap  import MaxHeap, MinHeap
import random


# creamos un clase Paciente donde se recogerán los datos de las personas que lleguen a urgencias
class Paciente:
    def __init__(self, id_paciente, nombre, nivel_urgencia, horas_espera):
            self.id_paciente = id_paciente
            self.nombre = nombre
            self.nivel_urgencia = nivel_urgencia
            self.horas_espera = horas_espera
            self.atendido = False
        
    def __lt__(self, other):
            return self.nivel_urgencia < other.nivel_urgencia
        
    def __gt__(self,other):
            return self.horas_espera < other.horas_espera
        
    def __str__(self):
            return f"Entrada nº{self.id_paciente} - {self.nombre}: Urgencia {self.nivel_urgencia}, Espera {self.horas_espera} horas"

# creamos un clase SalaEmergencias en la que gestionará el orden de prioridad
class SalaEmergencias:
    def __init__(self):
            self.max_heap = MaxHeap()  # Urgencia
            self.min_heap = MinHeap()  # Tiempo de espera

    def add_paciente(self, paciente):
            self.max_heap.push(paciente)
            self.min_heap.push(paciente)

    def atender_pacientes(self):
        reporte = []
        pacientes_vistos = set()  # Utilizamos un conjunto para registrar los ID de pacientes ya atendidos

        while not self.max_heap.is_empty():
            paciente_urgente = self.max_heap.peek()
            paciente_espera = self.min_heap.peek()

            if paciente_urgente.nivel_urgencia == 10 and not paciente_urgente.atendido and paciente_urgente.id_paciente not in pacientes_vistos:
                paciente_atendido = self.max_heap.pop()
                paciente_atendido.atendido = True
                pacientes_vistos.add(paciente_atendido.id_paciente)
                reporte.append(paciente_atendido)
            elif paciente_espera.horas_espera > 5 and not paciente_espera.atendido and paciente_espera.id_paciente not in pacientes_vistos:
                paciente_atendido = self.min_heap.pop()
                paciente_atendido.atendido = True
                pacientes_vistos.add(paciente_atendido.id_paciente)
                reporte.append(paciente_atendido)
            else:
                paciente_atendido = self.max_heap.pop()
                if not paciente_atendido.atendido and paciente_atendido.id_paciente not in pacientes_vistos:
                    paciente_atendido.atendido = True
                    pacientes_vistos.add(paciente_atendido.id_paciente)
                    reporte.append(paciente_atendido)

            # Limpiamos los montículos de pacientes ya atendidos
            while not self.max_heap.is_empty() and self.max_heap.peek().atendido:
                self.max_heap.pop()
            while not self.min_heap.is_empty() and self.min_heap.peek().atendido:
                self.min_heap.pop()

        return reporte

    def reportes(self):
        # Atender pacientes según la lógica establecida
        pacientes_atendidos = self.atender_pacientes()
        # Imprimir reporte de pacientes atendidos
        for paciente in pacientes_atendidos:
            print(paciente)

# Creamos la sala de emergencia
sala_emergencia = SalaEmergencias()

    # Creación de los pacientes
nombres = ["Juan", "Giussepe", "Miguel", "Antonio", "Maria", "Marta", "Emma", "Hellen", "Sandra", "Carlos", "Luis", "Josep", "Elisa", "Eloise", "David", "Eduardo"]
id_paciente = 0
for _ in range(20):
        nombre = random.choice(nombres)
        nivel_urgencia = random.randint(1, 10)
        horas_espera = random.randint(0, 10)
        paciente = Paciente(id_paciente, nombre, nivel_urgencia, horas_espera)
        sala_emergencia.add_paciente(paciente)
        id_paciente += 1

    # Generamos el reporte con los pacientes atendidos.
sala_emergencia.reportes()