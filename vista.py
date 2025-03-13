import tkinter as tk
from tkinter import messagebox
from controlador import ControladorBanco

class AplicacionBanco:
    def __init__(self, root):
        self.root = root
        self.root.title("Cuenta Bancaria")
        self.root.geometry("300x250")
        
        self.controlador = ControladorBanco(self)
        
        self.label = tk.Label(root, text="Ingrese una cantidad:")
        self.label.pack(pady=5)
        
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        self.boton_depositar = tk.Button(root, text="Depositar", command=self.depositar)
        self.boton_depositar.pack(pady=5)
        
        self.boton_retirar = tk.Button(root, text="Retirar", command=self.retirar)
        self.boton_retirar.pack(pady=5)
        
        self.boton_saldo = tk.Button(root, text="Consultar Saldo", command=self.consultar_saldo)
        self.boton_saldo.pack(pady=5)
        
        self.boton_salir = tk.Button(root, text="Salir", command=root.quit)
        self.boton_salir.pack(pady=5)
        
        self.mensaje = tk.Label(root, text="", fg="blue")
        self.mensaje.pack(pady=5)
    
    def obtener_cantidad(self):
        try:
            return float(self.entry.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido")
            return None
    
    def depositar(self):
        cantidad = self.obtener_cantidad()
        if cantidad is not None:
            self.controlador.depositar(cantidad)
    
    def retirar(self):
        cantidad = self.obtener_cantidad()
        if cantidad is not None:
            self.controlador.retirar(cantidad)
    
    def consultar_saldo(self):
        self.controlador.consultar_saldo()

    def actualizar_mensaje(self, mensaje):
        self.mensaje.config(text=mensaje)
