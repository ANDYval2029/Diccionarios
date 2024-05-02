#Valenzuela Vargas Andrea
import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
       
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def angle(self, other):
        dot_product = self.x * other.x + self.y * other.y
        mag_self = math.sqrt(self.x**2 + self.y**2)
        mag_other = math.sqrt(other.x**2 + other.y**2)
        return math.atan2(other.y, other.x) - math.atan2(self.y, self.x)

# Ejemplo de uso
v1 = Vector2D(8, 10)
v2 = Vector2D(7, 5)

# Suma de vectores
suma = v1 + v2
print("Suma:", suma.x, suma.y)

# Resta de vectores
resta = v1 - v2
print("Resta:", resta.x, resta.y)

# Producto punto
producto_punto = v1.dot_product(v2)
print("Producto Punto:", producto_punto)

# Magnitud de un vector
magnitud_v1 = v1.magnitude()
print("Magnitud v1:", magnitud_v1)

# Calcular ángulo entre v1 y v2
angulo = v1.angle(v2)

# Convertir a grados si es necesario
angulo_grados = math.degrees(angulo)

print("Ángulo entre v1 y v2:", angulo, "radianes o", angulo_grados, "grados")

