Title: Tailscale Aperture: Gateway de IA sin distribuir API keys
Date: 2026-03-16 10:00
Category: Herramientas
Tags: tailscale, seguridad, ia, api, gateway
Slug: tailscale-aperture-gateway-ia-seguro
Lang: es
featured_image: /images/tailscale-aperture.png
Summary: Aperture de Tailscale centraliza el acceso a LLMs eliminando la necesidad de distribuir API keys a desarrolladores, usando la identidad de Tailscale para autenticación.

Una de las cosas que me quitó el sueño cuando empecé a usar LLMs en el trabajo fue: **¿dónde guardo las API keys?** En repositorios privados, en `.env` files que se me olvidaban gitignorear, en notas del móvil... Un desastre.

Tailscale anunció recientemente [Aperture](https://tailscale.com/docs/features/aperture), un AI gateway que corre dentro de tu tailnet y que elimina completamente ese problema.

## El problema de las API keys distribuidas

Cuando los desarrolladores necesitan acceso a OpenAI, Anthropic, o cualquier otro proveedor de LLM, la práctica habitual ha sido:

1. Crear una API key
2. Compartirla por Slack, email, o pegada en un repo privado
3. Rezar porque no se filtrre
4. Cuando alguien se va, rotar manualmente todas las keys

Esto escama mal. Una organización con 50 desarrolladores puede tener cientos de keys flotando en documentos, scripts de CI/CD, y machines de desarrolladores que ya no están en la empresa.

## Aperture: centralización con identidad real

La solución de Tailscale es elegante: **usar la identidad del tailnet para autenticar, no keys distribuidas**.

Cómo funciona:

1. **Configuras Aperture en tu tailnet** con las API keys de tus proveedores (OpenAI, Anthropic, Google, OpenRouter, etc.)
2. **Los desarrolladores se conectan a Aperture** usando su identidad de Tailscale
3. **Aperture inyecta las credenciales** del proveedor correspondiente y reenvía la petición
4. **Telemetría completa**: tokens usados, costos, sesiones, todo en un dashboard

Los desarrolladores nunca ven las API keys reales. Aperture las mantiene centralizadas y las inyecta server-side.

## Integración con herramientas existentes

Lo bueno es que funciona con las herramientas que ya usas:

-**Claude Code**: Configuras `ANTHROPIC_BASE_URL=http://ai` y listo
- **Codex**: Base URL a Aperture
- **Gemini CLI, Roo Code, Cline**: Similar, cambias la URL base
- **Custom apps**: Funciona con cualquier cliente que use OpenAI-compatible APIs

Desde el punto de vista del cliente, Aperture se ve como el proveedor mismo. Detecta el modelo en el request body y enruta al proveedor correcto.

## pi-ts-aperture: Plugin para Pi

Hay un plugin oficial de Pi para routearte automáticamente a través de Aperture:

```bash
pi install npm:@aliou/pi-ts-aperture
/aperture:setup
```

El asistente te pide:
1. URL de tu Aperture (ej: `ai.your-tailnet.ts.net`)
2. Qué proveedores routear

Guarda la configuración en `~/.pi/agent/extensions/aperture.json` y modifica los providers para usar Aperture como proxy.

## Visibilidad y control

El dashboardde Aperture te da:

- **Tokens por modelo y usuario**: ¿Cuánto gasta cada persona?
- **Sesiones agrupadas**: Una sesión de Claude Code puede tener 50 requests; las ves como una unidad coherente
- **Tool use**: Qué herramientas se están invocando y con qué frecuencia
- **Adopción**: Quién está usando qué, y quién probó una vez y no volvió
- **Export a S3**: Para integrar con tu SIEM habitual

Para equipos de plataforma o seguridad que necesitan auditoria, esto es oro.

## Requisitos

- Un tailnet de Tailscale (fundamental, toda la autenticación depende de la identidad de Tailscale)
- API keys de los proveedores que quieras usar
- El dispositivo que corre Pi debe estar en el tailnet

## En resumen

Si tu organización está adoptando herramientas de IA y no quieres lidiar con API keys circulando por todos lados, Aperture es una solución limpia. Centraliza credenciales, da visibilidad real del uso, y usa la infraestructura de identidad que ya tienes con Tailscale.

Está en alpha todaví a, pero disponible gratuitodurante el periodo de testing. Vale la pena probarlo si ya usas Tailscale.