class book:
    def __init__(self, titulo,portada,fecha,autor,editorial,paginas):
        self.titulo= titulo
        self.portada=portada
        self.fecha=fecha
        self.autor=autor
        self.editorial=editorial
        self.paginas=paginas

    def nom(self):
        print("El título es "+self.titulo +"\n la portada es " + self.potada + "\n la fecha es "+self.fecha+ "\n el autor es " + self.autor +
              "\n la editorial es " + self.editorial + "\n el numero de páginas es "+ self.paginas)


    """Per crear un arxiu .json per utilitzar amb el json-server, s’agafarà una class creada (amb constructor, 
    atributs i getters i setters i s’afegirà la següent funció: """
    def to_dict(self):
        return {
            "titulo":self.titulo,
            "portada":self.portada,
            "fecha":self.fecha,
            "autor":self.autor,
            "editorial":self.editorial,
            "paginas":self.paginas
        }
    """A partir de aquí definimos los getters y setters de los atributos de la clase. Esto sirve para poder ver el valor de la tributo(getters)
    y para cambiar la instancia de los atributos por una instancia nueva (setters)"""
    def getTitulo(self):
        return self.titulo
    def setTitulo(self,titulo):
        self.titulo=titulo
    def getPortada(self):
        return self.portada
    def setPortada(self,portada):
        self.portada=portada
    def getFecha(self):
        return self.fecha
    def setFecha(self,fecha):
        self.fecha=fecha
    def getAutor(self):
        return self.autor
    def setAutor(self,autor):
        self.autor=autor
    def getEditorial(self):
        return self.editorial
    def setEditorial(self,editorial):
        self.editorial=editorial
    def getPaginas(self):
        return self.paginas
    def setPaginas(self,paginas):
        self.paginas=paginas
