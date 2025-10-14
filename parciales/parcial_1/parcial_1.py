'''
Se desea implementar un sistema de gestion de parqueo inteligente para monitorear la ocupación
de los estacinamientos en un centro comercial. El equipo debe simular en python cómo funcionaría el sistema.
Se debe generar datos simulados y procesarlos con python.
'''

import random
import datetime
import time

class SistemaParqueo:
    def __init__(self):
        # Constantes
        self.CAPACIDAD_MAXIMA = 50
        self.TARIFA_POR_HORA = 5.00  # $5 por hora
        
        # Variables
        self.espacios_ocupados = 0
        self.espacios_libres = self.CAPACIDAD_MAXIMA
        self.placas_autos = []  # Lista de placas actualmente estacionadas
        self.historial_eventos = []  # Lista de tuplas con eventos
        self.historial_autos = {}  # Diccionario con historial por placa
        
    def calcular_porcentaje_ocupacion(self):
        """Calcula el porcentaje de ocupación"""
        return (self.espacios_ocupados / self.CAPACIDAD_MAXIMA) * 100
    
    def obtener_estado_parqueo(self):
        """Determina el estado del parqueo"""
        porcentaje = self.calcular_porcentaje_ocupacion()
        
        if porcentaje >= 90:
            return "LLENO"
        elif porcentaje >= 50:
            return "MEDIO OCUPADO"
        else:
            return "DISPONIBLE"
    
    def obtener_hora_actual(self):
        """Obtiene la hora actual formateada"""
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def entrada_auto(self, placa, cantidad=1):
        """Maneja la entrada de autos al parqueo"""
        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a 0")
            
            if self.espacios_libres < cantidad:
                raise ValueError(f"No hay suficientes espacios. Solo quedan {self.espacios_libres} espacios libres")
            
            for _ in range(cantidad):
                if placa == "aleatorio":
                    placa_auto = self.generar_placa_aleatoria()
                else:
                    placa_auto = placa.upper()
                
                hora_entrada = self.obtener_hora_actual()
                evento = (placa_auto, "ENTRADA", hora_entrada, 0.00)
                
                # Registrar evento
                self.historial_eventos.append(evento)
                
                # Agregar a lista actual
                self.placas_autos.append(placa_auto)
                
                # Agregar al historial del auto
                if placa_auto not in self.historial_autos:
                    self.historial_autos[placa_auto] = []
                self.historial_autos[placa_auto].append(evento)
            
            self.espacios_ocupados += cantidad
            self.espacios_libres -= cantidad
            
            print(f"✓ Entraron {cantidad} auto(s). Placa(s) registrada(s)")
            
        except ValueError as e:
            print(f"❌ Error: {e}")
    
    def salida_auto(self, placa, cantidad=1):
        """Maneja la salida de autos del parqueo"""
        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a 0")
            
            if placa not in self.placas_autos and placa != "aleatorio":
                raise ValueError(f"La placa {placa} no se encuentra en el parqueo")
            
            autos_a_remover = []
            
            if placa == "aleatorio":
                # Sacar autos aleatorios
                if len(self.placas_autos) < cantidad:
                    raise ValueError(f"No hay suficientes autos. Solo hay {len(self.placas_autos)} autos estacionados")
                
                autos_a_remover = random.sample(self.placas_autos, cantidad)
            else:
                # Verificar si hay suficientes autos con esa placa
                conteo_placa = self.placas_autos.count(placa)
                if conteo_placa < cantidad:
                    raise ValueError(f"Solo hay {conteo_placa} auto(s) con placa {placa}")
                
                autos_a_remover = [placa] * cantidad
            
            for placa_auto in autos_a_remover:
                # Remover de la lista actual
                self.placas_autos.remove(placa_auto)
                
                # Calcular tarifa (simulada)
                tarifa = round(random.uniform(5.0, 50.0), 2)  # Tarifa aleatoria entre $5 y $50
                
                hora_salida = self.obtener_hora_actual()
                evento = (placa_auto, "SALIDA", hora_salida, tarifa)
                
                # Registrar evento
                self.historial_eventos.append(evento)
                
                # Agregar al historial del auto
                self.historial_autos[placa_auto].append(evento)
            
            self.espacios_ocupados -= cantidad
            self.espacios_libres += cantidad
            
            print(f"✓ Salieron {cantidad} auto(s). Tarifa(s) calculada(s)")
            
        except ValueError as e:
            print(f"❌ Error: {e}")
    
    def generar_placa_aleatoria(self):
        """Genera una placa de auto aleatoria"""
        letras = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
        numeros = ''.join(random.choices('0123456789', k=3))
        return f"{letras}-{numeros}"
    
    def mostrar_estado_actual(self):
        """Muestra el estado actual del parqueo"""
        print("\n" + "="*50)
        print("ESTADO ACTUAL DEL PARQUEO")
        print("="*50)
        print(f"Capacidad máxima: {self.CAPACIDAD_MAXIMA}")
        print(f"Espacios ocupados: {self.espacios_ocupados}")
        print(f"Espacios libres: {self.espacios_libres}")
        print(f"Porcentaje de ocupación: {self.calcular_porcentaje_ocupacion():.1f}%")
        print(f"Estado: {self.obtener_estado_parqueo()}")
        print("="*50)
    
    def mostrar_autos_estacionados(self):
        """Muestra todos los autos actualmente estacionados"""
        print(f"\nAutos estacionados ({len(self.placas_autos)}):")
        if not self.placas_autos:
            print("No hay autos estacionados")
        else:
            for i, placa in enumerate(sorted(self.placas_autos), 1):
                print(f"{i}. {placa}")
    
    def mostrar_historial_auto(self, placa):
        """Muestra el historial de eventos de un auto específico"""
        placa = placa.upper()
        if placa in self.historial_autos:
            print(f"\nHistorial del auto {placa}:")
            for evento in self.historial_autos[placa]:
                print(f"  {evento[1]} - {evento[2]} - ${evento[3]:.2f}")
        else:
            print(f"No se encontró historial para la placa {placa}")
    
    def mostrar_ultimos_eventos(self, cantidad=10):
        """Muestra los últimos eventos del parqueo"""
        print(f"\nÚltimos {cantidad} eventos:")
        eventos_recientes = self.historial_eventos[-cantidad:] if self.historial_eventos else []
        
        if not eventos_recientes:
            print("No hay eventos registrados")
        else:
            for evento in eventos_recientes:
                print(f"  {evento[0]} - {evento[1]} - {evento[2]} - ${evento[3]:.2f}")

