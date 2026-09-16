# Redes de Computadoras — Apuntes

## 1. ¿Qué es una red de computadoras?
Una red de computadoras es el proceso de conectar computadoras y otros dispositivos para que puedan comunicarse, compartir recursos e intercambiar datos entre sí. Permite que los dispositivos trabajen juntos, ya sea en una red pequeña doméstica o una red grande como Internet.

## 2. Tipos de redes (por tamaño y alcance)
- **PAN** – Red de área personal (ej.: Bluetooth, punto de acceso del teléfono).
- **LAN** – Red de área local (ej.: hogar, oficina, escuela).
- **MAN** – Red de área metropolitana (ej.: ciudad).
- **WAN** – Red de área amplia (ej.: países, Internet).

> Las redes más grandes cubren áreas más amplias: WAN ⊃ MAN ⊃ LAN ⊃ PAN.

## 3. Dispositivos clave en una red
- **Router** – Conecta diferentes redes y enruta los datos.
- **Switch** – Conecta dispositivos dentro de la misma red.
- **Hub** – Envía datos a todos los dispositivos (menos común).
- **Módem** – Conecta tu red a Internet.
- **Punto de acceso** – Proporciona una red inalámbrica (WiFi).

## 4. Tipos de redes comunes
- **Red cableada** – Utiliza cables (Ethernet).
- **Red inalámbrica** – Utiliza ondas de radio (WiFi).
- **VPN** – Crea una conexión segura a través de Internet.

## 5. Dispositivos de red (detalle)
| Dispositivo | Función | Ejemplo |
|---|---|---|
| Router | Ruta los datos entre diferentes redes | Router doméstico, ISP |
| Switch | Conecta dispositivos en la misma red | Switch de 24 puertos |
| Hub | Envía datos a todos los dispositivos (menos común) | Hub antiguo |
| Módem | Conecta una red local con el ISP | Módem por cable |
| Punto de acceso | Proporciona acceso WiFi a los dispositivos | Router WiFi |

## 6. Topologías de red
La topología de red es el arreglo de los dispositivos en una red.
- **Bus** – Todos los dispositivos comparten un mismo cable.
- **Estrella** – Todos los dispositivos se conectan a un dispositivo central.
- **Anillo** – Los dispositivos están conectados en un círculo.
- **Malla** – Los dispositivos se conectan con muchos otros dispositivos.
- **Árbol** – Conexión jerárquica (como un árbol).

## 7. Direccionamiento IP
La dirección IP es un número único asignado a cada dispositivo en una red.
- **IPv4** – Dirección de 32 bits (ej.: 192.168.1.1).
- **IPv6** – Dirección de 128 bits (ej.: 2001:0db8::1).

Tipos:
- **Pública** – Se usa en Internet.
- **Privada** – Se usa en redes locales.

**Ejemplos de rangos IP:**
- Privadas (IPv4): 192.168.0.0 – 192.168.255.255
- Loopback (IPv4): 127.0.0.1
- Públicas (IPv4): 1.0.0.0 – 223.255.255.255

## 8. Protocolos de red
Los protocolos son reglas que controlan cómo se envían, reciben y entienden los datos.
- **TCP** – Confiable, orientado a la conexión (ej.: web, correo electrónico).
- **UDP** – Más rápido, sin conexión (ej.: transmisión de video, juegos en línea).
- **HTTP** – Transferencia de páginas web.
- **HTTPS** – Versión segura de HTTP (usa cifrado).
- **FTP** – Transferencia de archivos en una red.

## 9. Tipos de redes (resumen con diagrama)
Las redes se clasifican según su tamaño y alcance: WAN, MAN, LAN, PAN (de mayor a menor alcance).

## 10-11. Cables de red y conectores
- **Par trenzado** – Se usa en redes LAN (ej.: Cat5e, Cat6).
- **Cable coaxial** – Se usa en redes más antiguas (menos común).
- **Fibra óptica** – Se usa para alta velocidad y largas distancias.

**Conectores:** RJ45 (Ethernet), BNC (Coaxial), SC (Fibra óptica).

## 12. Clases de direcciones IP
| Clase | Rango (primer octeto) | Máscara por defecto | Se usa para |
|---|---|---|---|
| A | 1 – 126 | 255.0.0.0 | Grandes redes |
| B | 128 – 191 | 255.255.0.0 | Redes medianas |
| C | 192 – 223 | 255.255.255.0 | Redes pequeñas |
| D | 224 – 239 | – | Multidifusión |
| E | 240 – 255 | – | Experimental |

