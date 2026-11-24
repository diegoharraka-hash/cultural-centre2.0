class Actividad:
    siguiente_id = 1 # esto va a actuar como un contador 



    def __init__(self , titulo : str , nombre : str , fecha : str , aforo : int , precio_base : float,):
        
        self.titulo = titulo


        self.codigo = f"ACT-{self.siguiente_id}" # cada vez que llamemos al atributo codigo muestra el contador inicial
        self.siguiente_id += 1

        self.nombre = nombre 
        self.fecha = fecha 
        self.aforo = aforo 
        self.precio_base = precio_base

    def resumen (self):
        return f"{self.titulo} | {self.nombre} | {self.fecha}| {self.aforo} | {self.precio_base} "

    @property # nos va a permitir proteger nuestros datos 
    def aforo (self) -> int:
        return self._aforo
    
    @property
    def precio_base (self) -> float :
        return self._precio_base

    @aforo.setter
    def aforo (self , valor : int ):
        if valor < 0 :
            raise ValueError ("Error , el valor no puede ser 0 ")
        self._aforo = valor

    @precio_base.setter
    def precio_base (self , v : int ):
        if v < 0:
            raise ValueError ("Error , el precio no puede ser negativo")
        self._precio_base = v





 



        







    





