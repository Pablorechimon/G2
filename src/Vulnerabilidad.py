class Vulnerabilidad :
    categoria
    recurso_asignado
    punto_de_contacto
        
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
        
    def set_categoria(self, categoria):
        self.categoria = categoria
        
    def set_categoria(self, recurso):
        self.recurso = recurso
        
    def set_categoria(self, punto_de_contacto):
        self.punto_de_contacto = punto_de_contacto