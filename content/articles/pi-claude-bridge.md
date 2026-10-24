Title: pi-claude-bridge: la suscripción de Claude Pro, Max o Team dentro de pi
Date: 2026-10-24
Category: Herramientas
Tags: pi, claude, claude-code, coding-agent, suscripciones, cli
Slug: pi-claude-bridge
Lang: es
Summary: pi-claude-bridge conecta pi con el Agent SDK de Claude Code para usar Opus, Sonnet y Haiku de tu suscripción Pro, Max o Team como modelos normales de pi, sin API key y con todas las herramientas pasando por la TUI de pi.
Featured_image: /images/pi-claude-bridge.png

En el trabajo el presupuesto de modelos es una cuenta de **Claude Team**. Y con eso la pregunta es siempre la misma: ¿esta sesión la pago con la suscripción o con una API key aparte? [pi-claude-bridge](https://github.com/elidickinson/pi-claude-bridge) va justo a eso: los modelos de Claude aparecen en `/model` de pi y la conversación consume cuota de suscripción, no tokens facturados.

![Repositorio de pi-claude-bridge](/images/pi-claude-bridge.png)

## Qué es exactamente

Es una extensión de pi que se apoya en el [Agent SDK de Claude Code](https://github.com/anthropics/claude-agent-sdk-typescript). Nació como fork de `claude-agent-sdk-pi` de Prateek Sunal y hace dos cosas:

1. **Provider** — Registra un provider `claude-bridge` con los modelos de Claude del catálogo de `pi-ai`. Todas las llamadas a herramientas pasan por la TUI de pi, así que ves lo mismo que verías con cualquier otro modelo.
2. **Herramienta `AskClaude`** — Permite delegar una pregunta a Claude Code mientras usas otro provider. Está marcada como deprecada.

```bash
pi install npm:pi-claude-bridge
```

Necesita pi 1.2.0 o superior para tener todos los modelos disponibles.

## Uso como provider

```bash
/model claude-bridge/claude-opus-5
```

Y ya está. Detrás, pi traduce sus herramientas al formato de Claude Code, así que el flujo de trabajo no cambia: mismas herramientas, misma sesión, mismos subagentes. Hay unos cuantos detalles que sí cambian y conviene conocer:

- **Bash tiene timeout de 120 segundos**, el que aplica Claude Code por defecto. El bash de pi no tiene timeout propio, así que hereda el del puente.
- **Las skills se reenvían** al system prompt de Claude Code.
- **El steering a mitad de turno** llega a Claude en el siguiente límite de herramienta, no de inmediato.
- **La lista de modelos es la de `pi-ai`**. Cuando `pi-ai` añade un modelo de Claude, aparece en `/model` al actualizar el paquete, sin esperar una release del puente. Los ids con fecha (`claude-opus-4-5-20251101`) no se muestran.

## Login: el puente no tiene login propio

Esto es la causa del primer tropiezo de bastante gente (issue #201 del repo). La extensión no autentica contra Anthropic por su cuenta: lanza el binario `claude` y usa **la sesión que ya tenga Claude Code**. El `/login` de pi para el provider `anthropic` no tiene nada que ver, y si lo usas pensando que el puente lo va a heredar, acabas pagando Extra Usage sin enterarte.

Así que lo primero es comprobar con qué cuenta está logueado `claude`. Dentro de Claude Code:

```text
/status
```

```text
Account:       tu@empresa.com
Organization:  Tu Empresa
Login method:  Claude Team account
```

Si ahí pone `Claude Max account`, `Claude Pro account` o `Claude Team account`, el puente usará esa sesión. Si pone una API key, no.

Y por si acaso: desactiva **Extra Usage** en los ajustes de Claude. Si Claude Code no puede tirar de tu suscripción para una petición, la alternativa es facturarte el excedente, y eso es mejor saberlo antes que después.

## Contexto de 1M

El contexto de un millón de tokens no está disponible igual en todos los planes, y el puente necesita saber el tuyo. Se configura en `~/.pi/agent/claude-bridge.json`:

```json
{
  "provider": {
    "plan": "max",
    "longContextExtraUsage": false
  }
}
```

Con `plan: "pro"` (el valor por defecto) tienes 1M en Fable 5/5.1, Opus 5.5/5/4.8/4.7 y Sonnet 5.5/5. Opus 4.6 solo llega a 1M con plan Max o con Extra Usage, y Sonnet 4.6 solo con Extra Usage. Ojo con el nombre del valor: si tu cuenta es de empresa, el README pide poner igualmente `max`, porque es el que habilita el contexto largo en **Team Premium y Enterprise**. Llamativo, pero así está. Si tu plan declara 1M pero Claude Code no te lo sirve, `forceTwoHundredK` pinea modelos concretos a 200K:

```json
{
  "provider": {
    "plan": "max",
    "forceTwoHundredK": ["claude-opus-4-6"]
  }
}
```

## El resto de la configuración

```json
{
  "provider": {
    "strictMcpConfig": true,
    "autoMemoryEnabled": false,
    "pathToClaudeCodeExecutable": "/home/you/.nix-profile/bin/claude"
  },
  "askClaude": {
    "enabled": false,
    "defaultMode": "read",
    "allowFullMode": true
  }
}
```

`strictMcpConfig` viene activado y bloquea los servidores MCP de `~/.claude.json` y `.mcp.json`. Tiene sentido: si ya tienes MCP en pi, cargar además los de Claude Code duplica herramientas y gasta contexto. El MCP en la nube (Gmail, Drive vía OAuth de claude.ai) está bloqueado siempre.

`pathToClaudeCodeExecutable` es para cuando los binarios que trae el SDK no pueden ejecutarse en tu sistema. En Nix es el caso típico: apuntas al `claude` del perfil.

## Lo que hay que saber antes de usarlo

Esto no es un provider más, y tiene trampas que documenta el propio repo. Las importantes:

**Reconstruir la sesión reenvía toda la conversación.** El puente reescribe la sesión de Claude Code desde el historial de pi cada vez que divergen: después de un abort, de un `/compact`, de navegar por el árbol de la sesión, de un error de API, o al volver a una sesión. La siguiente petición suele fallar la caché de prompt de todo lo que va después del system prompt. En sesiones con muchos aborts, se nota en la factura.

**Los archivos que edita Claude Code no sobreviven a una reconstrucción.** La edición sí, queda en el historial como llamada y resultado de herramienta. Lo que se pierde es el snapshot del archivo después de la edición. Las expansiones `@file` sí se conservan.

**Los cambios de system prompt a mitad de sesión pueden no llegar al modelo.** Claude Code graba el prompt de la primera petición (contexto del proyecto, skills, instrucciones de extensiones) y lo reutiliza al reanudar. Eso mantiene estable el prefijo cacheado, pero si cambias `AGENTS.md` a mitad de sesión, puede que no surta efecto hasta una reconstrucción o una compactación.

**Las variables `ANTHROPIC_*` exportadas secuestran el proceso hijo.** Un `ANTHROPIC_BASE_URL`, `ANTHROPIC_API_KEY` o `ANTHROPIC_AUTH_TOKEN` en el entorno redirige Claude Code a esa pasarela y todos los turnos fallan con su error de autenticación. Si tienes una de esas en tu `.zshrc`, quítala del proceso de pi.

**`modelOverrides` de `models.json` no funciona aquí.** Solo aplican a ajustes del lado de pi, como el umbral de compactación. Para tocar `contextWindow` hay que editar `src/models.ts` o usar `forceTwoHundredK`.

## Detalles que me han sorprendido para bien

**Los hooks de Claude Code siguen funcionando.** `~/.claude/settings.json` se dispara dentro de los turnos del puente. Eso puede ser útil o un desastre: un hook que inyecta guía específica de Claude duplica lo que ya hacen tus extensiones de pi. La salida es la que sugiere el README:

```sh
[ -n "$PI_CODING_AGENT" ] && exit 0
```

pi pone `PI_CODING_AGENT=true` en los procesos hijos, así que el hook se autodescarta cuando corre dentro de pi.

**La compactación la sigue haciendo pi.** El puente enruta esas llamadas a consultas aisladas de Claude Code, sin tocar la sesión viva hasta que pi termina de reescribir el historial.

**El uso del plan se puede leer desde otras extensiones.** Claude Code emite un `rate_limit_event` cuando cambia una ventana de uso, y el puente lo pasa por el evento `after_provider_response` como cabeceras `anthropic-ratelimit-unified-*`, con los mismos nombres que usa la API de Anthropic. Una extensión que ya lea esas cabeceras para el provider `anthropic` nativo puede aceptar `claude-bridge` sin cambios.

**Convivencia con subagentes.** Con `@gotgenes/pi-subagents` hay que añadir esto en `~/.pi/agent/subagents.json`:

```json
{"promptInheritance": {"claude-bridge": "portable"}}
```

## Sobre la facturación

Anthropic anunció y luego desanunció un cambio en cómo se factura el uso del Agent SDK. A día de hoy, esta extensión consume tu cuota de suscripción igual que Claude Code. Hay además un cambio anunciado por el que los planes Max y Team incluyen créditos mensuales de API, y el propio repo no sabe todavía si eso acabará tocando al puente: el consenso en los issues es "de momento igual que siempre".

Es el motivo por el que me interesa en el trabajo y no en casa: donde hay Claude contratado, el puente tiene sentido; donde no, ninguno.

## Mi caso de uso

En la máquina del trabajo tengo una cuenta Claude Team y pi es mi harness. Esto es lo que quiero montar ahí, y conviene decirlo claro: **todavía no lo he probado en esa máquina**. Lo que he verificado es lo que cuento arriba — configuración, cómo funciona por dentro y las trampas que documenta el repo. Cuando lo tenga rodando unos días actualizo esta entrada con el veredicto y con el valor de `plan` con el que me haya quedado.

El planteamiento es el que me interesa: la TUI es la de pi, las herramientas son las de pi, las skills son las de pi, y por debajo el que habla con Anthropic es Claude Code con mi sesión. Nada de API keys sueltas y nada de elegir entre el agente que me gusta y el modelo que ya está pagado.

La pega real, cuando lo pruebe, va a ser la de las sesiones con muchos aborts, que es donde el puente paga el precio de reconstruir el historial.

En casa el planteamiento es el contrario: suscripción de OpenCode Go y [pi-provider-opencode-console](https://pablocaro.es/pi-provider-opencode-console) para tener el catálogo de modelos en vivo.

## Recursos

- [pi-claude-bridge en GitHub](https://github.com/elidickinson/pi-claude-bridge) — Código, configuración y *known issues*
- [En npm](https://www.npmjs.com/package/pi-claude-bridge) — `pi install npm:pi-claude-bridge`
- [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-typescript) — La base sobre la que se apoya
- [claude-agent-sdk-pi](https://github.com/prateekmedia/claude-agent-sdk-pi) — El proyecto del que nació
- [El puente de OpenCode](https://pablocaro.es/pi-provider-opencode-console) — La otra extensión de providers que uso
