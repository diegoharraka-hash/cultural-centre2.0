class Actividad:
    siguiente_id = 1 # esto va a actuar como un contador 

    def __init__(self , titulo : str , nombre : str , fecha : str , aforo : int , precio_base : float,):
        self.titulo = titulo

        self.codigo = f"ACT-{self.siguiente_id}" # cada vez que llamemos al atributo codigo muestra el contador inicial
        self.siguiente_id += 1 # cada vez que creamos el la siguiente actividad va a aumentar automaticamente 

        self.nombre = nombre 
        self.fecha = fecha 
        self.aforo = aforo 
        self.precio_base = precio_base

    def resumen ():
        return "f ({self.titulo}) , ({self.codigo}) , ({self.nombre}) , ({self.fecha}) , ({self.aforo}) , ({self.precio_base}) "

    @property # nos va a permitir proteger nuestros datos 
    def aforo (self) -> int:
        return self.aforo

    def precio_base (self) -> float :
        return self.precio_base

    @aforo.setter
    def aforo (self):
        if self.aforo < 0 :
            return ValueError

    @precio_base.setter
    def precio_base (self):
        if self.precio_base < 0 :
            return ValueError



        







    





