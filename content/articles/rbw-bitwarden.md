Title: rbw: El cliente de Bitwarden para terminal que deberías usar
Date: 2026-02-26 11:45
Category: Herramientas
Tags: bitwarden, cli, rust, seguridad, pi-agent
Slug: rbw-bitwarden-cli
Lang: es
Summary: Cómo instalar y configurar rbw, una implementación en Rust del cliente de Bitwarden, y cómo integrarlo en tus flujos de trabajo con pi-agent.

Aunque Bitwarden tiene un cliente oficial de línea de comandos, este puede resultar lento al estar basado en Node.js. Para los que buscamos algo más ágil, [rbw](https://github.com/doy/rbw) es la solución ideal. Es una implementación no oficial en Rust que destaca por ser extremadamente rápida y por gestionar el desbloqueo del almacén mediante un agente, evitando que tengas que introducir tu contraseña maestra en cada comando.

## Instalación

La forma más sencilla de instalarlo es bajando el binario directamente desde sus releases de GitHub. Yo utilizo `gah` para este propósito:

```bash
gah install doy/rbw
```

Este comando descargará el binario de `rbw` y el de `rbw-agent`.

## Configuración inicial

Lo primero es configurar tu cuenta y el servidor:

```bash
rbw login
```

Te pedirá tu email y la URL del servidor (puedes dejarla en blanco si usas el oficial de Bitwarden o poner la de tu instancia de Vaultwarden).

Para empezar a usarlo, desbloquea el almacén:

```bash
rbw unlock
```

A diferencia del cliente oficial, no necesitas exportar variables de entorno con tokens de sesión. El agente de `rbw` se encarga de todo en segundo plano.

## Uso básico

Para obtener una contraseña rápidamente:

```bash
rbw get "Nombre del Elemento"
```

Si hay varios elementos con el mismo nombre, puedes usar filtros o el ID. También puedes obtener campos personalizados o el nombre de usuario:

```bash
rbw get "OpenRouter" --folder "APIs"
rbw get --username "Twitter"
```

## Integración con pi-agent

Una de las mayores ventajas de tener un cliente CLI rápido y seguro es la capacidad de integrar secretos en tus herramientas de desarrollo.

[pi-agent](https://github.com/mariozechner/pi-agent) permite ejecutar comandos para obtener claves de API dinámicamente. Esto evita tener que guardar claves en archivos de configuración en texto plano. En tu `settings.json`, puedes configurar el acceso a una clave de la siguiente manera:

```json
{ 
    "type": "api_key", 
    "key": "!rbw get 'OpenRouter'" 
}
```

El prefijo `!` indica a `pi-agent` que debe ejecutar el comando y usar su salida estándar como la clave. Gracias al agente de `rbw`, este comando se ejecutará instantáneamente sin pedirte la clave maestra cada vez, siempre que el almacén esté desbloqueado.
