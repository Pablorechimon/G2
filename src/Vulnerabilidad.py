class Vulnerabilidad :
    def __init__(self, id, nombre, id_primario_activo, id_cuenta, region, id_vulnerabilidad, nombre_vulnerabilidad,
                 dias, limite, resultado, solucion, categoria, recurso_asignado, punto_de_contacto) :
        self.nombre = nombre
        self.id = id
        self.id_primario_activo = id_primario_activo
        self.id_cuenta = id_cuenta
        self.region = region
        self.id_vulnerabilidad = id_vulnerabilidad
        self.nombre_vulnerabilidad = nombre_vulnerabilidad
        self.dias = dias
        self.limite = limite
        self.resultado = resultado
        self.solucion = solucion
        self.categoria = categoria
        self.recurso_asignado = recurso_asignado
        self.punto_de_contacto = punto_de_contacto