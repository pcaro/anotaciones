Title: Server-Sent Events: Comunicación en tiempo real simplificada
Date: 2024-09-23 00:01
Tags: javascript, sse, tiempo-real, web-apis
Lang: es
Category: Programación
Slug: server-sent-events-comunicacion-tiempo-real
Summary: Server-Sent Events ofrece una alternativa simple y eficiente a WebSockets para comunicación unidireccional servidor-cliente en aplicaciones web

Los **Server-Sent Events (SSE)** representan una solución elegante y simple para implementar comunicación en tiempo real en aplicaciones web cuando solo necesitamos que el servidor envíe datos al cliente.

## ¿Qué son los Server-Sent Events?

SSE es un estándar web que permite que un servidor envíe datos automáticamente a una página web usando una conexión HTTP persistente. A diferencia de WebSockets, la comunicación es **unidireccional**: solo el servidor puede enviar mensajes al cliente.

## Implementación básica

### Cliente (JavaScript)

```javascript
// Crear conexión SSE
const eventSource = new EventSource('/api/events');

// Escuchar mensajes genéricos
eventSource.onmessage = function(event) {
    console.log('Mensaje recibido:', event.data);
    const data = JSON.parse(event.data);
    updateUI(data);
};

// Escuchar eventos personalizados
eventSource.addEventListener('notification', function(event) {
    const notification = JSON.parse(event.data);
    showNotification(notification.title, notification.message);
});

// Manejar errores
eventSource.onerror = function(event) {
    console.error('Error en SSE:', event);
};

// Cerrar conexión
// eventSource.close();
```

### Servidor (Python/Flask)

```python
from flask import Flask, Response
import json
import time
import threading

app = Flask(__name__)

def generate_events():
    """Generador que produce eventos SSE"""
    while True:
        # Evento genérico
        data = {
            'timestamp': time.time(),
            'users_online': get_users_count(),
            'server_status': 'running'
        }
        
        yield f"data: {json.dumps(data)}\n\n"
        
        time.sleep(10)  # Enviar cada 10 segundos

@app.route('/api/events')
def stream_events():
    """Endpoint SSE"""
    return Response(
        generate_events(),
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Access-Control-Allow-Origin': '*'
        }
    )

@app.route('/api/notify')
def send_notification():
    """Enviar notificación específica"""
    def notification_event():
        notification = {
            'title': 'Nueva actualización',
            'message': 'El sistema se actualizó correctamente'
        }
        
        # Evento con nombre personalizado
        yield f"event: notification\n"
        yield f"data: {json.dumps(notification)}\n\n"
    
    return Response(notification_event(), mimetype='text/event-stream')
```

## Formato del stream de eventos

Los eventos SSE siguen un formato específico:

```
event: message-type
data: {"key": "value"}
id: unique-message-id
retry: 3000

```

- **event**: Nombre del evento (opcional)
- **data**: Contenido del mensaje
- **id**: Identificador único para reconexión
- **retry**: Tiempo de reintento en milisegundos

## Casos de uso ideales

### 1. Feeds en tiempo real

```javascript
const newsSource = new EventSource('/api/news-feed');

newsSource.addEventListener('article', function(event) {
    const article = JSON.parse(event.data);
    addArticleToFeed(article);
});
```

### 2. Notificaciones push

```javascript
const notificationSource = new EventSource('/api/notifications');

notificationSource.onmessage = function(event) {
    const notification = JSON.parse(event.data);
    
    // Mostrar notificación del navegador
    if (Notification.permission === 'granted') {
        new Notification(notification.title, {
            body: notification.message,
            icon: '/icon.png'
        });
    }
};
```

### 3. Dashboard en tiempo real

```javascript
const dashboardSource = new EventSource('/api/dashboard');

dashboardSource.addEventListener('metrics', function(event) {
    const metrics = JSON.parse(event.data);
    updateCharts(metrics);
    updateCounters(metrics);
});

dashboardSource.addEventListener('alert', function(event) {
    const alert = JSON.parse(event.data);
    showAlert(alert.level, alert.message);
});
```

## Ventajas de SSE

1. **Simplicidad**: API más simple que WebSockets
2. **Reconexión automática**: El navegador reintenta automáticamente
3. **Eficiencia**: Menor overhead que polling
4. **Compatibilidad**: Funciona sobre HTTP/HTTPS estándar
5. **Firewall-friendly**: No requiere puertos especiales

## Limitaciones importantes

1. **Unidireccional**: Solo servidor → cliente
2. **Límites de conexión**: Navegadores limitan conexiones simultáneas
3. **Formato de datos**: Solo texto (aunque JSON funciona bien)
4. **Sin compresión nativa**: A diferencia de WebSockets

## SSE vs WebSockets: ¿Cuándo usar cada uno?

### Usa SSE cuando:
- Solo necesitas servidor → cliente
- Simplicidad es prioritaria  
- Actualizaciones periódicas (feeds, notificaciones)
- Compatibilidad con proxies/firewalls es importante

### Usa WebSockets cuando:
- Necesitas comunicación bidireccional
- Latencia ultra-baja es crítica
- Intercambio intensivo de datos
- Control total sobre el protocolo

## Manejo de errores y reconexión

```javascript
const eventSource = new EventSource('/api/events');

let reconnectInterval = 1000;
const maxReconnectInterval = 30000;

eventSource.onopen = function() {
    console.log('Conexión SSE establecida');
    reconnectInterval = 1000; // Reset interval
};

eventSource.onerror = function(event) {
    console.error('Error SSE:', event);
    
    if (eventSource.readyState === EventSource.CLOSED) {
        // Reconexión manual con backoff exponencial
        setTimeout(() => {
            console.log('Intentando reconectar...');
            reconnectSSE();
        }, reconnectInterval);
        
        reconnectInterval = Math.min(reconnectInterval * 2, maxReconnectInterval);
    }
};

function reconnectSSE() {
    eventSource.close();
    eventSource = new EventSource('/api/events');
}
```

## Conclusión

Server-Sent Events ofrece una solución pragmática para comunicación en tiempo real cuando WebSockets resulta excesivo. Su simplicidad, reconexión automática y compatibilidad lo convierten en una opción excelente para feeds, notificaciones y dashboards en tiempo real.

Para aplicaciones que requieren actualizaciones del servidor al cliente sin la complejidad de WebSockets, SSE es la herramienta perfecta.

*Documentación oficial*: [Using server-sent events - MDN](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)