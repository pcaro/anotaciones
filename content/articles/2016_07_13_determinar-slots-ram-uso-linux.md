Title: Determinar slots de RAM en uso en Linux
Date: 2016-07-13 20:28
Tags: linux, ram, dmidecode, lshw, hardware, memoria
Lang: es
Category: Linux
Slug: determinar-slots-ram-uso-linux
Summary: Comandos de Linux para determinar cuántos slots de RAM están ocupados y su capacidad usando dmidecode, lshw y técnicas de inspección de hardware

¿Cuántos **slots de RAM tienes ocupados** y cuántos libres? Linux proporciona herramientas para inspeccionar la configuración de memoria sin abrir el ordenador.

## dmidecode: La herramienta principal

### Información básica de memoria
```bash
# Ver toda la información de memoria
sudo dmidecode -t memory

# Tipo específico de memoria (tabla 16)
sudo dmidecode -t 16

# Solo los tamaños instalados
sudo dmidecode -t memory | grep -i size
```

**Salida típica**:
```
Size: 8192 MB
Size: 8192 MB
Size: No Module Installed
Size: No Module Installed
```

### Información detallada por slot
```bash
# Información granular de cada slot (tabla 17)
sudo dmidecode -t 17

# Resumen compacto
sudo dmidecode -t 17 | grep -E "(Size|Locator|Speed|Type:)"
```

**Información proporcionada**:
- **Locator**: Identificador físico del slot (DIMM_A1, DIMM_B1, etc.)
- **Size**: Capacidad instalada o "No Module Installed"
- **Type**: DDR3, DDR4, etc.
- **Speed**: Velocidad en MT/s

## lshw: Alternativa con formato estructurado

```bash
# Información de memoria con lshw
sudo lshw -class memory

# Solo memoria física (sin caché)
sudo lshw -class memory | grep -A 10 "System Memory"

# Formato más compacto
sudo lshw -short -class memory
```

## Scripts útiles para análisis

### Contador de slots ocupados
```bash
#!/bin/bash
echo "=== Análisis de slots de RAM ==="
TOTAL_SLOTS=$(sudo dmidecode -t 17 | grep "Size:" | wc -l)
OCCUPIED_SLOTS=$(sudo dmidecode -t 17 | grep "Size:" | grep -v "No Module" | wc -l)
FREE_SLOTS=$((TOTAL_SLOTS - OCCUPIED_SLOTS))

echo "Slots totales: $TOTAL_SLOTS"
echo "Slots ocupados: $OCCUPIED_SLOTS" 
echo "Slots libres: $FREE_SLOTS"
```

### Resumen detallado
```bash
#!/bin/bash
echo "=== Configuración actual de RAM ==="
sudo dmidecode -t 17 | awk '
/Memory Device/,/^$/ {
    if(/Locator:/) locator=$2
    if(/Size:/ && !/No Module/) {
        size=$2" "$3
        print locator": "size
    }
    if(/Size:.*No Module/) print locator": Vacío"
}'
```

## Información adicional útil

### Capacidad máxima soportada
```bash
# Máxima capacidad total
sudo dmidecode -t 16 | grep "Maximum Capacity"

# Número máximo de dispositivos
sudo dmidecode -t 16 | grep "Number Of Devices"
```

### Verificación de velocidad y tipo
```bash
# Velocidad configurada
sudo dmidecode -t 17 | grep -E "(Speed|Configured)"

# Tipo de memoria
sudo dmidecode -t 17 | grep "Type:" | grep -v "Error"
```

## Ejemplo de salida interpretada

```bash
$ sudo dmidecode -t 17 | grep -E "(Locator|Size|Type:)" | head -12

Locator: DIMM_A1
Size: 8192 MB  
Type: DDR4

Locator: DIMM_A2
Size: No Module Installed
Type: Unknown

Locator: DIMM_B1  
Size: 8192 MB
Type: DDR4

Locator: DIMM_B2
Size: No Module Installed
Type: Unknown
```

**Interpretación**: 
- 4 slots totales (DIMM_A1, A2, B1, B2)
- 2 slots ocupados con 8GB DDR4 cada uno
- 2 slots libres disponibles

## Limitaciones importantes

⚠️ **Precisión**: Las herramientas de línea de comandos pueden no reflejar perfectamente el hardware físico

⚠️ **Privilegios**: Se requieren permisos de root para acceder a información DMI

⚠️ **Compatibilidad**: Algunos sistemas embebidos pueden no proporcionar información completa

Para **máxima certeza**, la inspección física sigue siendo recomendable, pero estas herramientas proporcionan información suficientemente precisa para la mayoría de casos.

*Fuente original*: [Unix & Linux Stack Exchange](http://unix.stackexchange.com/questions/33249/how-to-determine-the-amount-of-ram-slots-in-use)