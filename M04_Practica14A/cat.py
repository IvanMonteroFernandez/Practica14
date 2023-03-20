class cat:
    def __init__(self, color, peso, altura, raza):
        self.color = color
        self.peso = peso
        self.altura = altura
        self.raza = raza


    def nom(self):
        print(
            "El color es " + self.color + "\n la peso es " + self.peso + "\n la altura es " + self.altura +
            "\n el raza es " + self.raza )
    """Per crear un arxiu .json per utilitzar amb el json-server, s’agafarà una class creada (amb constructor, 
    atributs i getters i setters i s’afegirà la següent funció: """
    def to_dict(self):
        return {
            "color":self.color,
            "peso":self.peso,
            "altura":self.altura,
            "raza":self.raza
        }
    """A partir de aquí definimos los getters y setters de los atributos de la clase. Esto sirve para poder ver el valor de la tributo(getters)
    y para cambiar la instancia de los atributos por una instancia nueva (setters)"""

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso

    def getAltura(self):
        return self.altura

    def setAltura(self, altura):
        self.altura = altura

    def getRaza(self):
        return self.raza

    def setRaza(self, raza):
        self.raza = raza


