#16 problemas
#programa para multiplicar los elementos de un diccionario

#1 Definir un diccionario
diccionario = {'a': 5, 'b': 6, 'c': 7}

# Multiplicar todos los valores por un número específico
factor = 3
resultado = {key: value * factor for key, value in diccionario.items()}

print(resultado)

#2 programa para eliminar la cable de un diccionario

# Definir un diccionario
mi_diccionario = {'A': 1, 'b': 2, 'C': 3}

# Mostrar el diccionario original
print("Diccionario original:", mi_diccionario)

# Clave a eliminar
clave_a_eliminar = 'C'

# Verificar si la clave está presente en el diccionario antes de eliminarla
if clave_a_eliminar in mi_diccionario:
    del mi_diccionario[clave_a_eliminar]
    print("Clave '{}' eliminada del diccionario.".format(clave_a_eliminar))
else:
    print("La clave '{}' no está presente en el diccionario.".format(clave_a_eliminar))

# Mostrar el diccionario después de eliminar la clave
print("Diccionario actualizado:", mi_diccionario)

#3 programa que convierta 2 listas en un diccionario

# Definir dos listas
keys = ['a', 'b', 'c']
values = [1, 2, 3]

# Convertir las listas en un diccionario
mi_diccionario = dict(zip(keys, values))

# Mostrar el diccionario resultante
print("Diccionario resultante:", mi_diccionario)

#4 programa para ordenar un diccionario dado por clave

# Definir un diccionario
mi_diccionario = {'y': 2, 'x': 1, 'z': 3}

# Ordenar el diccionario por las claves
diccionario_ordenado = dict(sorted(mi_diccionario.items()))

# Mostrar el diccionario ordenado
print("Diccionario ordenado por clave:")
for clave, valor in diccionario_ordenado.items():
    print(clave, ":", valor)

#5 valores mximos y minimos de un diccionario 

# Definir un diccionario
mi_diccionario = {'a': 10, 'b': 5, 'c': 20, 'd': 15}

# Obtener el valor máximo y la clave correspondiente
max_valor = max(mi_diccionario.values())
max_clave = max(mi_diccionario, key=mi_diccionario.get)

# Obtener el valor mínimo y la clave correspondiente
min_valor = min(mi_diccionario.values())
min_clave = min(mi_diccionario, key=mi_diccionario.get)

# Mostrar los resultados
print("Valor máximo:", max_valor, "clave:", max_clave)
print("Valor mínimo:", min_valor, "clave:", min_clave)

#6 obtener un diccionario a partir de los campos de un objeto
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 30, "Madrid")

# Obtener el diccionario a partir de los campos del objeto
diccionario_persona = persona1.__dict__

# Mostrar el diccionario
print(diccionario_persona)

#7 eliminar duplicados del diccionario

# Definir un diccionario con duplicados
mi_diccionario = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

# Crear un nuevo diccionario sin duplicados
diccionario_sin_duplicados = {}
for clave, valor in mi_diccionario.items():
    if valor not in diccionario_sin_duplicados.values():
        diccionario_sin_duplicados[clave] = valor

# Mostrar el nuevo diccionario
print("Diccionario sin duplicados:", diccionario_sin_duplicados)

#8 programa para verificar si un diccionario está vacío o no

# Definir un diccionario
mi_diccionario = {}

# Verificar si el diccionario está vacío
if not mi_diccionario:
    print("El diccionario está vacío")
else:
    print("El diccionario no está vacío")

#9 

# Definir la lista de diccionarios original
lista_diccionarios = [{'Matematicas': 90, 'ciencia': 92}, {'matematicas': 89, 'ciencia': 94}, {'Matematicas': 92, 'ciencia': 88}]

# Función para extraer una lista de valores donde la asignatura sea igual a "Ciencia" o "Matemáticas"
def extraer_valores(diccionarios, asignatura):
    valores_asignatura = []
    for diccionario in diccionarios:
        # Convertir todas las claves del diccionario a minúsculas para hacer la comparación insensible a mayúsculas/minúsculas
        diccionario_min = {k.lower(): v for k, v in diccionario.items()}
        if asignatura.lower() in diccionario_min:
            valores_asignatura.append(diccionario_min[asignatura.lower()])
    return valores_asignatura

# Asignatura deseada
asignatura = "Ciencia"

# Extraer una lista de valores donde la asignatura sea igual a "Ciencia"
valores_ciencia = extraer_valores(lista_diccionarios, asignatura)
print(f"Lista de valores de la asignatura '{asignatura}': {valores_ciencia}")

# Asignatura deseada
asignatura = "Matemáticas"

# Extraer una lista de valores donde la asignatura sea igual a "Matemáticas"
valores_matematicas = extraer_valores(lista_diccionarios, asignatura)
print(f"Lista de valores de la asignatura '{asignatura}': {valores_matematicas}")

#10 programa para encontrar la longitud de un diccionario de valores

# Definir un diccionario
mi_diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Encontrar la longitud del diccionario de valores
longitud_diccionario_valores = len(mi_diccionario.values())

# Mostrar la longitud del diccionario de valores
print("Longitud del diccionario de valores:", longitud_diccionario_valores)

#11 programa para obtener la profundidad de un diccionario

def profundidad_diccionario(diccionario):
    if isinstance(diccionario, dict):
        if diccionario:
            return 1 + max(profundidad_diccionario(valor) for valor in diccionario.values())
        else:
            return 1
    else:
        return 0

# Ejemplo de diccionario
mi_diccionario = {'a': {'b': {'c': 1, 'd': 2}}, 'e': 3}

# Obtener la profundidad del diccionario
profundidad = profundidad_diccionario(mi_diccionario)

# Mostrar la profundidad del diccionario
print("Profundidad del diccionario:", profundidad)

#12 programa para acceder al elemento de la clave de un diccionario por índice. Salida esperada: física matemáticas química

# Definir el diccionario
mi_diccionario = {'quimica': 85, 'fisica': 90, 'matematicas': 95}

# Obtener las claves del diccionario y ordenarlas
claves_ordenadas = sorted(mi_diccionario.keys())

# Iterar sobre las claves ordenadas y mostrar sus valores
for clave in claves_ordenadas:
    print(clave)

#13 programa en para convertir un diccionario en una lista de listas

# Definir el diccionario original
diccionario_original = {1: 'rojo', 2: 'verde', 3: 'negro', 4: 'blanco', 5: 'negro'}

# Convertir el diccionario en una lista de listas
lista_de_listas = [[clave, valor] for clave, valor in diccionario_original.items()]

# Mostrar la lista de listas resultante
print("Lista de listas:", lista_de_listas)

#14 programa para filtrar números pares de un diccionario de valores
# Definir el diccionario original
diccionario_original = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}

# Filtrar números pares de los valores del diccionario
diccionario_filtrado = {clave: list(filter(lambda x: x % 2 == 0, valores)) for clave, valores in diccionario_original.items()}

# Mostrar el diccionario filtrado
print("Diccionario filtrado:", diccionario_filtrado)

# Definir el segundo diccionario original
diccionario_original_2 = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}

# Filtrar números pares de los valores del segundo diccionario
diccionario_filtrado_2 = {clave: list(filter(lambda x: x % 2 == 0, valores)) for clave, valores in diccionario_original_2.items()}

# Mostrar el segundo diccionario filtrado
print("Diccionario filtrado:", diccionario_filtrado_2)








