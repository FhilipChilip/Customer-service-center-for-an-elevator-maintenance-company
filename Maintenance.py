class Maintenance:

    type = "MAINTENANCE"
    objetive_min = 240             
 
    def __init__(self, id, minute_arrival):
        self.id = id
        self.minute_arrival = minute_arrival
        self.minute_atention = None
        self.state = "ON_WAIT"          
 
    def start_atention(self, minute_actual):
        self.minute_atention = minute_actual
        self.state = "ON_ATENTION"
 
    def wait(self):
        return self.minuto_atencion - self.minuto_llegada
 
    def cumple_objetivo(self):
        return self.wait() <= self.objetive_min
 
    def closeCall(self):
        self.estado = "CERRADA"
        return True
 