**Rangos privados:**
- 10.0.0.0 – 10.255.255.255
- 172.16.0.0 – 172.31.255.255
- 192.168.0.0 – 192.168.255.255

## 17. Seguridad de la red
La seguridad de la red protege los datos y dispositivos de amenazas y accesos no autorizados.
- **Firewall** – Bloquea el tráfico no deseado.
- **Antivirus** – Detecta y elimina malware.
- **Cifrado** – Mantiene los datos seguros (HTTPS).
- **VPN** – Crea un túnel seguro en Internet.
- **IDS/IPS** – Detecta y previene ataques.

Flujo: `Internet → Firewall → Red interna`

## 19. Modelos y protocolos de red (resumen rápido)

**Modelo OSI (7 capas)**
7. Aplicación
6. Presentación
5. Sesión
4. Transporte
3. Red
2. Enlace de datos
1. Física

**Modelo TCP/IP (4 capas)**
4. Aplicación (HTTP, FTP, DNS)
3. Transporte (TCP, UDP)
2. Internet (IP)
1. Acceso a la red (Ethernet, WiFi)

**Diferencia clave:**
- OSI tiene 7 capas (teórico).
- TCP/IP tiene 4 capas (práctico).
- TCP/IP se usa ampliamente en Internet.
- OSI ayuda a comprender los conceptos de red.

## 20. Comandos de redes comunes
| Comando | Función |
|---|---|
| `ping` | Verifica si un dispositivo es alcanzable |
| `ipconfig` | Muestra la configuración IP (Windows) |
| `ifconfig` | Muestra la configuración IP (Linux) |
| `tracert` | Muestra la ruta hacia un destino |
| `netstat` | Muestra conexiones activas |
| `nslookup` | Busca nombres de dominio |
| `arp` | Muestra la tabla ARP |
| `route` | Muestra la tabla de enrutamiento |

## 21. Tipos de topologías de red
- **Bus** – Todos los dispositivos comparten un solo cable.
- **Estrella** – Todos los dispositivos se conectan a un dispositivo central.
- **Anillo** – Los dispositivos se conectan en un círculo.
- **Malla** – Conexión jerárquica (como un árbol).

## 22. Internet y sus servicios
Internet es una red global de redes que conecta millones de dispositivos y brinda numerosos servicios.
- **Web** – Acceso a sitios web (ej. Google, YouTube).
- **Correo electrónico** – Envío y recepción de mensajes.
- **FTP** – Transferencia de archivos.
- **Chat** – Comunicación en tiempo real.
- **Nube** – Almacenamiento de datos en línea (ej.: Google Drive).

## 23. Dispositivos de red y sus funciones (ejemplo de configuración)
Flujo típico: `Laptop → Switch → Router → Internet (WiFi / Punto de acceso)`

## 25. Tipos de seguridad de red
- **Firewall** – Bloquea el acceso no autorizado.
- **Antivirus** – Detecta y elimina malware.
- **Cifrado** – Protege los datos convirtiéndolos en código.
- **VPN** – Crea una conexión segura a través de Internet.
- **IDS/IPS** – Detecta y previene ataques.

Flujo: `Usuario → Firewall → Internet → Servidor` (red protegida, con cifrado de vuelta).

## 27. Ancho de banda de red
El ancho de banda es la cantidad de datos que se pueden transmitir en una red en un período de tiempo determinado.
- **Medido en** – bps (bits por segundo).
- **Unidades comunes** – Kbps, Mbps, Gbps.
- Mayor ancho de banda = transferencia de datos más rápida.
- Menor ancho de banda = transferencia de datos más lenta.

**Comparación:**
| Tecnología | Ancho de banda |
|---|---|
| Dial-up | 56 Kbps |
| Banda ancha | 10 Mbps |
| Fibra óptica | 1 Gbps |

## 28. Capas de la red (Modelo TCP/IP)
| Capa | Nombre | Función | Ejemplos |
|---|---|---|---|
| 4 | Aplicación | Proporciona servicios de red a las aplicaciones | HTTP, FTP, DNS |
| 3 | Transporte | Maneja la entrega y la confiabilidad de los datos | TCP, UDP |
| 2 | Internet | Maneja el enrutamiento y el direccionamiento | IP, ICMP |
| 1 | Acceso a la red | Gestiona la conexión física y el enlace de datos | Ethernet, WiFi |

> El modelo TCP/IP es un modelo práctico, mientras que el modelo OSI tiene 7 capas.

## Conclusión
El trabajo en redes permite que los dispositivos se comuniquen, compartan recursos y accedan a información. Se utilizan diferentes dispositivos, protocolos y topologías para que Internet y las redes locales funcionen de manera eficiente.
