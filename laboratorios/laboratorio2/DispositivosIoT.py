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


# función recursiva corregida
def monitorear_ciclos(dispositivo, ciclos):
    if ciclos <= 0:
        print("Monitoreo finalizado.")
    else:
        # Verifica si el dispositivo tiene el método leer_dato
        if hasattr(dispositivo, "leer_dato"):
            print(f"Ciclo {ciclos}: {dispositivo.leer_dato()}")
        else:
            print(f"Ciclo {ciclos}: {dispositivo.nombre} no puede ser monitoreado.")
        monitorear_ciclos(dispositivo, ciclos - 1)


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

    print("\n--- Gestión con funciones estándar ---")
    print(f"Cantidad de dispositivos: {len(dispositivos)}")

    # Leer datos de sensores (simulación)
    datos_temperatura = [d.leer_dato() for d in dispositivos if isinstance(d, SensorTemperatura)]
    if datos_temperatura:
        print(f"Temperatura máxima: {max(datos_temperatura):.2f} °C")
        print(f"Temperatura mínima: {min(datos_temperatura):.2f} °C")
        print(f"Temperatura promedio: {sum(datos_temperatura)/len(datos_temperatura):.2f} °C")

    # Ordenar dispositivos por nombre
    dispositivos_ordenados = sorted(dispositivos, key=lambda d: d.nombre)
    print("\nDispositivos ordenados por nombre:")
    for d in dispositivos_ordenados:
        print(f"- {d.nombre} ({d.ubicacion})")

    # Filtrar dispositivos que están apagados usando lambda y filter
    apagados = list(filter(lambda d: d.obtener_estado() == "Apagado", dispositivos))
    print("\nDispositivos apagados:")
    for d in apagados:
        print(f"- {d.nombre} ({d.ubicacion})")

    # Ejemplo de monitoreo recursivo
    print("\n--- Monitoreo recursivo de Sensor de Temperatura ---")
    monitorear_ciclos(temp, 3)
