# eventos_seguridad.ps1
# Obtiene los ultimos 50 eventos del log de seguridad de Windows
# y los exporta a un archivo CSV, verificando el resultado.

$logName    = "Security"
$cantidad   = 50
$archivoCsv = "eventos.csv"

Write-Output "Obteniendo los ultimos $cantidad eventos del log '$logName'..."

try {
    $eventos = Get-EventLog -LogName $logName -Newest $cantidad -ErrorAction Stop
    $eventos | Export-Csv -Path $archivoCsv -NoTypeInformation

    if (Test-Path -Path $archivoCsv) {
        Write-Output "Exito: el archivo '$archivoCsv' fue creado correctamente."
        Write-Output "Cantidad de eventos exportados: $($eventos.Count)"
    } else {
        Write-Output "Error: el archivo '$archivoCsv' no fue generado."
    }
}
catch {
    Write-Output "Error al obtener o exportar los eventos: $($_.Exception.Message)"
}
