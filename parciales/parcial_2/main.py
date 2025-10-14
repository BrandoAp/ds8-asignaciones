import pygame
import random
import sys
from devices import *
from datetime import datetime


pygame.init()
ANCHO, ALTO = 800, 600

screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Seguridad IoT")
font = pygame.font.SysFont(None, 24)

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 100, 100)
VERDE = (100, 255, 100)
AZUL = (100, 100, 255)

devices = [
    MotionSensor("Sensor de Movimiento"),
    TemperatureSensor("Sensor de Temperatura"),
    PowerSensor("Sensor de Energía"),
    NoiseSensor("Sensor de Ruido"),
    Camera("Cámara de Seguridad"),
]

alertas = []
turno = 0
puntaje = 0
alerta_seleccionada = None
mensaje = ""

clock = pygame.time.Clock()


def nueva_alerta():
    global alertas, turno
    alertas = []
    turno += 1
    for d in devices:
        alerta = d.generar_alerta()
        if alerta:
            alertas.append(alerta)


def dibujar_texto(texto, x, y, color=NEGRO):
    txt = font.render(texto, True, color)
    screen.blit(txt, (x, y))


running = True
while running:
    screen.fill(BLANCO)

    dibujar_texto(f"Turno: {turno}", 20, 20)
    dibujar_texto(f"Puntaje: {puntaje}", 150, 20)
    dibujar_texto(f"Alertas activas: {len(alertas)}", 300, 20)
    dibujar_texto("Presiona ESPACIO para generar alertas", 20, 60)
    dibujar_texto("Selecciona alerta (click) y presiona R (real) o F (falsa)", 20, 85)

    y = 130
    for i, alerta in enumerate(alertas):
        color = ROJO if i == alerta_seleccionada else AZUL
        pygame.draw.rect(screen, color, (20, y, 760, 40), 2)
        dibujar_texto(
            f"{alerta['dispositivo']} - {alerta['mensaje']}, (Sev: {alerta['severidad']})",
            30,
            y + 10,
        )
        y += 50

    if mensaje:
        dibujar_texto(mensaje, 20, 550, VERDE if "Correcto" in mensaje else ROJO)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                nueva_alerta()
                alerta_seleccionada = None
                mensaje = ""

            elif event.key == pygame.K_r and alerta_seleccionada is not None:
                alerta = alertas[alerta_seleccionada]
                if alerta["real"]:
                    puntaje += 10
                    mensaje = "Correcto (+10)"
                else:
                    puntaje -= 5
                    mensaje = " Incorrecto (-5)"
                alertas.pop(alerta_seleccionada)
                alerta_seleccionada = None

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 20 <= x <= 780:
                idx = (y - 130) // 50
                if 0 <= idx < len(alertas):
                    alerta_seleccionada = idx

    clock.tick(30)

pygame.quit()
sys.exit
