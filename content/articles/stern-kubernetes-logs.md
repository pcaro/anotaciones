Title: Stern: Logs de Kubernetes con esteroides
Slug: stern-kubernetes-logs
Date: 2026-02-20
Tags: kubernetes, cli, logs, devops, tools
Category: DevOps
Lang: es

Si trabajas con Kubernetes, probablemente hayas sufrido el comando `kubectl logs`. Es útil para ver los logs de un pod específico, pero se queda corto cuando tienes múltiples réplicas de un servicio o cuando los pods se reinician y cambian de nombre.

Aquí es donde entra **[Stern](https://github.com/stern/stern)**.

Stern te permite hacer "tail" (seguir) logs de múltiples pods y contenedores dentro de Kubernetes simultáneamente. Lo mejor de todo es que utiliza expresiones regulares para seleccionar los pods, por lo que no necesitas copiar y pegar esos IDs aleatorios (`pod-1234567890-abcde`).

## Instalación

Stern es muy popular y está disponible en la mayoría de gestores de paquetes.### Usando Krew (recomendado)
Si ya usas `kubectl`, Krew es la forma más natural de instalar plugins:

```bash
kubectl krew install stern
```

### Usando Homebrew
```bash
brew install stern
```

### Binario directo
También puedes descargar el binario directamente desde sus [releases en GitHub](https://github.com/stern/stern/releases).

Si utilizas algún helper como `gah` (GitHub Asset Helper) o scripts personalizados, la instalación es tan sencilla como:

```bash
gah install stern/stern
```

## Características principales

### 1. Tailing de múltiples pods
En lugar de buscar el nombre exacto del pod, puedes usar una regex:

```bash
stern backend
```

Esto mostrará los logs de todos los pods que contengan "backend" en su nombre (`backend-api`, `backend-worker`, etc.), intercalados y coloreados para distinguirlos fácilmente.

### 2. Filtrado y exclusión
Puedes filtrar el contenido de los logs sobre la marcha sin necesidad de `grep`:

```bash
# Solo mostrar líneas que contengan "Error"
stern backend -i Error

# Excluir líneas que contengan "Health check"
stern backend -e "Health check"
```

### 3. Selectores de Kubernetes
Además de regex por nombre, puedes usar selectores de etiquetas, lo cual es mucho más preciso para entornos de producción:

```bash
stern -l app=mi-app -l tier=frontend
```

### 4. Formato de salida
Si tus logs están en JSON (como es buena práctica), Stern puede pasarlos tal cual para que los proceses con herramientas como `jq` o `fx`:

```bash
stern backend -o raw | fx
```

## Conclusión
Stern es una de esas herramientas que instalas el primer día y te preguntas cómo podías vivir sin ella. Hace que el debug en entornos distribuidos sea mucho menos doloroso al agregar la información de manera coherente.

Dale una oportunidad y tus sesiones de debugging te lo agradecerán.

![stern help]({static}/images/stern_help.png)
