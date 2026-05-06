Title: Winhance: limpiar y optimizar Windows sin reinstallar
Date: 2026-05-05
Tags: windows, debloater, herramientas, winhance
Slug: winhance-windows-debloater
Lang: es
Featured_image: /images/winhance-windows-debloater.png
Summary: Winhance es una utilidad en C# para debloater, optimizar y personalizar Windows 10/11 sin necesidad de reinstalar el sistema.
Category: Herramientas

![Winhance](/images/winhance-windows-debloater.png)

Llevo usando Linux como sistema principal desde hace años. Tengo dos máquinas con Windows en casa: el portátil de mi hija y un pequeño Mele que uso para conectar al telescopio. No estoy acostumbrado a manejar el ecosistema de Windows, así que cuando toca reinstalar o limpiar una de esas máquinas siempre termino buscando utilidades que hagan el trabajo por mí.

[Winhance](https://github.com/memstechtips/Winhance) es exactamente eso: una herramienta de C# con casi 10.000 estrellas en GitHub que permite debloater, optimizar y personalizar Windows 10 y 11 sin tener que reinstalar. Esencialmente hace lo mismo que [UnattendedWinstall](https://github.com/memstechtips/UnattendedWinstall) pero sin necesidad de una instalación limpia.

La instalación es ridiculamente simple desde PowerShell:

```powershell
irm "https://get.winhance.net" | iex
```

También hay un instalador descargable desde [winhance.net](https://winhance.net) o [GitHub Releases](https://github.com/memstechtips/Winhance/releases), con opción de instalación normal o portable.

Lo que me ha gustado:

- **Software & Apps**: interfaz para quitar bloatware de Windows (apps preinstaladas, capacidades legacy, optional features) e instalar aplicaciones útiles via WinGet. Tiene categorías organizadas para navegadores, multimedia, visores de documentos, etc.

- **Optimize**: todo en un panel searchable. Control del UAC, ajustes de privacidad, optimizaciones para gaming, configuración de Windows Updates, planes de energía, sonido y notificaciones. Cada opción con un toggle switch claro.

- **Customize**: selector de tema oscuro/claro, personalización de la taskbar, menú inicio y el explorador de archivos.

- **Advanced Tools**: herramienta para crear ISOs de Windows personalizadas con WIMUtil (incluyendo drivers del sistema actual) y generar archivos `autounattend.xml` basados en tus selecciones de Winhance.

- **Configuración exportable**: puedes guardar toda tu configuración en un archivo para importarla después de una reinstalación. Esto es oro puro si manejas varias máquinas.

La licencia es [PolyForm Shield 1.0.0](https://polyformproject.org/licenses/shield/1.0.0/), lo que significa que es gratis para uso personal, empresas y profesionales de IT, pero no puedes hacerle fork y redistribuirlo como producto competidor.

Me lo dejo aquí apuntado para la próxima vez que tenga que limpiar una de esas dos máquinas Windows. Seguro me ahorra un buen rato de clicks por el panel de configuración.
