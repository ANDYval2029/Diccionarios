class CarreraUniversitaria:
    def __init__(self, nombre_carrera):
        self.nombre_carrera = nombre_carrera

    def __str__(self):
        return f"Carrera: {self.nombre_carrera}"


class Alumno:
    def __init__(self, nombre, edad, notas, carrera):
        self.nombre = nombre
        self.edad = edad
        self.notas = notas
        self.carrera = carrera


    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Notas: {self.notas}, {self.carrera}"


class CienciasFisicoMatematicas1(CarreraUniversitaria):
    def __init__(self, nombre_carrera):
        super().__init__(nombre_carrera)
        
class CienciasFisicoMatematicas2(CarreraUniversitaria):
    def __init__(self, nombre_carrera):
        super().__init__(nombre_carrera)
        
class CienciasFisicoMatematicas3(CarreraUniversitaria):
    def __init__(self, nombre_carrera):
        super().__init__(nombre_carrera)



def main():
    cienciasFisicoMatematicas = CienciasFisicoMatematicas1("Electronica")
    cienciasFisicoMatematicas1 = CienciasFisicoMatematicas2("Matematicas")
    cienciasFisicoMatematicas2 = CienciasFisicoMatematicas3("Fisica")

    alumno1 = Alumno("Francisco", 20, [80, 75, 90], cienciasFisicoMatematicas)
    alumno2 = Alumno("Marta", 21, [85, 90, 95], cienciasFisicoMatematicas1)
    alumno3 = Alumno("Jesus", 19, [9,10,10], cienciasFisicoMatematicas2)

    print("Información del alumno 1:")
    print(alumno1)

    print("\nInformación del alumno 2:")
    print(alumno2)
    
    print("\nInformación del alumno 3:")
    print(alumno3)


if __name__ == "__main__":
    main()
