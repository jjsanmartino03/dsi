from guia import Guia


class Contribuyente:
    def __init__(self, nombre, apellido, cuit):
        self.nombre = nombre
        self.apellido = apellido
        self.cuit = cuit


class Persistencia:
    guias = []

    def guardar_guia(self, guia):
        Persistencia.guias.append(guia)


class ValidadorAFIP:
    contribuyentes = [Contribuyente("Juan", "Perez", 20448733751), Contribuyente("Maria", "Gomez", 20448733762)]

    def buscar_cuit(self, cuit) -> Contribuyente | None:
        for contribuyente in ValidadorAFIP.contribuyentes:
            if contribuyente.cuit == cuit:
                return contribuyente

        return None


class Controller:
    def validar_datos(self, nombre, apellido, cuit):
        validador = ValidadorAFIP()
        contribuyente = validador.buscar_cuit(cuit)

        if contribuyente is None:
            print("El CUIT no existe, inténtelo otra vez")
            return

        if contribuyente.nombre != nombre or contribuyente.apellido != apellido:
            print("Los datos no coinciden, inténtelo otra vez")
            return

        print("Los datos son correctos")
        guia = Guia(nombre, apellido, cuit)

        return guia


class IU:
    @staticmethod
    def registrar_guia():
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        cuit = int(input("Ingrese su CUIT: "))

        controller = Controller()

        guia = controller.validar_datos(nombre, apellido, cuit)

        if guia == None:
            return

        contrasenia = input("Ingrese su contraseña: ")

        guia.contrasenia = contrasenia

        persistencia = Persistencia()
        persistencia.guardar_guia(guia)

        print("Su usuario fue creado con éxito")


IU.registrar_guia()
