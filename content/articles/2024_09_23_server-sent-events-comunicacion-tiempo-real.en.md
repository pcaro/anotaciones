Title: Server-Sent Events: Simplified Real-Time Communication
Date: 2024-09-23 00:01
Tags: javascript, sse, real-time, web-apis
Lang: en
Category: Programming
Slug: server-sent-events-comunicacion-tiempo-real
Summary: Server-Sent Events offer a simple and efficient alternative to WebSockets for unidirectional server-to-client communication in web applications

**Server-Sent Events (SSE)** represent an elegant and simple solution for implementing real-time communication in web applications when we only need the server to send data to the client.

## What are Server-Sent Events?

SSE is a web standard that allows a server to automatically send data to a web page using a persistent HTTP connection. Unlike WebSockets, communication is **unidirectional**: only the server can send messages to the client.

## Basic Implementation

### Client (JavaScript)

```javascript
// Create SSE connection
const eventSource = new EventSource('/api/events');

// Listen for generic messages
eventSource.onmessage = function(event) {
    console.log('Message received:', event.data);
    const data = JSON.parse(event.data);
    updateUI(data);
};

// Listen for custom events
eventSource.addEventListener('notification', function(event) {
    const notification = JSON.parse(event.data);
    showNotification(notification.title, notification.message);
});

// Handle errors
eventSource.onerror = function(event) {
    console.error('SSE Error:', event);
};

// Close connection
// eventSource.close();
```

### Server (Python/Flask)

```python
from flask import Flask, Response
import json
import time
import threading

app = Flask(__name__)

def generate_events():
    """Generator producing SSE events"""
    while True:
        # Generic event
        data = {
            'timestamp': time.time(),
            'users_online': get_users_count(),
            'server_status': 'running'
        }
        
        yield f"data: {json.dumps(data)}\n\n"
        
        time.sleep(10)  # Send every 10 seconds

@app.route('/api/events')
def stream_events():
    """SSE Endpoint"""
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
    """Send specific notification"""
    def notification_event():
        notification = {
            'title': 'New Update',
            'message': 'System updated successfully'
        }
        
        # Event with custom name
        yield f"event: notification\n"
        yield f"data: {json.dumps(notification)}\n\n"
    
    return Response(notification_event(), mimetype='text/event-stream')
```

## Event Stream Format

SSE events follow a specific format:

```
event: message-type
data: {"key": "value"}
id: unique-message-id
retry: 3000

```

- **event**: Event name (optional)
- **data**: Message content
- **id**: Unique identifier for reconnection
- **retry**: Retry time in milliseconds

## Ideal Use Cases

### 1. Real-Time Feeds

```javascript
const newsSource = new EventSource('/api/news-feed');

newsSource.addEventListener('article', function(event) {
    const article = JSON.parse(event.data);
    addArticleToFeed(article);
});
```

### 2. Push Notifications

```javascript
const notificationSource = new EventSource('/api/notifications');

notificationSource.onmessage = function(event) {
    const notification = JSON.parse(event.data);
    
    // Show browser notification
    if (Notification.permission === 'granted') {
        new Notification(notification.title, {
            body: notification.message,
            icon: '/icon.png'
        });
    }
};
```

### 3. Real-Time Dashboard

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

## Advantages of SSE

1. **Simplicity**: Simpler API than WebSockets
2. **Automatic Reconnection**: Browser retries automatically
3. **Efficiency**: Lower overhead than polling
4. **Compatibility**: Works over standard HTTP/HTTPS
5. **Firewall-friendly**: Does not require special ports

## Important Limitations

1. **Unidirectional**: Only server → client
2. **Connection Limits**: Browsers limit simultaneous connections
3. **Data Format**: Text only (though JSON works fine)
4. **No Native Compression**: Unlike WebSockets

## SSE vs WebSockets: When to Use Which?

### Use SSE when:
- You only need server → client
- Simplicity is a priority
- Periodic updates (feeds, notifications)
- Compatibility with proxies/firewalls is important

### Use WebSockets when:
- You need bidirectional communication
- Ultra-low latency is critical
- Intensive data exchange
- Full control over the protocol

## Error Handling and Reconnection

```javascript
const eventSource = new EventSource('/api/events');

let reconnectInterval = 1000;
const maxReconnectInterval = 30000;

eventSource.onopen = function() {
    console.log('SSE connection established');
    reconnectInterval = 1000; // Reset interval
};

eventSource.onerror = function(event) {
    console.error('SSE Error:', event);
    
    if (eventSource.readyState === EventSource.CLOSED) {
        // Manual reconnection with exponential backoff
        setTimeout(() => {
            console.log('Attempting to reconnect...');
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

## Conclusion

Server-Sent Events offers a pragmatic solution for real-time communication when WebSockets is overkill. Its simplicity, automatic reconnection, and compatibility make it an excellent choice for feeds, notifications, and real-time dashboards.

For applications requiring server-to-client updates without the complexity of WebSockets, SSE is the perfect tool.

*Official documentation*: [Using server-sent events - MDN](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)
