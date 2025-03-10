class VistaCuenta:
    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)
    
    @staticmethod
    def mostrar_menu():
        print("\n1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Consultar saldo")
        print("4. Salir")
        return input("Seleccione una opción: ")
    
    @staticmethod
    def obtener_cantidad(mensaje):
        try:
            return float(input(mensaje))
        except ValueError:
            return None
