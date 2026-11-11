import util.globals as globales
from customtkinter import *
import util.generic as utl

class VentanaPrincipal():
    def __init__(self, principal):
        #Inicio
        size = globales.getSize()
        self.usuario = globales.getUser()
        self.w=size[0]
        self.h=size[1]
        self.principal = principal
        self.panel = None
        #Creacion de ventana
        self.ventana = CTkToplevel()
        self.ventana.title("Ventana Principal")
        utl.c_ventana(self.ventana, self.w, self.h)
        self.ventana.protocol("WM_DELETE_WINDOW", self.close)
        #Fuentes
        self.TitulobarraSuperior = CTkFont(family="Inter", size=25, weight="bold")
        self.texto = CTkFont(family="Inter", size=14, weight="bold")
        self.entry = CTkFont(family="Inter", size=14, weight="normal")

    def close(self):
        globales.setUser(None)
        self.principal.deiconify()
        self.ventana.destroy()