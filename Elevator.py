from Emergency import Emergency
from Maintenance import Maintenace
from Steps import Steps

class Elevator:

	def __init__(self, id, building, state, emergency, typeCall, minuteCall):

	self.id = id
	self.building = building
	self.state = state
	self.emergency = emergency
	self.typeCall = String
	self.minute_arrival = int


	def registerCall(self, id, type, min):
        elevator = self.park.search(lambda a: a.id == id)
        if elevator is None:
            print(f"REFUSED: the elevator {id} doesn´t exists on the park")
            return
 
        if elevator.state == "OUT_OF_SERVCICE":
            print(f"REFUSED: the elevator {id} is out of service")
            self.rechazadas_fuera_servicio += 1
            return
 
        if elevator.call_active is not None:
            print("REFUSED: the elevator has an active call")
            self.refused_duplicated += 1
            return
 
        Call = Emergency (id, min) if type == "EMERGENY" else Maintenance(id, min)
        elevator.call_active = call
 
        if tipo == "EMERGENCY":
            self.cola_emergencia.enqueue(call)
            position = len(self.cola_emergency)
        else:
            self.cola_maintenance.enqeue(call)
            position = len(self.cola_maintenance)
 
        print(f"enqueued on {type} (position {position})")
 

	def loadElevator(self, id, building, state, emergency):
        if self.parque.buscar(lambda a: a.codigo == codigo) is not None:
            print(f"REFUSED: The ID {id} already exists on the park (duplicated)")
            return False
        self.park.ad(Elevator(id, building, state, emergency))
        print(f"Ascensor {id} ({building}) add to park, state: {state}")
        return True
				
	def attendNext(self):

		if self.cola_emergencia.esta_vacia() and self.cola_mantenimiento.esta_vacia():
            print("No hay llamadas en espera (las dos colas estan vacias)")
            return
 
        toca_mantenimiento = (
            self.emergencias_desde_ultimo_mantenimiento >= self.EMERGENCIAS_ANTES_DE_MANTENIMIENTO
            and not self.cola_mantenimiento.esta_vacia()
        )
 
        if toca_mantenimiento:
            llamada = self.cola_mantenimiento.desencolar()
            self.emergencias_desde_ultimo_mantenimiento = 0
        elif not self.cola_emergencia.esta_vacia():
            llamada = self.cola_emergencia.desencolar()
            self.emergencias_desde_ultimo_mantenimiento += 1
        else:
            llamada = self.cola_mantenimiento.desencolar()
            self.emergencias_desde_ultimo_mantenimiento = 0
 
        ascensor = self.parque.buscar(lambda a: a.codigo == llamada.codigo)
        ascensor.estado = "EN_ATENCION"
        llamada.iniciar_atencion(minuto_actual)
 
        espera = llamada.espera()
        cumple = llamada.cumple_objetivo()
 
        self.atendidas[llamada.tipo] += 1
        self.suma_espera[llamada.tipo] += espera
        self.max_espera[llamada.tipo] = max(self.max_espera[llamada.tipo], espera)
        if cumple:
            self.cumplen_objetivo[llamada.tipo] += 1
 
        self.llamada_en_curso = llamada
        self.ascensor_en_curso = ascensor
 
        etiqueta = "CUMPLE" if cumple else "INCUMPLE"
        print(f"{ascensor.codigo} | {llamada.tipo} | espera {espera} min -> {etiqueta} "
              f"(objetivo {llamada.objetivo_min})")

	def createReport(self):



