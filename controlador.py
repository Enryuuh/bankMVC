from modelo import CuentaBancaria

class ControladorBanco:
    def __init__(self, vista):
        self.cuenta = CuentaBancaria()
        self.vista = vista

    def depositar(self, cantidad):
        mensaje = self.cuenta.depositar(cantidad)
        self.vista.actualizar_mensaje(mensaje)

    def retirar(self, cantidad):
        mensaje = self.cuenta.retirar(cantidad)
        self.vista.actualizar_mensaje(mensaje)

    def consultar_saldo(self):
        mensaje = self.cuenta.consultar_saldo()
        self.vista.actualizar_mensaje(mensaje)
