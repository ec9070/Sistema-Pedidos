def setSize(ancho, altura, tema):
    global w 
    global h
    global apariencia
    w = ancho
    h = altura
    apariencia = tema

def setUser(user):
    global usuario
    usuario = user

def getSize():
    size=(w,h,apariencia)
    return size

def getUser():
    return usuario

