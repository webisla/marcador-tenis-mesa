# marcador_tenis_mesa.py
# Aplicación de marcador de tenis de mesa - Python
# Autor: [Tu Nombre]
# Versión: 1.0
# Descripción: Permite registrar puntuaciones, anunciar ganador y reiniciar partidos.

class TableTennisGame:
    def __init__(self, jugador1, jugador2):
        """
        Inicializa los jugadores y puntuaciones.
        """
        self.jugadores = {jugador1: 0, jugador2: 0}
        self.ganador = None

    def sumar_punto(self, jugador):
        """
        Suma un punto al jugador indicado.
        """
        if jugador in self.jugadores:
            self.jugadores[jugador] += 1
            self.verificar_ganador()

    def restar_punto(self, jugador):
        """
        Resta un punto solo si la puntuación es mayor a cero.
        """
        if jugador in self.jugadores and self.jugadores[jugador] > 0:
            self.jugadores[jugador] -= 1
            self.ganador = None  # Permite corregir si se restó después de anunciar ganador

    def verificar_ganador(self):
        """
        Verifica si algún jugador ha ganado (11+ puntos y ventaja de 2).
        """
        nombres = list(self.jugadores.keys())
        puntos = list(self.jugadores.values())
        if ((puntos[0] >= 11 or puntos[1] >= 11) and abs(puntos[0] - puntos[1]) >= 2):
            self.ganador = nombres[0] if puntos[0] > puntos[1] else nombres[1]

    def reiniciar(self):
        """
        Reinicia puntuaciones y estado de ganador.
        """
        for jugador in self.jugadores:
            self.jugadores[jugador] = 0
        self.ganador = None

    def mostrar_puntuaciones(self):
        """
        Muestra las puntuaciones actuales por consola.
        """
        print("---- Marcador Actual ----")
        for jugador, puntos in self.jugadores.items():
            print(f"{jugador}: {puntos}")
        if self.ganador:
            print(f"¡Ganador: {self.ganador}!")
        print("-------------------------")

def main():
    # Solicita nombres de jugadores por consola
    jugador1 = input("Ingrese nombre del Jugador 1: ")
    jugador2 = input("Ingrese nombre del Jugador 2: ")
    juego = TableTennisGame(jugador1, jugador2)

    while not juego.ganador:
        juego.mostrar_puntuaciones()
        accion = input("¿Quién anotó (+1) o deshacer (-1)? Indique nombre (o 'fin' para terminar): ")
        if accion == "fin":
            break
        elif accion in juego.jugadores:
            tipo = input("Escriba '+1' para sumar punto, '-1' para restar punto: ")
            if tipo == "+1":
                juego.sumar_punto(accion)
            elif tipo == "-1":
                juego.restar_punto(accion)
        else:
            print("Nombre no válido. Intente de nuevo.")

    juego.mostrar_puntuaciones()
    if input("¿Nuevo juego? (s/n): ").lower() == 's':
        juego.reiniciar()
        main()

if __name__ == "__main__":
    main()
