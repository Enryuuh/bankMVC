from modelo import CuentaBancaria
from vista import VistaCuenta

class ControladorCuenta:
    def __init__(self):
        self.cuenta = CuentaBancaria()
        self.vista = VistaCuenta()
    
    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()
            if opcion == "1":
                cantidad = self.vista.obtener_cantidad("Ingrese la cantidad a depositar: ")
                if cantidad is not None:
                    self.vista.mostrar_mensaje(self.cuenta.depositar(cantidad))
                else:
                    self.vista.mostrar_mensaje("Entrada no válida.")
            elif opcion == "2":
                cantidad = self.vista.obtener_cantidad("Ingrese la cantidad a retirar: ")
                if cantidad is not None:
                    self.vista.mostrar_mensaje(self.cuenta.retirar(cantidad))
                else:
                    self.vista.mostrar_mensaje("Entrada no válida.")
            elif opcion == "3":
                self.vista.mostrar_mensaje(self.cuenta.consultar_saldo())
            elif opcion == "4":
                self.vista.mostrar_mensaje("Gracias por usar el banco, chaitoo")
                break
            else:
                self.vista.mostrar_mensaje("Opción no válida. Intente de nuevo.")
