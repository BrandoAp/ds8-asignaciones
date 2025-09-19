# Clase para dispositivo genérico
class DispositivoIoT:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self._estado = False

    def encender(self):
        self._estado = True
        print(f"{self.nombre} en {self.ubicacion} está ENCENDIDO.")

    def apagar(self):
        self._estado = False
        print(f"{self.nombre} en {self.ubicacion} está APAGADO.")

    def obtener_estado(self):
        return "Encendido" if self._estado else "Apagado"


# Subclase Sensor de Temperatura
class SensorTemperatura(DispositivoIoT):
    def __init__(self, nombre, ubicacion, rango_medicion=(-10, 50)):
        super().__init__(nombre, ubicacion)
        self.rango_medicion = rango_medicion

    def leer_dato(self):
        import random
        temperatura = random.uniform(*self.rango_medicion)
        print(f"📡 {self.nombre} en {self.ubicacion}: {temperatura:.2f} °C")
        return temperatura


# Subclase Sensor de Movimiento
class SensorMovimiento(DispositivoIoT):
    def __init__(self, nombre, ubicacion):
        super().__init__(nombre, ubicacion)

    def leer_dato(self):
        import random
        movimiento = random.choice([True, False])
        estado = "Movimiento detectado 🚨" if movimiento else "Sin movimiento"
        print(f"📡 {self.nombre} en {self.ubicacion}: {estado}")
        return movimiento


# Subclase Cámara de Seguridad
class CamaraSeguridad(DispositivoIoT):
    def __init__(self, nombre, ubicacion, resolucion="1080p"):
        super().__init__(nombre, ubicacion)
        self.resolucion = resolucion

    def leer_dato(self):
        print(f"📷 {self.nombre} en {self.ubicacion} está grabando en {self.resolucion}.")
        return f"Grabando en {self.resolucion}"
#funcion recursiva
def moritorear_ciclos(dispositivo, ciclos):
    if ciclos <= 0:
        print ("moritoreo finalizado.")
    else:
        print(f"Ciclo {ciclos}: {dispositivo.moritorear()}")
        moritorear_ciclos(dispositivo,ciclos-1)

# ================================================================
# ✅ Función que recibe otra función como parámetro (lo que te asignaron a ti)
# ================================================================
def aplicar_funcion(dispositivos, funcion):
    """
    Recibe una lista de dispositivos y una función,
    aplica esa función a cada dispositivo y devuelve los resultados.
    """
    resultados = []
    for d in dispositivos:
        resultados.append(funcion(d))
    return resultados


# Ejemplo de uso
if __name__ == "__main__":
    # Crear dispositivos
    temp = SensorTemperatura("Sensor Temp", "Sala")
    mov = SensorMovimiento("Sensor Mov", "Garaje")
    cam = CamaraSeguridad("Camara 1", "Entrada")

    dispositivos = [temp, mov, cam]

    # Pasamos una función normal como parámetro
    def obtener_info(d):
        return f"{d.nombre} en {d.ubicacion} está {d.obtener_estado()}"

    print("\n--- Estados de los dispositivos ---")
    print(aplicar_funcion(dispositivos, obtener_info))

    # También podemos pasar una función lambda como parámetro
    print("\n--- Solo los nombres de los dispositivos ---")
    print(aplicar_funcion(dispositivos, lambda d: d.nombre))
