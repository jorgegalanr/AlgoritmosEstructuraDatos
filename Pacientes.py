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


    



