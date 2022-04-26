from g2.src import Persona


class UsuarioCliente(Persona):

    def __init__(self, id, nombre, email, id_cliente, vulnerabilidades_a_aprobar):
        Persona.__init__(id, nombre, email)
        self.id_cliente = id_cliente
        self.vulnerabilidades_a_aprobar = list(vulnerabilidades_a_aprobar)

    def agregarVulnerabilidad(self, vulnerabilidad):
        self.vulnerabilidades_a_aprobar.append(vulnerabilidad)
