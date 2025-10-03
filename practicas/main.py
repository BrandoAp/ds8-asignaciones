"""
Sistema de Simulación de Dispositivos IoT
Programación Orientada a Objetos en Python

Este sistema demuestra conceptos de POO como:
- Herencia
- Encapsulación (atributos privados)
- Polimorfismo
- Abstracción
"""
import random
import time
from datetime import datetime


# ==================== CLASE BASE ====================
class DispositivoIoT:

    def __init__(self, id_dispositivo, nombre, ubicacion):
        """
        Constructor de la clase base
        __init__ es el metodo constructor que se ejecuta al crear un objeto
        self hace referencia al objeto actual (la instancia)
        """
        self.id_dispositivo = id_dispositivo  # Atributo público
        self.nombre = nombre  # Atributo público
        self.ubicacion = ubicacion  # Atributo público

        # Atributos privados (inician con _)
        # Estos no deberían ser accedidos directamente desde fuera de la clase
        self._estado = "Inactivo"  # Estado del dispositivo
        self._datos_historicos = []  # Lista de lecturas históricas
        self._tiempo_creacion = datetime.now()  # Tiempo de creación

    # Metodo privado (inicia con _)
    def _validar_lectura(self, valor):
        """
        Metodo privado para validar las lecturas
        Este metodo no debería ser llamado directamente desde fuera de la clase
        """
        return valor is not None and isinstance(valor, (int, float))

    # Metodo público para obtener el estado
    def obtener_estado(self):
        """Getter para obtener el estado del dispositivo"""
        return self._estado

    # Metodo público para cambiar el estado
    def cambiar_estado(self, nuevo_estado):
        """Setter para cambiar el estado del dispositivo"""
        self._estado = nuevo_estado
        return self._estado

    # Metodo que será sobrescrito en las subclases (POLIMORFISMO)
    def leer_datos(self):
        """
        Metodo base para leer datos del dispositivo.
        Este metodo será implementado de forma diferente en cada subclase.
        """
        raise NotImplementedError("Este método debe ser implementado en la subclase")

    # Metodo común para todos los dispositivos
    def obtener_informacion(self):
        """Retorna información básica del dispositivo"""
        return {
            'id': self.id_dispositivo,
            'nombre': self.nombre,
            'ubicacion': self.ubicacion,
            'estado': self._estado,
            'tiempo_creacion': self._tiempo_creacion.strftime("%Y-%m-%d %H:%M:%S"),
            'lecturas_historicas': len(self._datos_historicos)
        }


# ==================== SUBCLASES (HERENCIA) ====================

class SensorTemperatura(DispositivoIoT):
    """
    Subclase que hereda de DispositivoIoT
    Representa un sensor de temperatura
    """

    def __init__(self, id_dispositivo, nombre, ubicacion, rango_min=-40, rango_max=80):
        """
        Constructor que llama al constructor de la clase padre
        super() nos permite acceder a los métodos de la clase padre
        """
        super().__init__(id_dispositivo, nombre, ubicacion)  # Llama al __init__ del padre
        self.rango_min = rango_min
        self.rango_max = rango_max
        self.tipo = "Sensor de Temperatura"

    # Implementación específica del metodo polimórfico
    def leer_datos(self):
        """
        POLIMORFISMO: Este metodo se comporta diferente en cada subclase
        Simula la lectura de temperatura
        """
        temperatura = round(random.uniform(self.rango_min, self.rango_max), 1)

        # Validación usando metodo privado del padre
        if self._validar_lectura(temperatura):
            self._datos_historicos.append({
                'valor': temperatura,
                'unidad': '°C',
                'timestamp': datetime.now().strftime("%H:%M:%S")
            })
            return temperatura
        return None


