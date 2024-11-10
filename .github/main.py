class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio= precio
        self.marca=marca
        self.registro=registro
        self.asientos= list(Asiento)
        self.motor=Motor
        
    def cantidadAsientos():
        casientos=0
        for i in self.asientos:
            if self.asientos[i]!=None:
                casientos+=1
        return casientos
    
    def verificarIntegridad():
        pass

class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio= precio
        self.registro=registro
    
    def cambiarColor(self,col):
        if col=="rojo" or col=="verde" or col=="amarillo" or col=="negro" or col=="blanco":
            self.color=col

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    
    def cambiarRegistro(self,nuevoregistro):
        registro=nuevoregistro
        
    def asignarTipo(self,nuevotipo):
        if nuevotipo=="electrico" or nuevotipo=="gasolina":
            tipo=nuevotipo