"""
Módulo que define las clases `Vehiculo`, `Motor`, `Coche`, `Camion`, `Yate` y `Moto`.

**Autor:**

* Andres Cerdas Padilla

**Fecha:**

* 2024-03-13

"""


class Vehiculo:
    def __init__(self, modelo: str, año: int, chasis: str, motor: "Motor"):

        if not chasis in ["A", "B"]:
            raise ValueError("Este chasis no es válido.")

        self.modelo = modelo
        self.año = año
        self.chasis = chasis
        self.motor = motor

    def calcular_consumo_gasolina(self) -> float:
        return (
            1.1 * self.motor.potencia
            + 0.2 * self.motor.peso
            - (0.3 if self.chasis == "A" else 0.5)
        )

    def __repr__(self) -> str:
        """Devuelve una representación textual del  vehículo."""
        return f" \n Datos del Vehículo: {self.modelo}, Año: {self.año}, Chasis: {self.chasis}, Motor: {self.motor} \n "


class Motor:
    def __init__(self, tipo: str, potencia: float, peso: float):
        self.tipo = tipo
        self.potencia = potencia
        self.peso = peso

    def __repr__(self) -> str:
        """Devuelve una representación textual del  motor."""
        return f"{self.tipo}, Potencia: {self.potencia}, Peso: {self.peso}"


#================================= Tipos de Vehiculos ===============================================#

class Coche(Vehiculo):
    def __init__(self, modelo: str, año: int, chasis: str, motor: "Motor", puertas: int):
        super().__init__(modelo, año, chasis, motor)
        self.puertas = puertas

    def __repr__(self) -> str:
        """Devuelve una representación textual del  coche"""
        return f"{super().__repr__()}, Puertas: {self.puertas}"
    

class Camion(Vehiculo):
    def __init__(self, modelo: str, año: int, chasis: str, motor: "Motor", capacidad_carga: float):
        super().__init__(modelo, año, chasis, motor)
        self.capacidad_carga = capacidad_carga

    def __repr__(self) -> str:
        """Devuelve una representación textual del  vehículo."""
        return f"{super().__repr__()}, Capacidad de carga: {self.capacidad_carga} ton"


class Yate(Vehiculo):
    def __init__(self, modelo: str, año: int, chasis: str, motor: "Motor", eslora: float):
        super().__init__(modelo, año, chasis, motor)
        self.eslora = eslora

    def __repr__(self) -> str:
        """Devuelve una representación textual del  vehículo."""
        return f"{super().__repr__()}, Eslora: {self.eslora} m"


class Moto(Vehiculo):
    def __init__(self, modelo: str, año: int, chasis: str, motor: "Motor", cilindrada: int):
        super().__init__(modelo, año, chasis, motor)
        self.cilindrada = cilindrada

    def __repr__(self) -> str:
        """Devuelve una representación textual del  vehículo."""
        return f"{super().__repr__()}, Cilindrada: {self.cilindrada} cc"