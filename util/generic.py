def c_ventana(ventana,ancho,largo):
    largo = largo - 48
    p_ancho = ventana.winfo_screenwidth()
    p_largo = ventana.winfo_screenheight()
    x = int((p_ancho/2) - (ancho/2))
    y = int((p_largo/2) - (largo/2))
    return ventana.geometry(f"{ancho}x{largo}+{x}+{y}")