class Nodo:
    def __init__(self, marca=None, modelo=None, sig=None):
        self.marca = marca
        self.modelo = modelo
        self.sig = sig

    def __str__(self):
        return "%s %s %s" %(self.marca, self.modelo)

class  lista:

    def __init__(self):
        self.inicio = None
        self.fin = None

    def agregar(self, carro):
        if self.inicio == None
            self.inicio = carro

        if self.fin != None
            self.fin.sig = carro

        self.fin = carro

    def listar(self):
        aux = self.inicio
        while aux != None:
            print(aux)
            aux = aux.sig

    def eliminar(self, modelo):
        if self.inicio.modelo == modelo
            self.inicio = self.inicio.sig
            return True
        else:
            aux = self.inicio
            anterior = aux
            while aux != None
                if aux.modelo == modelo
                    anterior.sig = nodo.sig
                    return True
                anterior = aux
                aux = aux.sig
        return False

if __name__ == "__main__":
    l = lista()

    while (true):
        print(".......Menu........\n"+
        "1. Agregar\n"+
        "2. Listar\n"+
        "3. Eliminar\n")
        sel = input("Seleccionar Opcion")
        if sel == "1":
            marca = input("Ingresar marca")
            modelo = input("Ingresar modelo")
            node = Nodo(marca,modelo)
            l.agregar(node)
        elif sel == "2"
            l.listar()
        elif sel == "3"
            modelo = input("Ingrese modelo a borrar")
            if(l.eliminar(modelo)):
                print("Modelo borrado")
            else:
                print("No se encontro modelo")
