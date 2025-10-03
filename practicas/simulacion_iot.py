"""
Sistema de Simulación de Dispositivos IoT - Versión Optimizada
"""

import random
import time
from datetime import datetime

"""
__slots__ es una optimización de memoria en Python
que reemplaza el diccionario dinámico (__dict__)
por una estructura estática más eficiente.

"""


# ==================== CLASE BASE OPTIMIZADA ====================
class DispositivoIoT:
    __slots__ = (
        "id_dispositivo",
        "nombre",
        "ubicacion",
        "_estado",
        "_datos_historicos",
        "_tiempo_creacion",
    )

    def __init__(self, id_dispositivo, nombre, ubicacion):
        # OPTIMIZACIÓN: __slots__ para reducir uso de memoria
        self.id_dispositivo = id_dispositivo
        self.nombre = nombre
        self.ubicacion = ubicacion
        self._estado = "Inactivo"
        self._datos_historicos = []
        self._tiempo_creacion = datetime.now()

    def _validar_lectura(self, valor):
        # OPTIMIZACIÓN: isinstance más rápido que type checking
        return isinstance(valor, (int, float, bool))

    def obtener_estado(self):
        return self._estado

    def cambiar_estado(self, nuevo_estado):
        self._estado = nuevo_estado
        return self._estado

    def leer_datos(self):
        raise NotImplementedError

    def obtener_informacion(self):
        # OPTIMIZACIÓN: Diccionario pre-construido más rápido
        return {
            "id": self.id_dispositivo,
            "nombre": self.nombre,
            "ubicacion": self.ubicacion,
            "estado": self._estado,
            "tiempo_creacion": self._tiempo_creacion.strftime("%Y-%m-%d %H:%M:%S"),
            "lecturas_historicas": len(self._datos_historicos),
        }


class SensorTemperatura(DispositivoIoT):
    __slots__ = ("rango_min", "rango_max", "tipo")

    def __init__(self, id_dispositivo, nombre, ubicacion, rango_min=-40, rango_max=80):
        # Llamada directa a __init__ en lugar de super()
        DispositivoIoT.__init__(self, id_dispositivo, nombre, ubicacion)
        self.rango_min = rango_min
        self.rango_max = rango_max
        self.tipo = "Sensor de Temperatura"

    def leer_datos(self):
        # random.uniform más rápido que randrange para floats
        temperatura = round(random.uniform(self.rango_min, self.rango_max), 1)

        if self._validar_lectura(temperatura):
            # Tupla en lugar de diccionario para menos overhead
            self._datos_historicos.append(
                (temperatura, "°C", datetime.now().strftime("%H:%M:%S"))
            )
            return temperatura
        return None


class SensorMovimiento(DispositivoIoT):
    __slots__ = ("sensibilidad", "tipo", "_probabilidades")

    def __init__(self, id_dispositivo, nombre, ubicacion, sensibilidad="media"):
        DispositivoIoT.__init__(self, id_dispositivo, nombre, ubicacion)
        self.sensibilidad = sensibilidad
        self.tipo = "Sensor de Movimiento"
        # Pre-calcular probabilidades
        self._probabilidades = {"baja": 0.2, "media": 0.4, "alta": 0.7}

    def leer_datos(self):
        # Acceso directo al diccionario
        prob = self._probabilidades.get(self.sensibilidad, 0.4)
        movimiento_detectado = random.random() < prob

        if self._validar_lectura(movimiento_detectado):
            self._datos_historicos.append(
                (movimiento_detectado, datetime.now().strftime("%H:%M:%S"))
            )
            return movimiento_detectado
        return None


class CamaraSeguridad(DispositivoIoT):
    __slots__ = ("resolucion", "tipo", "_grabando")

    def __init__(self, id_dispositivo, nombre, ubicacion, resolucion="1080p"):
        DispositivoIoT.__init__(self, id_dispositivo, nombre, ubicacion)
        self.resolucion = resolucion
        self.tipo = "Cámara de Seguridad"
        self._grabando = False

    def leer_datos(self):
        # randint más rápido para enteros
        calidad_imagen = random.randint(60, 100)

        if self._validar_lectura(calidad_imagen):
            self._datos_historicos.append(
                (calidad_imagen, self.resolucion, datetime.now().strftime("%H:%M:%S"))
            )
            return calidad_imagen
        return None

    def iniciar_grabacion(self):
        self._grabando = True
        return self._grabando

    def detener_grabacion(self):
        self._grabando = False
        return self._grabando


