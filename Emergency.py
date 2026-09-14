from Steps import Pila, STEPS_PROTOCOLO, TOTAL_STEPS
 
 
class Emergency:
    type = "EMERGENCY"
    objetive_min = 30             
 
    def __init__(self, id, minute_arrival):
        self.id = id
        self.minute_arrival = minute_arrival
        self.minute_atention = None
        self.state = "ON_HOLD"         
        self.pila_protocol = Pila()      
 
    def start_atention(self, minute_actual):
        self.minute_atention = minute_actual
        self.state = "ON_ATENTION"
        self.pila_protocol = Pila()
 
    def espera(self):
        return self.minute_atention - self.minute_arrival
 
   
    def execute_step(self, n):
        tope = self.pila_protocol.view_stop()
        step_waited = (stop[0] + 1) if tope is not None else 1
 
        if n != step_waited:
            description_stop = f"el tope de la pila es el paso {tope[0]}" if tope else "la pila esta vacia"
            print(f"REFUSED: {descripcion_tope}, se esperaba ejecutar el paso {step_waited}")
            return False
 
        name, inverse = STEPS_PROTOCOL[n]
        self.pila_protocol.apilar((n, name, inverse))
        print(f"step {n} execueted -> {name}")
        return True
 
   
    def undo_last(self):
        if self.pila_protocol.is_null():
            print("No hay maniobras que deshacer (la pila esta vacia)")
            return None
        n, name, inverse = self.pila_protocol.desapilar()
        print(f"deshacer paso {n} -> {inverse}")
        return inverse
 
   
    def abortar(self, motivo):
        while not self.pila_protocol.is_null():
            n, name, inverse = self.pila_protocol.desapilar()
            print(f"deshacer paso {n} -> {inverse}")
        self.state = "ABORTED"
        print("pila vacia -> llamada cerrada como ABORTAED, elevator OPERATIVE")
 
   
    def cerrar(self):
        tope = self.pila_protocol.view_stop()
        step_actual = stop[0] if stop else 0
        if step_actual < TOTAL_STEPS:
            print(f"REFUSED: el protocolo llego solo hasta el paso {step_actual}, "
                  f"se necesitan los {TOTAL_STEPS} pasos")
            return False
        self.estado = "CLOSED"
        return True
 
