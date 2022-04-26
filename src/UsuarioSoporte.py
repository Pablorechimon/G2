from g2.src import Persona


class UsuarioSoporte(Persona):

    def __init__(self, id, nombre, email, equipo, tipo, vulnerabilidades_a_remediar):
        Persona.__init__(id, nombre, email)
        self.equipo = equipo
        self.id_cliente = tipo
        self.vulnerabilidades_a_remediar= list(vulnerabilidades_a_remediar)

    def agregarVulnerabilidad(self, vulnerabilidad):
        self.vulnerabilidades_a_remediar.append(vulnerabilidad)