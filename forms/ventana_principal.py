import util.globals as globales
from customtkinter import *
import util.generic as utl
from PIL import Image
import io

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
        self.MenuSuperior()
        self.MenuLateral()
        self.Principal()

    def close(self):
        globales.setUser(None)
        self.principal.deiconify()
        self.ventana.destroy()

    def MenuSuperior(self):
        # Frame
        f_superior = CTkFrame(self.ventana, height=70, bg_color="#E2E7EE", fg_color="#E2E7EE")
        f_superior.pack(side=TOP, fill="both")
        f_superior.pack_propagate(0)
        #Logo
        logo = CTkImage(Image.open("./util/img/Logo.png"), size=(178,45))
        label_logo = CTkLabel(f_superior, width=178, height=45, text="", corner_radius=10, bg_color="#E2E7EE", image=logo)
        label_logo.pack(side=LEFT, padx=24)
        #Boton desplegar menu lateral
        iconoMenu = CTkImage(Image.open("./util/img/menu.png"))
        btnMenu = CTkButton(f_superior, width=25, image=iconoMenu, text="", bg_color="#E2E7EE", fg_color="#E2E7EE", command=self.Ocultar_Menu)
        btnMenu.pack(side=LEFT)
        #Titulo
        titulo = CTkLabel(f_superior, width=230, text="Gestor de Pedidos", fg_color="#E2E7EE", font=self.TitulobarraSuperior, text_color="black")
        titulo.pack(side=LEFT, padx=(38,0))
        #Barra de busqueda
        iconoLupa = CTkImage(Image.open("./util/img/lupa.png"))
        self.btnBusqueda = CTkButton(f_superior, width=22, image=iconoLupa, text="", bg_color="#E2E7EE", fg_color="#E2E7EE", command=self.buscarPedido)
        self.btnBusqueda.pack(side=LEFT, padx=(38,0))
        self.busqueda = CTkEntry(f_superior, width=280, height=36, bg_color="#E2E7EE", fg_color="white", corner_radius=8, placeholder_text="Buscar Pedido", placeholder_text_color="#98A2B2", border_width=0, font=self.entry, text_color="black") 
        self.busqueda.pack(side=LEFT, padx=(10,0))
        #Boton Pizarra
        btnPizarra = CTkButton(f_superior, width=34, text="Pizarra", text_color="black", font=self.texto, bg_color="#E2E7EE", fg_color="#E2E7EE", command=self.Principal)
        btnPizarra.pack(side=LEFT, padx=(55,0))
        #Boton Cerrar Sesion
        btnCerrar = CTkButton(f_superior, width=34, text="Cerrar sesión", text_color="black", font=self.texto, bg_color="#E2E7EE", fg_color="#E2E7EE", command=self.CerrarSesion)
        btnCerrar.pack(side=LEFT, padx=(15,0))

    def Ocultar_Menu(self):
        if self.lateral.winfo_ismapped():
            self.lateral.pack_forget()
        else:
            self.lateral.pack(side=LEFT, fill="both", expand=False)

    def buscarPedido(self):
        pass

    def Principal(self):
        if(self.panel):
            self.Limpiar_Principal()
            self.panel.configure(fg_color="#99B4DF", bg_color="#99B4DF")
            self.busqueda.configure(state="normal")
            self.btnBusqueda.configure(hover=True, state="normal")
        else:
            self.panel = CTkFrame(self.ventana, bg_color="#99B4DF", fg_color="#99B4DF")
            self.panel.pack(side=RIGHT, fill="both", expand=True)

    def Limpiar_Principal(self):
        for item in self.panel.winfo_children():
            item.destroy()  

    def CerrarSesion(self):
        globales.setUser(None)
        self.principal.deiconify()
        self.ventana.destroy()

    def MenuLateral(self):
        #Frame
        self.lateral = CTkFrame(self.ventana, width=253, bg_color="#0D1C55", fg_color="#0D1C55")
        # self.lateral.pack_propagate(0)
        self.lateral.pack(side=LEFT, fill="both", expand=False)
        #Perfil
        f_encabezado = CTkFrame(self.lateral, height=69, fg_color="#0D1C55")
        f_encabezado.pack_propagate(0)
        f_encabezado.pack(side=TOP, fill="both", ipadx=5)
        if(self.usuario[4]):
            imgPerfil = CTkImage(Image.open(io.BytesIO(self.usuario[4])),size=(58,58))
        else:
            imgPerfil = CTkImage(Image.open("./util/img/usuario.png"),size=(58,58))
        self.perfil = CTkLabel(f_encabezado, width=43, image=imgPerfil, text="", bg_color="#0D1C55", fg_color="#0D1C55")
        self.perfil.pack(side=LEFT, pady=(18,0), anchor="n")
        f_nombre = CTkFrame(f_encabezado , fg_color="#0D1C55", height=69)
        f_nombre.pack_propagate(0)
        f_nombre.pack(side=LEFT, anchor="n", padx=(4,0), pady=(21,0))
        nombre = CTkLabel(f_nombre, height=9, text=self.usuario[1], text_color="white", font=self.texto ,bg_color="#0D1C55", fg_color="#0D1C55")
        nombre.pack(side=TOP, anchor="w")
        rol = CTkLabel(f_nombre, height=9, text=self.usuario[5], text_color="#B8BFCC", font=self.texto, bg_color="#0D1C55", fg_color="#0D1C55")
        rol.pack(side=TOP, anchor="w", pady=(11,0))
        #Menu
        linea = CTkFrame(self.lateral, height=2, fg_color="white")
        linea.pack(side=TOP, pady=(32,0), fill="x")
        tituloMenu = CTkLabel(self.lateral, height=18, fg_color="#0D1C55", bg_color="#0D1C55", text="MENU", text_color="#98A2B2", font=self.texto)
        tituloMenu.pack(side=TOP, pady=(13,0))
        #Opciones
        # Perfil
        iconoUsuario = CTkImage(Image.open("./util/img/user.png"))
        op_perfil = CTkButton(self.lateral, height=21, fg_color="#0D1C55", image=iconoUsuario, text="Perfil", text_color="white", font=self.texto, anchor="w", command=self.Perfil)
        op_perfil.pack(side=TOP, pady=(20,0), fill="x")
        if(self.usuario[5] in ["Administrador","Vendedor","Asistente"]):
            # Agregar pedido
            iconoAgregar = CTkImage(Image.open("./util/img/add.png"))
            agregarPedido = CTkButton(self.lateral, height=21, fg_color="#0D1C55", image=iconoAgregar, text="Agregar Pedido", text_color="white", font=self.texto, anchor="w", command=self.Agregar_pedido)
            agregarPedido.pack(side=TOP, pady=(25,0), fill="x")
        if(self.usuario[5]=="Administrador"):
            # Administracion de usuarios
            iconoUsuarios = CTkImage(Image.open("./util/img/usuarios.png"))
            adminUsuarios = CTkButton(self.lateral, height=21, fg_color="#0D1C55", image=iconoUsuarios, text="Administrar Usuarios", text_color="white", font=self.texto, anchor="w", command=lambda:self.Admin_Usuarios())
            adminUsuarios.pack(side=TOP, pady=(25,0), fill='x')
            # Reportes
            iconoReportes = CTkImage(Image.open("./util/img/reportes.png"))
            reportes = CTkButton(self.lateral, height=21, fg_color="#0D1C55", image=iconoReportes, text="Reportes", text_color="white", font=self.texto, anchor="w", command=lambda:self.Reportes())
            reportes.pack(side=TOP, pady=(25,0), fill='x')
        # Cerrar Sesion
        iconoSesion = CTkImage(Image.open("./util/img/cerrarSesion.png"))
        cerrar = CTkButton(self.lateral, height=21, fg_color="#0D1C55", image=iconoSesion, text="Cerrar Sesión", text_color="white", font=self.texto, anchor="w", command=self.CerrarSesion)
        cerrar.pack(side=TOP, pady=(25,0), fill='x')
        #Linea
        linea = CTkFrame(self.lateral, height=2, fg_color="white")
        linea.pack(side=TOP, pady=(32,0), fill="x")
        # Filtros

    def Perfil(self):
        pass

    def Agregar_pedido(self):
        pass

    def Reportes(self):
        pass
