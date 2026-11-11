import hashlib

def c_ventana(ventana,ancho,largo):
    p_ancho = ventana.winfo_screenwidth()
    p_largo = ventana.winfo_screenheight()
    if largo < p_largo:
        largo = largo - 48
    x = int((p_ancho/2) - (ancho/2))
    y = int((p_largo/2) - (largo/2))
    return ventana.geometry(f"{ancho}x{largo}+{x}+{y}")

def hash(text:str):
    h = hashlib.new("SHA256")
    h.update(text.encode())
    return h.hexdigest()