<h1 aling="center"> #Programa de Gestión de Vehículos </h1>

Este programa te permite gestionar una lista de vehículos, incluyendo:

- **Crear** vehículos de diferentes tipos (coche, camión, yate, moto).
- **Mostrar** la información de los vehículos, incluyendo el consumo de gasolina.
- **Calcular** el consumo de gasolina de cada vehículo.  

<h3>##Inquietudes y decisiones</h3>

Al desarrollar este programa, se tuvieron en cuenta las siguientes inquietudes:

**¿Cómo representar la diversidad de tipos de vehículos?** Se decidió utilizar herencia para crear clases específicas para cada tipo de vehículo (coche, camión, yate, moto).<p>

**¿Cómo calcular el consumo de gasolina?** Se desarrolló una fórmula que toma en cuenta la potencia del motor, el peso del motor y el tipo de chasis.<p>

**¿Cómo mostrar la información de los vehículos de forma clara y organizada?** Se utilizó una función para mostrar la información de cada vehículo, incluyendo el consumo de gasolina.<p>

<h3>##Técnicas y arquitectura</h3>

El programa está escrito en Python y utiliza las siguientes técnicas:

* __Programación orientada a objetos__: Se utilizan clases para representar los diferentes tipos de vehículos.
* __Hereditaria__: Se utiliza la herencia para crear clases específicas para cada tipo de vehículo.
* __Polimorfismo__: Se utiliza el polimorfismo para mostrar la información de los vehículos de forma clara y organizada.

<h3>## :hammer: La arquitectura del programa es la siguiente:</h3>

**Módulo** __main.py__: Contiene la función principal del programa, que permite al usuario crear, mostrar y gestionar una lista de vehículos.<p>
**Módulo** __vehiculo.py__: Define las clases Vehiculo, Motor, Coche, Camion, Yate y Moto.

**Funcionamiento del algoritmo:**<p>
El algoritmo principal del programa funciona de la siguiente manera:

1. Se crea una lista vacía para almacenar los vehículos.
2. Se presenta un menú al usuario con las opciones de crear un vehículo, mostrar los vehículos o salir del programa.
3. Si el usuario elige crear un vehículo, se le pide que introduzca la información del vehículo, como el tipo de vehículo, el modelo, el año, el chasis y la potencia del motor.
4. Se crea un nuevo objeto Vehiculo de la clase correspondiente al tipo de vehículo seleccionado.
5. Se añade el nuevo objeto Vehiculo a la lista.
6. Si el usuario elige mostrar los vehículos, se muestra la información de cada vehículo en la lista, incluyendo el consumo de gasolina. 
7. Si el usuario elige salir del programa, se termina el programa. 

El diagrama  UML que representa esta arquitectura se encuentra en el archivo "Diagrama_de_clases.jpeg"

**Autor:**

* Andrés Cerdas Padilla