class SensorMovimiento(DispositivoIoT):
    """Subclase para sensor de movimiento"""

    def __init__(self, id_dispositivo, nombre, ubicacion, sensibilidad="media"):
        super().__init__(id_dispositivo, nombre, ubicacion)
        self.sensibilidad = sensibilidad
        self.tipo = "Sensor de Movimiento"

    def leer_datos(self):
        """
        POLIMORFISMO: Comportamiento diferente para sensor de movimiento
        Simula la detección de movimiento
        """
        # Probabilidad de detección basada en sensibilidad
        probabilidades = {"baja": 0.2, "media": 0.4, "alta": 0.7}
        prob = probabilidades.get(self.sensibilidad, 0.4)

        movimiento_detectado = random.random() < prob

        if self._validar_lectura(movimiento_detectado):
            self._datos_historicos.append({
                'valor': "Movimiento detectado" if movimiento_detectado else "Sin movimiento",
                'timestamp': datetime.now().strftime("%H:%M:%S")
            })
            return movimiento_detectado
        return None


class CamaraSeguridad(DispositivoIoT):
    """Subclase para cámara de seguridad"""

    def __init__(self, id_dispositivo, nombre, ubicacion, resolucion="1080p"):
        super().__init__(id_dispositivo, nombre, ubicacion)
        self.resolucion = resolucion
        self.tipo = "Cámara de Seguridad"
        self._grabando = False

    def leer_datos(self):
        """
        POLIMORFISMO: Comportamiento diferente para cámara
        Simula la captura de imágenes
        """
        calidad_imagen = random.randint(60, 100)  # Porcentaje de calidad

        if self._validar_lectura(calidad_imagen):
            self._datos_historicos.append({
                'valor': f"Imagen capturada - Calidad: {calidad_imagen}%",
                'resolucion': self.resolucion,
                'timestamp': datetime.now().strftime("%H:%M:%S")
            })
            return calidad_imagen
        return None

    def iniciar_grabacion(self):
        """Metodo específico de la cámara"""
        self._grabando = True
        return self._grabando

    def detener_grabacion(self):
        """Metodo específico de la cámara"""
        self._grabando = False
        return self._grabando


# ==================== FUNCIONES AUXILIARES ====================

def funcion_recursiva_monitoreo(ciclos, mostrar_progreso=False):
    """
    FUNCIÓN RECURSIVA: Se llama a sí misma hasta llegar a 0
    Simula ciclos de monitoreo que van disminuyendo
    Retorna el número de ciclos procesados
    """
    if mostrar_progreso:
        print(f"Monitoreando... Ciclos restantes: {ciclos}")

    # Caso base: cuando llega a 0, termina la recursión
    if ciclos <= 0:
        if mostrar_progreso:
            print("Monitoreo completado!")
        return 0

    # Simula tiempo de procesamiento
    time.sleep(0.1)  # Reducido para que sea más rápido

    # Llamada recursiva con un ciclo menos
    return 1 + funcion_recursiva_monitoreo(ciclos - 1, mostrar_progreso)


def procesar_dispositivos(lista_dispositivos, funcion_procesamiento):
    """
    FUNCIÓN QUE RECIBE OTRA FUNCIÓN COMO PARÁMETRO
    Aplica una función de procesamiento a cada dispositivo
    """
    resultados = []

    for dispositivo in lista_dispositivos:
        resultado = funcion_procesamiento(dispositivo)
        resultados.append(resultado)

    return resultados


# Funciones para usar como parámetro
def leer_y_mostrar_datos(dispositivo):
    """Función que lee datos de un dispositivo y los muestra"""
    dato = dispositivo.leer_datos()
    print(f"{dispositivo.nombre}: {dato}")
    return dato


def activar_dispositivo(dispositivo):
    """Función que activa un dispositivo"""
    dispositivo.cambiar_estado("Activo")
    return dispositivo.obtener_estado()