# ==================== FUNCIONES AUXILIARES OPTIMIZADAS ====================
def funcion_recursiva_monitoreo(ciclos, mostrar_progreso=False):
    """
    OPTIMIZACIÓN: Recursión convertida a iteración para evitar stack overflow
    """
    ciclos_procesados = 0

    while ciclos > 0:
        if mostrar_progreso:
            print(f"Monitoreando... Ciclos restantes: {ciclos}")

        time.sleep(0.05)  # Reducido tiempo de sleep
        ciclos_procesados += 1
        ciclos -= 1

    if mostrar_progreso:
        print("Monitoreo completado!")

    return ciclos_procesados


def procesar_dispositivos(lista_dispositivos, funcion_procesamiento):
    """
    OPTIMIZACIÓN: List comprehension más rápido que loop tradicional
    """
    return [funcion_procesamiento(dispositivo) for dispositivo in lista_dispositivos]


# Funciones optimizadas para usar como parámetro
def leer_y_mostrar_datos(dispositivo):
    dato = dispositivo.leer_datos()
    print(f"{dispositivo.nombre}: {dato}")
    return dato


def activar_dispositivo(dispositivo):
    dispositivo.cambiar_estado("Activo")
    return dispositivo.obtener_estado()


# ==================== FUNCIÓN PRINCIPAL OPTIMIZADA ====================
def main():
    print("=" * 50)
    print("SISTEMA IoT OPTIMIZADO")
    print("=" * 50)

    # Lista pre-construida más eficiente
    dispositivos = [
        SensorTemperatura("TEMP001", "Sensor Cocina", "Cocina", -10, 50),
        SensorTemperatura("TEMP002", "Sensor Jardín", "Jardín Exterior", -20, 45),
        SensorMovimiento("MOV001", "Detector Entrada", "Puerta Principal", "alta"),
        SensorMovimiento("MOV002", "Detector Patio", "Patio Trasero", "media"),
        CamaraSeguridad("CAM001", "Cámara Principal", "Salón", "4K"),
        CamaraSeguridad("CAM002", "Cámara Externa", "Entrada", "1080p"),
    ]

    # Operaciones por lotes
    print("\nDEMOSTRANDO POLIMORFISMO...")
    for dispositivo in dispositivos:
        dispositivo.cambiar_estado("Activo")
        dato = dispositivo.leer_datos()
        print(f"• {dispositivo.tipo}: {dato}")

    print("\nEJECUTANDO MONITOREO...")
    funcion_recursiva_monitoreo(3)  # Menos ciclos para demo

    print("\nACTIVANDO DISPOSITIVOS...")
    estados = procesar_dispositivos(dispositivos, activar_dispositivo)
    datos = procesar_dispositivos(dispositivos, leer_y_mostrar_datos)

    # Filtrado más eficiente
    valores_numericos = [dato for dato in datos if isinstance(dato, (int, float))]

    print(f"\nESTADÍSTICAS:")
    print(f"• Dispositivos: {len(dispositivos)}")
    print(f"• Lecturas numéricas: {len(valores_numericos)}")

    if valores_numericos:
        print(f"• Máximo: {max(valores_numericos)}")
        print(f"• Mínimo: {min(valores_numericos)}")
        print(f"• Suma: {sum(valores_numericos)}")

    # Operaciones de filtrado más eficientes
    sensores_temp = [d for d in dispositivos if isinstance(d, SensorTemperatura)]
    print(f"\nSensores temperatura: {len(sensores_temp)}")

    dispositivos_activos = [d for d in dispositivos if d.obtener_estado() == "Activo"]
    print(f"Dispositivos activos: {len(dispositivos_activos)}")

    print("\nRESUMEN FINAL:")
    for dispositivo in dispositivos:
        info = dispositivo.obtener_informacion()
        print(
            f"{info['nombre']} - Estado: {info['estado']} - Lecturas: {info['lecturas_historicas']}"
        )

    print("\n¡Sistema optimizado ejecutado exitosamente!")


if __name__ == "__main__":
    # Llamada directa más rápida
    main()
