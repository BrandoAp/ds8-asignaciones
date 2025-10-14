import random
from datetime import datetime


class Dispositivo:
    def __init__(self, nombre, tipo, fiabilidad=0.9):
        self.nombre = nombre
        self.tipo = tipo
        self.fiabilidad = fiabilidad

    def generar_alerta(self):
        raise NotImplementedError


class MotionSensor(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre, "Movimiento")

    def generar_alerta(self):
        movimiento = random.choices([True, False])
        real = movimiento and random.random() < 0.8
        if movimiento or random.random() < 0.2:
            return {
                "dispositivo": self.nombre,
                "mensaje": "Movimiento detectado" if movimiento else "Falsa detección",
                "severidad": random.randint(1, 5),
                "real": real,
            }


class TemperatureSensor(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre, "Temperatura")

    def generar_alerta(self):
        temp = random.uniform(15, 50)
        real = temp > 40
        if random.random() < 0.3 or real:
            return {
                "dispositivo": self.nombre,
                "mensaje": f"Temperatura {temp:.1f}°C",
                "severidad": 5 if real else 2,
                "real": real,
            }


class PowerSensor(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre, "Energía")

    def generar_alerta(self):
        consumo = random.uniform(50, 700)
        real = consumo > 600
        if random.random() < 0.3 or real:
            return {
                "dispositivo": self.nombre,
                "mensaje": f"Consumo {consumo:.0f}W",
                "severidad": 4 if real else 2,
                "real": real,
            }


class NoiseSensor(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre, "Ruido")

    def generar_alerta(self):
        ruido = random.uniform(20, 100)
        real = ruido > 80
        if random.random() < 0.3 or real:
            return {
                "dispositivo": self.nombre,
                "mensaje": f"Ruido {ruido:.0f}db",
                "severidad": 3,
                "real": real,
            }


class Camera(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre, "Cámara")

    def generar_alerta(self):
        evento = random.choice(["movimiento", "error", "ok"])
        real = evento == "movimiento"
        if evento != "ok":
            return {
                "dispositivo": self.nombre,
                "mensaje": f"Cámara detecta {evento}",
                "severidad": 4 if real else 2,
                "real": real,
            }
