from customtkinter import *
import util.globals as globales
import util.generic as utl
from PIL import Image
import re

class Login():
    def __init__(self):
        # Creacion de la ventana
        self.ventana = CTk()
        w = (int(self.ventana.winfo_screenwidth()))
        h = (int(self.ventana.winfo_screenheight()))
        self.w = int(w*0.67)
        self.h = int(h*0.67)
        # Apariencia
        apariencia = self.ventana._get_appearance_mode()
        globales.setSize(w,h,apariencia)
        self.ventana.title('Inicio de sesión')
        utl.c_ventana(self.ventana, self.w, self.h)
        self.ventana.resizable(0,0)
        if(apariencia=="dark"):
            self.fondo="#484b4f"
            self.img="./util/img/LoginImgDark.png"
            self.color_texto="white"
            self.entry="#6e6f73"
            self.holder_color="#C4C4C4"
        else:
            self.fondo="white"
            self.img="./util/img/LoginImg.png"
            self.color_texto="black"
            self.entry="white"
            self.holder_color="#8F7C7C"
        #Fuentes
        self.titulos = CTkFont(family="Inter", size=15, weight="bold")
        self.normal = CTkFont(family="Inter", size=15, weight="normal")
        self.login_form()
        self.ventana.mainloop()

    def login_form(self):
        # Imagen Fondo
        bg_image = CTkImage(Image.open(self.img), size=(self.w, self.h))
        bg_image_label = CTkLabel(self.ventana, image=bg_image, text="")
        bg_image_label.grid(row=0, column=0)
        # Formulario
        form = CTkFrame(self.ventana, width=self.w*0.5, height=self.h*0.5, fg_color=self.fondo, bg_color=self.fondo, corner_radius=0)
        form.pack_propagate(0)
        if(self.h<603):
            form.grid(row=0, column=0, pady=(self.h*0.21,0))
        else:
            form.grid(row=0, column=0, pady=(self.h*0.18,0))
        # Correo
        labelCorreo = CTkLabel(form, text="Correo Electronico: ",  text_color=self.color_texto, font=self.titulos, fg_color=self.fondo)
        labelCorreo.pack(side=TOP, anchor="w", padx=70, pady=(35,0))
        self.correo = CTkEntry(form, width=self.w*0.333, height=37, border_width=3, border_color="#BDBDE1", fg_color=self.entry, placeholder_text="ejemplo@email.com", placeholder_text_color=self.holder_color, font=self.normal, text_color=self.color_texto)
        self.correo.pack(side=TOP, anchor="w", padx=70, pady=(5,0))
        self.correo_validate = CTkLabel(form, text="")
        self.correo_validate.pack(side=TOP, anchor="w", padx=72)
        # Contraseña
        labelContra = CTkLabel(form, text="Contraseña: ", text_color=self.color_texto, font=self.titulos, fg_color=self.fondo)
        labelContra.pack(side=TOP, anchor="w", padx=70, pady=(5,0))
        self.contrasenna = CTkEntry(form, width=self.w*0.333, height=37, border_width=3, border_color="#BDBDE1", fg_color=self.entry, placeholder_text="Introduce tu contraseña", placeholder_text_color=self.holder_color, font=self.normal, text_color=self.color_texto)
        self.contrasenna.pack(side=TOP, anchor="w", padx=70, pady=(5,0))
        self.contrasenna.configure(show='*')
        self.contra_validate = CTkLabel(form, text="")
        self.contra_validate.pack(side=TOP, anchor="w", padx=72)
        # Boton formulario
        inicio = CTkButton(form, width=self.w*0.147, height=45, fg_color="#93A3DC", text_color="white", text="Iniciar Sesion", font=self.titulos, command=self.verificacion)
        inicio.pack(side=TOP, pady=(self.h*0.03, self.h*0.02))

    def verificacion(self):
        correo = self.correo.get()
        contra = self.contrasenna.get()
        correo_EX = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
        if(not correo):
            self.correo_validate.configure(text="Campo obligatorio", text_color="red")
        elif(not re.match(correo_EX,correo)):
            self.correo_validate.configure(text="Formato incorrecto", text_color="red")
            self.correo.delete(0 ,END)
        elif(not contra):
            self.correo_validate.configure(text="")
            self.contra_validate.configure(text="Campo obligatorio", text_color="red")
        elif(len(contra)<8):
            self.correo_validate.configure(text="")
            self.contra_validate.configure(text="Debe tener 8 o mas caracteres", text_color="red")
        else:
            self.correo_validate.configure(text="")
            self.contra_validate.configure(text="")