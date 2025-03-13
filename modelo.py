class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Has depositado ${cantidad}. Saldo actual: ${self.saldo}"
        return "La cantidad a depositar debe ser mayor que 0."

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            return f"Has retirado ${cantidad}. Saldo actual: ${self.saldo}"
        elif cantidad > self.saldo:
            return "Fondos insuficientes."
        return "La cantidad a retirar debe ser mayor que 0."

    def consultar_saldo(self):
        return f"Saldo actual: ${self.saldo}"