# ==================== FUNCIÓN PRINCIPAL ====================
def main():
    """Función principal que demuestra todos los conceptos"""

    print("=" * 60)
    print("SISTEMA DE SIMULACIÓN DE DISPOSITIVOS IoT")
    print("=" * 60)

    # 1. CREAR DISPOSITIVOS (Demostrar herencia)
    print("\nCREANDO DISPOSITIVOS...")

    dispositivos = [
        SensorTemperatura("TEMP001", "Sensor Cocina", "Cocina", -10, 50),
        SensorTemperatura("TEMP002", "Sensor Jardín", "Jardín Exterior", -20, 45),
        SensorMovimiento("MOV001", "Detector Entrada", "Puerta Principal", "alta"),
        SensorMovimiento("MOV002", "Detector Patio", "Patio Trasero", "media"),
        CamaraSeguridad("CAM001", "Cámara Principal", "Salón", "4K"),
        CamaraSeguridad("CAM002", "Cámara Externa", "Entrada", "1080p")
    ]

    # 2. DEMOSTRAR POLIMORFISMO
    print(f"\nDEMOSTRANDO POLIMORFISMO...")
    print("El mismo método 'leer_datos()' se comporta diferente en cada clase:")

    for dispositivo in dispositivos:
        dispositivo.cambiar_estado("Activo")
        dato = dispositivo.leer_datos()  # Polimorfismo en acción
        print(f"   • {dispositivo.tipo} - {dispositivo.nombre}: {dato}")

    # 3. FUNCIÓN RECURSIVA
    print(f"\nEJECUTANDO MONITOREO RECURSIVO...")
    funcion_recursiva_monitoreo(5)  # Iniciamos con 5 ciclos

    # 4. FUNCIÓN QUE RECIBE OTRA FUNCIÓN COMO PARÁMETRO
    print(f"\nUSANDO FUNCIÓN DE ORDEN SUPERIOR...")
    # Activamos todos los dispositivos usando una función como parámetro
    estados = procesar_dispositivos(dispositivos, activar_dispositivo)

    # Leemos datos de todos usando otra función como parámetro
    datos = procesar_dispositivos(dispositivos, leer_y_mostrar_datos)

    # 5. USO DE FUNCIONES BUILT-IN: len(), max(), min(), sum(), sorted()
    print(f"\nUSANDO FUNCIONES BUILT-IN DE PYTHON...")

    # Extraer solo valores numéricos para las operaciones matemáticas
    valores_numericos = [dato for dato in datos if isinstance(dato, (int, float))]

    print(f"Estadísticas de los datos:")
    print(f"   • Total de dispositivos: {len(dispositivos)}")
    print(f"   • Total de lecturas numéricas: {len(valores_numericos)}")

    if valores_numericos:  # Solo si hay valores numéricos
        print(f"   • Valor máximo: {max(valores_numericos)}")
        print(f"   • Valor mínimo: {min(valores_numericos)}")
        print(f"   • Suma total: {sum(valores_numericos)}")
        print(f"   • Valores ordenados: {sorted(valores_numericos)}")

    # Ordenar dispositivos por nombre
    dispositivos_ordenados = sorted(dispositivos, key=lambda d: d.nombre)
    print(f"   • Dispositivos ordenados por nombre:")
    for disp in dispositivos_ordenados:
        print(f"     - {disp.nombre}")

    # 6. USO DE FUNCIÓN LAMBDA
    print(f"\nUSANDO FUNCIÓN LAMBDA...")

    # Filtrar solo sensores de temperatura usando lambda
    sensores_temp = list(filter(lambda d: isinstance(d, SensorTemperatura), dispositivos))
    print(f"Sensores de temperatura encontrados: {len(sensores_temp)}")
    for sensor in sensores_temp:
        print(f"      • {sensor.nombre} en {sensor.ubicacion}")

    # Transformar nombres a mayúsculas usando lambda
    nombres_mayus = list(map(lambda d: d.nombre.upper(), dispositivos))
    print(f"Nombres en mayúsculas:")
    for nombre in nombres_mayus:
        print(f"      • {nombre}")

    # Crear lista de dispositivos activos usando lambda
    dispositivos_activos = list(filter(lambda d: d.obtener_estado() == "Activo", dispositivos))
    print(f"Dispositivos activos: {len(dispositivos_activos)}")

    # 7. MOSTRAR INFORMACIÓN FINAL
    print(f"\nRESUMEN FINAL DEL SISTEMA...")
    print("=" * 40)

    for dispositivo in dispositivos:
        info = dispositivo.obtener_informacion()
        print(f"{info['nombre']} ({info['id']})")
        print(f"Estado: {info['estado']}")
        print(f"Ubicación: {info['ubicacion']}")
        print(f"Lecturas históricas: {info['lecturas_historicas']}")
        print()

    print("¡Sistema de dispositivos IoT ejecutado exitosamente!")
    print("=" * 60)


# ==================== EJECUCIÓN ====================
if __name__ == "__main__":
    main()