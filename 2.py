class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

def destruirPares(lista):
    pila = Pila()

    for elemento in lista:
        if not pila.esta_vacia() and pila.items[-1] == elemento:
            pila.desapilar()
        else:
            pila.apilar(elemento)

    return len(pila.items)

# Ejemplo 1
entrada1 = [2, 1, 1, 3, 4]
salida1 = destruirPares(entrada1)
print(f"Ejemplo 1 - Entrada: {entrada1}, Salida: {salida1}")

# Ejemplo 2
entrada2 = [2, 1, 1, 2]
salida2 = destruirPares(entrada2)
print(f"Ejemplo 2 - Entrada: {entrada2}, Salida: {salida2}")
