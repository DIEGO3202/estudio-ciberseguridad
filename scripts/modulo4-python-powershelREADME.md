# Scripting multiplataforma — Python y PowerShell

Dos scripts de monitoreo y detección de eventos de seguridad, uno para Linux (Python) y otro para Windows (PowerShell), como parte de mi módulo de scripting multiplataforma.

## Contenido

| Archivo | Lenguaje | Descripción |
|---|---|---|
| `log_monitor.py` | Python | Lee un archivo de log, detecta líneas con `sudo` y genera un reporte (`reporte_sudo.txt`) con el detalle y el total de ocurrencias. |
| `eventos_seguridad.ps1` | PowerShell | Obtiene los últimos 50 eventos del log de seguridad de Windows, los exporta a CSV y verifica que el archivo se haya creado correctamente. |

## Qué practiqué acá

- Lectura y escritura de archivos con manejo de errores (`try/except` en Python, `try/catch` en PowerShell).
- Estructuras condicionales y bucles para procesar datos línea por línea.
- Cmdlets de PowerShell orientados a seguridad: `Get-EventLog`, `Export-Csv`, `Test-Path`.
- Buenas prácticas de portabilidad: cada script pensado para el entorno donde realmente corre, rutas configurables como variables, salida clara en consola para trazabilidad.

## Cómo ejecutarlos

**Python (Linux):**
```bash
python3 log_monitor.py
```
Requiere un archivo `accesos.log` en el mismo directorio.

**PowerShell (Windows):**
```powershell
.\eventos_seguridad.ps1
```
Puede requerir permisos de administrador para leer el log de seguridad.
