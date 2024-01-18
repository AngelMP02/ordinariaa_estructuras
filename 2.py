class NodoPila:
    def __init__(self, valor=None, sig=None):
        self.valor = valor
        self.sig = sig

class Pila:
    def __init__(self):
        self.cima = None
        self.tam = 0

    def push(self, valor):
        self.cima = NodoPila(valor, self.cima)
        self.tam += 1

    def pop(self):
        ret = self.cima.valor
        self.cima = self.cima.sig
        self.tam -= 1
        return ret

    def peek(self):
        return self.cima.valor

    def is_empty(self):
        return self.tam == 0

    def __str__(self):
        cad = '['
        aux = self.cima
        while aux:
            cad += str(aux.valor) + ' '
            aux = aux.sig
        return cad.strip() + ']'

def destruirPares(lista):
    pila = Pila()

    for elemento in lista:
        if not pila.is_empty() and pila.peek() == elemento:
            pila.pop()
        else:
            pila.push(elemento)

    # La pila ahora contiene la lista final sin pares consecutivos iguales
    lista_final = []
    while not pila.is_empty():
        lista_final.insert(0, pila.pop())

    return len(lista_final)


entrada1 = [2, 1, 1, 3, 4]
salida1 = destruirPares(entrada1)
print(f"Ejemplo 1:\nEntrada: {entrada1}\nSalida: {salida1}")

entrada2 = [2, 1, 1, 2]
salida2 = destruirPares(entrada2)
print(f"\nEjemplo 2:\nEntrada: {entrada2}\nSalida: {salida2}")
