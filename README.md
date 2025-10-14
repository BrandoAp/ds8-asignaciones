# ds8-asignaciones — Instalación y desarrollo local

Resumen breve
- Repositorio con ejercicios y laboratorios (p. ej. `laboratorios/laboratorio2/DispositivosIoT.py`).
- Este README explica cómo preparar el entorno y ejecutar el proyecto en Windows para desarrollo local.

Requisitos
- Windows 10/11
- Python 3.10+ (recomendado)
- Git (opcional, para control de versiones)
- VS Code (recomendado) con la extensión Python

Preparar entorno (recomendado: venv)
1. Abrir PowerShell o CMD en la raíz del proyecto:
   - PowerShell: `cd "c:\Users\avila\OneDrive\Desktop\learning\ds8-asignaciones"`
2. Crear y activar entorno virtual:
   - PowerShell:
     ```
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - CMD:
     ```
     python -m venv .venv
     .\.venv\Scripts\activate
     ```
3. Actualizar pip y setuptools (opcional):
   ```
   python -m pip install --upgrade pip setuptools
   ```

Instalar dependencias
- Si existe `requirements.txt`:
  ```
  pip install -r requirements.txt
  ```
- Si no existe y quieres generar una lista después de instalar paquetes:
  ```
  pip freeze > requirements.txt
  ```

Ejecución de archivos Python
- Para ejecutar el script principal de ejemplo:
  ```
  python laboratorios\laboratorio2\DispositivosIoT.py
  ```
- Para ejecutar cualquier otro módulo, usar la ruta relativa desde la raíz del proyecto.

Buenas prácticas en desarrollo
- Abrir el proyecto en VS Code:
  - Desde PowerShell/CMD:
    ```
    code .
    ```
- Usar el intérprete Python del entorno virtual en VS Code (seleccionarlo en la paleta de comandos).
- Formateo / linting (opcional):
  ```
  pip install black flake8
  black .
  flake8 .
  ```

Tests
- Si se agregan pruebas con pytest:
  ```
  pip install pytest
  pytest
  ```
- Crear carpeta `tests/` y nombrar archivos `test_*.py`.

Estructura sugerida del proyecto
- laboratorios/
  - laboratorio2/
    - DispositivosIoT.py
- README.md
- requirements.txt
- .venv/ (no versionar)

Consejos para contribuir
- Crear una rama por feature:
  ```
  git checkout -b feat/nombre-feature
  ```
- Hacer commits claros y abrir Pull Request al repositorio principal.
- Añadir tests para nuevas funcionalidades.

Solución de problemas comunes
- "python no se reconoce": verificar instalación de Python y PATH.
- Entorno no activado en VS Code: seleccionar intérprete .venv manualmente.
- Problemas con permisos en PowerShell al activar venv: ejecutar `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force` (si es apropiado y seguro).

Contacto / Autor
- Archivo creado para uso educativo. Para cambios específicos solicita detalles y se ajusta el README.

Notas finales
- README enfocado en desarrollo local en Windows. Si quieres, puedo:
  - Añadir instrucciones para Docker.
  - Generar `requirements.txt` automáticamente.
  - Incluir ejemplos de salida del script `DispositivosIoT.py`.
