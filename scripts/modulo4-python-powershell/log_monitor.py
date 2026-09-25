#!/usr/bin/env python3
"""
log_monitor.py
Script de monitoreo de logs para entorno Linux.
Lee el archivo accesos.log, detecta las lineas que contienen "sudo"
y genera un reporte estructurado en reporte_sudo.txt.
"""


def analizar_log(archivo_entrada, archivo_salida, patron="sudo"):
    lineas_detectadas = []
    contador = 0

    # Lectura del archivo de log linea por linea
    try:
        with open(archivo_entrada, "r") as log:
            for linea in log:
                if patron in linea:
                    lineas_detectadas.append(linea.strip())
                    contador += 1
    except FileNotFoundError:
        print(f"Error: no se encontro el archivo '{archivo_entrada}'.")
        return

    # Escritura del reporte de salida
    with open(archivo_salida, "w") as reporte:
        reporte.write(f"Reporte de comandos ejecutados con '{patron}'\n")
        reporte.write("=" * 50 + "\n\n")

        if lineas_detectadas:
            for linea in lineas_detectadas:
                reporte.write(linea + "\n")
        else:
            reporte.write("No se encontraron coincidencias.\n")

        reporte.write("\n" + "-" * 50 + "\n")
        reporte.write(f"Total de ocurrencias encontradas: {contador}\n")

    print(f"Analisis completado. Se detectaron {contador} linea(s) con '{patron}'.")
    print(f"Reporte generado en: {archivo_salida}")


if __name__ == "__main__":
    ARCHIVO_LOG = "accesos.log"
    ARCHIVO_REPORTE = "reporte_sudo.txt"
    analizar_log(ARCHIVO_LOG, ARCHIVO_REPORTE)
log_monitor.py
