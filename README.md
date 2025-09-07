# Sistema de Parqueo Inteligente — Explicación de `parcial_1.py`

Este repositorio contiene una simulación en Python de un sistema de gestión de parqueo para un centro comercial. A continuación se explica con detalle el archivo `parciales/parcial_1.py`, su diseño, componentes y cómo usarlo.

---

## Resumen

`parcial_1.py` implementa la clase `SistemaParqueo` que emula la operación de un estacionamiento: entradas, salidas, historial de eventos y cálculo de tarifas (simuladas). También proporciona una interfaz por consola (menú) para interactuar con la simulación y una opción de simulación automática.

---

## Estructura del archivo

- Importaciones
- Clase `SistemaParqueo`
  - Constantes y variables internas
  - Métodos de utilidad (porcentaje, estado, hora)
  - Métodos de operación (entrada_auto, salida_auto)
  - Métodos de visualización (mostrar_estado_actual, mostrar_autos_estacionados, mostrar_historial_auto, mostrar_ultimos_eventos)
  - Método auxiliar para generar placas aleatorias
- Función `main()` con un menú interactivo
- Bloque `if __name__ == "__main__": main()`

---

## Dependencias

El script usa solo la librería estándar de Python: `random`, `datetime` y `time`. No requiere instalación de paquetes externos.

---

## Detalle del comportamiento por secciones

### 1) Importaciones

Se importan módulos estándar:

- `random` — para generar placas y tarifas aleatorias y seleccionar autos al azar.
- `datetime` — para registrar la hora de entrada y salida en formato legible.
- `time` — usado únicamente en la simulación automática para introducir pausas.

### 2) Clase `SistemaParqueo`

Responsable de representar el estado del estacionamiento y todas sus operaciones.

Atributos principales:

- `CAPACIDAD_MAXIMA` (int): capacidad total del estacionamiento (valor por defecto: 50).
- `TARIFA_POR_HORA` (float): tarifa base por hora (no utilizada directamente para cálculo real en la versión actual, valor por defecto: 5.00).
- `espacios_ocupados` (int): número actual de espacios ocupados.
- `espacios_libres` (int): número actual de espacios libres.
- `placas_autos` (list): lista de placas actualmente estacionadas (permite duplicados).
- `historial_eventos` (list): lista cronológica de eventos con tuplas `(placa, tipo_evento, hora, tarifa)`.
- `historial_autos` (dict): historial indexado por placa; cada clave es una placa y su valor es la lista de eventos asociados.

Métodos descriptos:

- `calcular_porcentaje_ocupacion()` — Retorna el porcentaje de ocupación como número (0-100).

- `obtener_estado_parqueo()` — Devuelve una cadena que describe el estado según el porcentaje:

  - "LLENO" cuando >= 90%
  - "MEDIO OCUPADO" cuando >= 50% y < 90%
  - "DISPONIBLE" cuando < 50%

- `obtener_hora_actual()` — Retorna la hora actual formateada `YYYY-MM-DD HH:MM:SS`.

- `generar_placa_aleatoria()` — Genera una placa en formato `LLL-NNN` (3 letras, guion, 3 dígitos), por ejemplo `ABC-123`.

- `entrada_auto(placa, cantidad=1)` — Registra la entrada de uno o más autos:

  - Acepta `placa` como una cadena. Si se pasa "aleatorio", se generan placas aleatorias para cada auto.
  - Verifica que `cantidad` sea un entero > 0 y que haya espacios suficientes.
  - Por cada auto crea un evento `(placa_auto, "ENTRADA", hora_entrada, 0.00)` y lo añade a `historial_eventos` y `historial_autos`.
  - Actualiza `placas_autos`, `espacios_ocupados` y `espacios_libres`.
  - Maneja errores con mensajes legibles.

- `salida_auto(placa, cantidad=1)` — Registra la salida de autos:

  - Si `placa` es "aleatorio", selecciona aleatoriamente `cantidad` placas desde `placas_autos`.
  - Si se solicita una placa específica, verifica que existan suficientes entradas con esa placa.
  - Calcula una tarifa aleatoria entre $5.00 y $50.00 para cada auto (simulación), crea el evento `(placa_auto, "SALIDA", hora_salida, tarifa)` y lo registra en `historial_eventos` y `historial_autos`.
  - Actualiza `placas_autos`, `espacios_ocupados` y `espacios_libres`.
  - Maneja errores con mensajes legibles.

- Métodos de visualización:
  - `mostrar_estado_actual()` — Muestra en consola la capacidad, ocupación, espacios libres, % ocupación y estado.
  - `mostrar_autos_estacionados()` — Lista ordenada de placas actualmente estacionadas.
  - `mostrar_historial_auto(placa)` — Muestra los eventos (entradas/salidas) registrados para una placa específica.
  - `mostrar_ultimos_eventos(cantidad=10)` — Muestra los últimos N eventos registrados.

Notas de implementación:

- `placas_autos` permite duplicados: esto simula varios autos con la misma placa (posible en la simulación pero poco realista en la práctica).
- La tarifa se calcula aleatoriamente al salir; el atributo `TARIFA_POR_HORA` queda definido pero no usado en los cálculos actuales.
- Las horas registradas usan la hora del sistema en el momento del evento.

### 3) Interfaz por consola (`main`)

El script implementa un menú interactivo con opciones:

1. Entrada de auto(s)
2. Salida de auto(s)
3. Mostrar estado actual
4. Mostrar autos estacionados
5. Mostrar historial de auto
6. Mostrar últimos eventos
7. Simulación automática
8. Salir

Comportamiento clave:

- Para entradas/salidas, el usuario puede indicar la placa explícita o usar "aleatorio" para que el sistema genere/seleccione placas.
- La simulación automática ejecuta 5 iteraciones de entradas y salidas aleatorias (con pequeñas pausas `time.sleep(1)`) y luego muestra el estado.
- El programa maneja `KeyboardInterrupt` para permitir salir con Ctrl+C.

---

## Cómo ejecutar

Requisitos: Python 3.x instalado.

Desde la raíz del proyecto (donde se creó este `README.md`) ejecuta:

```bash
python parciales/parcial_1.py
```

En Windows PowerShell (pwsh):

```powershell
python .\parciales\parcial_1.py
```

Sugerencias de uso:

- Prueba la opción 7 para ver una simulación rápida.
- Usa "aleatorio" en entradas/salidas para simular tráfico masivo.

---

## Mejoras posibles (próximos pasos sugeridos)

- Usar `TARIFA_POR_HORA` y el tiempo real de estacionamiento (tiempo entre entrada y salida) para calcular tarifas reales.
- Evitar duplicados de placas en `placas_autos` o cambiar el modelo para almacenar instancias de vehículos con identificadores únicos.
- Persistencia: guardar `historial_eventos` en un archivo CSV o base de datos.
- Exponer una API REST o interfaz web para control remoto y visualización.
- Añadir tests unitarios para métodos clave.

---

## Licencia y autor

Archivo de ejemplo para una asignación de curso. Libre para estudiar y modificar.

---

Si deseas que mejore el README (añadir diagramas, ejemplos de salida, o instrucciones de pruebas automatizadas), dime qué prefieres y lo añado.
