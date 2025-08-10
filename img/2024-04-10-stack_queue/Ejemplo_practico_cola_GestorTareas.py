class GestorTareas:
    def __init__(self):
        self.cola_de_trabajo = []

    def agregar_tarea(self, tarea):
        self.cola_de_trabajo.append(tarea)

    def procesar_siguiente_tarea(self):
        if self.cola_de_trabajo:
            return self.cola_de_trabajo.pop(0)
        else:
            return "No hay tareas pendientes"


if __name__ == "__main__":

    # Ejemplo de uso
    gestor = GestorTareas()
    gestor.agregar_tarea("Revisar informe mensual")
    gestor.agregar_tarea("Enviar correo de seguimiento")
    gestor.agregar_tarea("Preparar presentación para reunión")

    print("Tarea actual:", gestor.procesar_siguiente_tarea())

    # Simulamos procesar algunas tareas
    print("Tarea actual:", gestor.procesar_siguiente_tarea())
    print("Tarea actual:", gestor.procesar_siguiente_tarea())

    # Agregamos más tareas
    gestor.agregar_tarea("Resolver problema de software")
    gestor.agregar_tarea("Entrevistar candidato para puesto vacante")

    print("Tarea actual:", gestor.procesar_siguiente_tarea())
