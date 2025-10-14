"""
PARTE 4: ANALISIS Y DECISIoN DE ALERTAS
El jugador analiza alertas y decide cuales atender
"""

def toggle_seleccion_alerta(self, indice):
    """
    Selecciona o deselecciona una alerta para atender.
    El jugador puede hacer clic en una alerta para marcarla.
    
    Args:
        indice: Índice de la alerta en la lista de alertas actuales
    """
    if indice in self.alertas_seleccionadas:
        self.alertas_seleccionadas.remove(indice)
    else:
        self.alertas_seleccionadas.add(indice)


def procesar_decisiones(self):
    """
    Procesa las decisiones del administrador de sistemas TI.
    Analiza cada alerta y determina si la decisión fue correcta:
    - Alerta REAL atendida: +2 puntos (correcto)
    - Alerta FALSA atendida: -1 punto (error)
    - Alerta REAL NO atendida: -2 puntos (crítico)
    - Alerta FALSA NO atendida: 0 puntos (correcto)
    """
    if self.estado_juego != "analizando":
        return
    
    resultados = []
    puntos_ganados = 0
    
    # Analizar las alartas 
    for i, alerta in enumerate(self.alertas_actuales):
        atendida = i in self.alertas_seleccionadas
        
        if atendida:
            # el admin decidio atender esta alerta
            if alerta["real"]:
                resultado = "CORRECTO (+2)"
                self.puntos += 2
                puntos_ganados += 2
            else:
                resultado = "ERROR (-1)"
                self.puntos -= 1
                puntos_ganados -= 1
        else:
            # el admin decidio no atender esta alerta
            if alerta["real"]:
                resultado = "CRÍTICO (-2)"
                self.puntos -= 2
                puntos_ganados -= 2
            else:
                resultado = "CORRECTO (0)"
        
        #resultado para mostrar feedback
        resultados.append({
            "alerta": alerta,
            "atendida": atendida,
            "resultado": resultado
        })
    
    # resultados por turnos
    self.resultado_turno = {
        "resultados": resultados,
        "puntos_ganados": puntos_ganados
    }
    self.estado_juego = "resultado"


def dibujar_pantalla_analizando(self):
    """
    Dibuja la pantalla donde el administrador TI analiza las alertas.
    Muestra todas las alertas con su información y permite seleccionarlas.
    
    El administrador debe considerar:
    - Severidad del evento
    - Tipo de dispositivo
    - Mensaje de la alerta
    - Contexto temporal (hora)
    """
    self.screen.fill(self.GRIS_CLARO)
    self.dibujar_header()
    
    y = 100
    self.dibujar_texto("ALERTAS DETECTADAS - Seleccione las que atenderá:", 
                      20, y, self.font_normal, self.GRIS_OSCURO)
    
    y += 40
    
    # alertas con scroll
    alerta_height = 90
    max_visible = 4
    
    # mostra alert
    for i, alerta in enumerate(self.juego.alertas_actuales):
        if i < self.scroll_offset:
            continue
        if i >= self.scroll_offset + max_visible:
            break
        
        # cambia color si esta selec
        seleccionada = i in self.juego.alertas_seleccionadas
        color_fondo = self.VERDE if seleccionada else self.BLANCO
        color_borde = self.GRIS_OSCURO if seleccionada else self.GRIS
        
        # Dibu caja de alerta
        rect = pygame.Rect(20, y, self.ANCHO - 40, alerta_height)
        pygame.draw.rect(self.screen, color_fondo, rect, border_radius=8)
        pygame.draw.rect(self.screen, color_borde, rect, 3, border_radius=8)
        
        # info alerta para análisis
        self.dibujar_texto(f"#{i+1} - {alerta['dispositivo']}", 
                          30, y + 10, self.font_normal, self.NEGRO)
        
        self.dibujar_texto(f"Mensaje: {alerta['mensaje']}", 
                          30, y + 35, self.font_pequeña, self.GRIS_OSCURO)
        
        #severidad???????
        sev_color = self.ROJO if alerta['severidad'] >= 4 else (
            self.NARANJA if alerta['severidad'] >= 3 else self.AMARILLO)
        self.dibujar_texto(f"Severidad: {alerta['severidad']}/5", 
                          30, y + 60, self.font_pequeña, sev_color)
        
        # ta selecionada 
        estado = "✓ SELECCIONADA" if seleccionada else "Clic para seleccionar"
        self.dibujar_texto(estado, self.ANCHO - 250, y + 35, 
                          self.font_pequeña, self.GRIS_OSCURO)
        
        y += alerta_height + 10
    
    # Botones del admin
    y = self.ALTO - 70
    
    # confirmar la funa 
    if self.dibujar_boton("CONFIRMAR DECISIONES", 
                         self.ANCHO // 2 - 250, y, 230, 50, 
                         self.VERDE, self.BLANCO):
        return "procesar"
    
    # se equivoca/reiniciar 
    if self.dibujar_boton("REINICIAR SELECCIÓN", 
                         self.ANCHO // 2 + 20, y, 230, 50, 
                         self.NARANJA, self.BLANCO):
        return "reiniciar"
    
    return None


def manejar_click_alertas(self, pos):
    """
    Maneja los clicks del administrador en las alertas.
    Permite seleccionar/deseleccionar alertas para atender.
    
    Args:
        pos: Posición (x, y) del click del mouse
    """
    x, y = pos
    
    # verifica el click
    if y < 140 or y > 500:
        return
    
    # Calcular clickeada
    alerta_height = 90
    indice = ((y - 140) // (alerta_height + 10)) + self.scroll_offset
    
    # seleccionar/deseleccionar 
    if 0 <= indice < len(self.juego.alertas_actuales):
        self.juego.toggle_seleccion_alerta(indice)


def dibujar_pantalla_resultado(self):
    """
    Muestra el feedback de las decisiones del administrador.
    Indica qué alertas eran reales/falsas y si la decisión fue correcta.
    """
    self.screen.fill(self.GRIS_CLARO)
    self.dibujar_header()
    
    y = 100
    self.dibujar_texto("ANÁLISIS DE DECISIONES:", 20, y, 
                      self.font_titulo, self.GRIS_OSCURO)
    
    y += 50
    
    for dato in self.juego.resultado_turno["resultados"]:
        alerta = dato["alerta"]
        tipo = "REAL" if alerta["real"] else "FALSA"
        estado = "Atendida" if dato["atendida"] else "Ignorada"
        
        color = self.VERDE if "CORRECTO" in dato["resultado"] else self.ROJO
        
        texto = f"[{tipo}] {estado} - {alerta['dispositivo']}: {dato['resultado']}"
        self.dibujar_texto(texto, 30, y, self.font_pequeña, color)
        y += 25
    
    y += 20
    puntos = self.juego.resultado_turno["puntos_ganados"]
    texto_puntos = f"Puntos este turno: {puntos:+d}"
    color_puntos = self.VERDE if puntos >= 0 else self.ROJO
    self.dibujar_texto(texto_puntos, 30, y, self.font_normal, color_puntos)
    
    y = self.ALTO - 70
    if self.dibujar_boton("CONTINUAR AL SIGUIENTE TURNO", 
                         self.ANCHO // 2 - 150, y, 300, 50, 
                         self.AZUL, self.BLANCO):
        return "siguiente"

    return None