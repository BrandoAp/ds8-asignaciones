class SistemaPuntuacion:
    """
    Clase encargada de calcular y administrar el puntaje del juego
    según las decisiones del administrador de sistemas TI.
    """

    def __init__(self, puntos_iniciales=15):
        self.puntos = puntos_iniciales
        self.historial = []  # Guarda las evaluaciones de cada turno

    def evaluar_alerta(self, alerta, atendida):
        """
        Evalúa una alerta según si fue atendida o no y si era real o falsa.
        Devuelve el resultado textual y los puntos obtenidos.

        Reglas:
        - Alerta REAL atendida: +2 puntos
        - Alerta FALSA atendida: -1 punto
        - Alerta REAL NO atendida: -2 puntos
        - Alerta FALSA NO atendida: 0 puntos
        """
        if atendida:
            if alerta["real"]:
                delta = 2
                resultado = "Correcto (+2)"
            else:
                delta = -1
                resultado = "Error (-1)"
        else:
            if alerta["real"]:
                delta = -2
                resultado = "Crítico (-2)"
            else:
                delta = 0
                resultado = "Correcto (0)"

        self.puntos += delta
        return resultado, delta

    def procesar_turno(self, alertas, seleccionadas):
        """
        Procesa un turno completo y devuelve un resumen de resultados.

        Args:
            alertas (list): Lista de alertas generadas en el turno.
            seleccionadas (set): Índices de alertas atendidas por el jugador.
        """
        resultados = []
        puntos_turno = 0

        for i, alerta in enumerate(alertas):
            atendida = i in seleccionadas
            resultado, delta = self.evaluar_alerta(alerta, atendida)
            puntos_turno += delta
            resultados.append({
                "alerta": alerta,
                "atendida": atendida,
                "resultado": resultado,
                "delta": delta
            })

        # Guardar en el historial global
        self.historial.append({
            "alertas": resultados,
            "puntos_turno": puntos_turno,
            "puntos_totales": self.puntos
        })

        return resultados, puntos_turno

    def obtener_puntaje_total(self):
        """Devuelve los puntos acumulados actuales."""
        return self.puntos

    def resumen(self):
        """Devuelve un resumen textual del progreso del jugador."""
        texto = ["=== Historial de Turnos ==="]
        for idx, turno in enumerate(self.historial, start=1):
            texto.append(f"Turno {idx}: +{turno['puntos_turno']} puntos (Total: {turno['puntos_totales']})")
        return "\n".join(texto)
