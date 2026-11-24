
from Actividad import Actividad # De el archivo actividad trae la clase actividad 
class Reservas:
    def __init__(self,identificador : str , persona : str , estado : str ):
        self.identificador = identificador
        self.persona = persona
        self.estado = estado
        self.actividades : list [Actividad] = [] # Guarda

    def anadir (self, actividad : Actividad) -> None:
        self.actividad.append(actividad)


        
        



        