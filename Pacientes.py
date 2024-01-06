# Fase Implementación

# creamos un clase Paciente donde se recogerán los datos de las personas que lleguen a urgencias
class Paciente:
    def __init__(self,ID_Paciente, nombre, nivel_urgencia, horas_espera):
        self.nombre = nombre
        self.nivel_urgencia = nivel_urgencia
        self.horas_espera = horas_espera
