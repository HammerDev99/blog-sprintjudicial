class NavegadorWeb:
    def __init__(self):
        self.historial = []

    def abrir_pagina(self, url):
        self.historial.append(url)

    def retroceder(self):
        if len(self.historial) > 1:
            self.historial.pop()  # Retrocedemos eliminando la página actual del historial
            return self.historial[-1]  # Devolvemos la URL de la página anterior
        else:
            return "No hay páginas anteriores en el historial"

    def adelantar(self):
        # Podríamos implementar la funcionalidad de avanzar utilizando otra pila para las páginas adelantadas
        pass


if __name__ == "__main__":

    # Ejemplo de uso
    navegador = NavegadorWeb()
    navegador.abrir_pagina("https://www.ejemplo.com/pagina1")
    navegador.abrir_pagina("https://www.ejemplo.com/pagina2")
    navegador.abrir_pagina("https://www.ejemplo.com/pagina3")

    print("Página actual:", navegador.historial[-1])

    pagina_anterior = navegador.retroceder()
    print("Página anterior:", pagina_anterior)

    pagina_anterior = navegador.retroceder()
    print("Página anterior:", pagina_anterior)
