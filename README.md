https://github.com/jorgegalanr/AlgoritmosEstructuraDatos

Jorge Galán Rodríguez

# Proyecto gestión de atención al paciente en Sala de Urgencias

## **Explicación proyecto**

El proyecto consta de 3 ficheros: 

- Fichero Nodo.py, le damos formato al nodo inicial.
- Fichero Heap.py, donde implementamos la lógica de montículos para la clase Heap y las clases HeapMin y HeapMax, heredan los métodos de Heap. 
- Fichero Pacientes.py, donde se implementa la lógica para el caso actual.

En el ejercicio se ha implementado un montículo con decisión binaria:
 1  1  --> urgencia 10
 1  0  --> urgencia 10
 0  1  --> horas de espera > 5
 0  0  --> no cumple ninguna de las 2 anteriores se ordena por urgencia

1) Arriba del montículo debe quedar pacientes urgencia 10. 
2) Una vez que se ha tratado a todos los pacientes de urgencia 10, se trata los que llevan más de 5 horas.
3) Una vez que se ha tratato lo anteriores, el resto se trata de mayor a menor urgencia.

Los datos de los pacientes se generan aleatoriamente para hacer pruebas de lógica, pero sería totalmente utilizable con datos reales. 

**Conclusión**
Es una práctica que si se sabe utilizar correctamente tiene muchas aplicaciones en las que se necesite ordenar si se tiene 2 posibles decisiones prioritarias. 
Por ejemplo, quiero hacer un analisis de mercado porque quiero cambiar de piso y me quiero comprar una propiedad en mi zona, pero que exista una buena oferta y oportunidad de chollo. 
- Mi primera prioridad sean propiedad con un rebaje mayor a 20% en menos de 6 meses.
- Segunda prioridad los que estén a menos de 3km de distancia de mi ubicacion actual. 
- Restante prioridad por cercanía a mi propiedad actual. 