def main():
    sistema = SistemaParqueo()
    
    print("🚗 SISTEMA DE PARQUEO INTELIGENTE 🚗")
    print("Simulación de estacionamiento de centro comercial")
    
    while True:
        print("\n" + "="*50)
        print("MENÚ PRINCIPAL")
        print("="*50)
        print("1. Entrada de auto(s)")
        print("2. Salida de auto(s)")
        print("3. Mostrar estado actual")
        print("4. Mostrar autos estacionados")
        print("5. Mostrar historial de auto")
        print("6. Mostrar últimos eventos")
        print("7. Simulación automática")
        print("8. Salir")
        print("="*50)
        
        try:
            opcion = input("Seleccione una opción (1-8): ").strip()
            
            if opcion == "1":
                placa = input("Ingrese la placa del auto (o 'aleatorio' para placa aleatoria): ").strip()
                cantidad = input("Cantidad de autos (Enter para 1): ").strip() or "1"
                sistema.entrada_auto(placa, cantidad)
                
            elif opcion == "2":
                placa = input("Ingrese la placa del auto (o 'aleatorio' para salida aleatoria): ").strip()
                cantidad = input("Cantidad de autos (Enter para 1): ").strip() or "1"
                sistema.salida_auto(placa, cantidad)
                
            elif opcion == "3":
                sistema.mostrar_estado_actual()
                
            elif opcion == "4":
                sistema.mostrar_autos_estacionados()
                
            elif opcion == "5":
                placa = input("Ingrese la placa del auto: ").strip()
                sistema.mostrar_historial_auto(placa)
                
            elif opcion == "6":
                cantidad = input("Cantidad de eventos a mostrar (Enter para 10): ").strip() or "10"
                sistema.mostrar_ultimos_eventos(int(cantidad))
                
            elif opcion == "7":
                # Simulación automática
                print("\n🔧 Iniciando simulación automática...")
                for _ in range(5):
                    # Entradas aleatorias
                    entradas = random.randint(1, 5)
                    sistema.entrada_auto("aleatorio", entradas)
                    time.sleep(1)
                    
                    # Salidas aleatorias
                    if sistema.espacios_ocupados > 0:
                        salidas = random.randint(1, min(3, sistema.espacios_ocupados))
                        sistema.salida_auto("aleatorio", salidas)
                        time.sleep(1)
                
                sistema.mostrar_estado_actual()
                
            elif opcion == "8":
                print("¡Gracias por usar el sistema de parqueo inteligente!")
                break
                
            else:
                print("❌ Opción no válida. Por favor seleccione 1-8.")
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()