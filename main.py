"""
Módulo principal del programa para la gestión de vehículos.

Este módulo utiliza las clases definidas en `vehiculo.py` para crear, mostrar y gestionar una lista de vehículos.

**Autores:**

* Bard, el modelo de lenguaje de Google AI.

**Fecha:**

* 2024-03-13

"""
from fastapi import fastAPI
from Vehiculo import Vehiculo, Motor, Coche, Camion, Yate, Moto

#=================================== Funciones ========================================#

def crear_vehiculo():
    """
    Crea un nuevo vehículo según el tipo introducido por el usuario.

    **Parámetros:**

    * Esta función tiene parámetros aunque no se definan explícitamente. Los parámetros se pasan a la
    función a través de la entrada del usuario y son los siguientes:
    -tipo_vehiculo (str): Tipo de vehículo a crear.
    -modelo (str): Modelo del vehículo.
    -año (int): Año del vehículo.
    -chasis (str): Tipo de chasis del vehículo.
    -motor (Motor): Objeto Motor del vehículo.

    **Retorno:**

    * Un objeto `Vehiculo` de la clase correspondiente.
    """

    tipo_vehiculo = input("Introduzca el tipo de vehículo sin acentos a continuación (coche, camión, yate o moto) : ").lower()
    modelo = input("Introduzca el modelo: ")
    año = int(input("Introduzca el año: "))
    chasis = input("Introduzca el tipo de chasis (A/B): ")
    chasis = chasis.upper()
    potencia = float(input("Introduzca la potencia del motor: "))
    peso = float(input("Introduzca el peso del motor: "))
    motor = Motor("Gasolina", potencia, peso)

    if tipo_vehiculo == "coche":
        puertas = int(input("Introduzca el número de puertas: "))
        return Coche(modelo, año, chasis, motor, puertas)
    elif tipo_vehiculo == "camion":
        capacidad_carga = float(input("Introduzca la capacidad de carga: "))
        return Camion(modelo, año, chasis, motor, capacidad_carga)
    elif tipo_vehiculo == "yate":
        eslora = float(input("Introduzca la eslora (longitud): "))
        return Yate(modelo, año, chasis, motor, eslora)
    elif tipo_vehiculo == "moto":
        cilindrada = int(input("Introduzca la cilindrada: "))
        return Moto(modelo, año, chasis, motor, cilindrada)
    else:
        print("Tipo de vehículo no válido.\n")
        return None

def mostrar_vehiculos(vehiculos: list[Vehiculo]):
    """
    Muestra una lista de vehículos con su información y consumo de gasolina.

    **Parámetros:**

    * `vehiculos`: Una lista de objetos `Vehiculo`.

    **Retorno:**

    * Ninguno.
    """

    for vehiculo in vehiculos:
        print(vehiculo)
        if isinstance(vehiculo, Coche):
            print(f"Puertas: {vehiculo.puertas}")
        elif isinstance(vehiculo, Camion):
            print(f"Capacidad de carga: {vehiculo.capacidad_carga} ton")
        elif isinstance(vehiculo, Yate):
            print(f"Eslora: {vehiculo.eslora} m")
        elif isinstance(vehiculo, Moto):
            print(f"Cilindrada: {vehiculo.cilindrada} cc")
        print(f"Consumo de gasolina: {vehiculo.calcular_consumo_gasolina()} L/100km")

def main():
    """
    Función principal del programa.

    **Parámetros:**

    * Ninguno.

    **Retorno:**

    * Ninguno.
    """

    vehiculos = []

    while True:
        # Menú principal
        print("""
        **Bienvenido al programa de gestión de vehículos**

        1. Crear vehículo
        2. Mostrar vehículos
        0. Salir

        """)

        opcion = input("Introduzca una opción: ")

        if opcion == "1":
            vehiculo = crear_vehiculo()
            if vehiculo:
                vehiculos.append(vehiculo)
        elif opcion == "2":
            mostrar_vehiculos(vehiculos)
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()