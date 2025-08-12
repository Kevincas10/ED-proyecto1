class Trabajador:
    def __init__(self, id, nombre, tipo_servicio, calificacion):
        self.id = id 
        self.nombre = nombre  
        self.tipo_servicio = tipo_servicio
        self.calificacion = calificacion  

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Tipo: {self.tipo_servicio}, Calificación: {self.calificacion}"

    def __lt__(self, other):
        return self.id < other.id

    def __eq__(self, other):
        return self.id == other.id
    

    