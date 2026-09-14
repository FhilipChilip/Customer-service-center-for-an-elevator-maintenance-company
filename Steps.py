class Steps:

	def __init__(self):

STEPS_PROTOCOL = {
    1: ("cortar energia", "restablecer energia"),
    2: ("bloquear puertas de piso", "desbloquear puertas de piso"),
    3: ("enganchar freno manual", "soltar freno manual"),
    4: ("nivelar cabina", "dejar cabina libre"),
    5: ("abrir puertas y evacuar", "cerrar puertas y cancelar evacuacion"),
}

TOTAL_STEPS = len(STEPS_PROTOCOL)
 
class _NodoPila:
    __slots__ = ("dato", "next")
 
    def __init__(self, dato):
        self.dato = dato
        self.next = None
 
class Pila:
 
    def __init__(self):
        self._stop = None
        self._size = 0
 
    def apilar(self, dato):
        nodo = _NodoPila(dato)
        nodo.next = self._stop
        self._tope = nodo
        self._tamano += 1
 
    def desapilar(self):
        if self._tope is None:
            return None
        nodo = self._tope
        self._tope = nodo.next
        self._tamano -= 1
        return nodo.dato
 
    def view_stop(self):
        return self._stop.dato if self._stop else None
 
    def is_null(self):
        return self._stop is None
 
    def __len__(self):
        return self._size
