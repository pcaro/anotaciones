Correo no leído en pestaña principal de gmail
#############################################

:date: 2016-07-28 18:00
:tags: linux
:lang: es
:category: Trucos
:slug: gmail_correo_no_leido_solo_en_principal

Lo de siempre, otra nota recordatoria.

Si filtras el correo en gmail por no leído (:code:`is:unread`), obtienes todo el correo no leído,
que en mi caso siempre incluye cientos de notificaciones, social, promociones o foros que no suele ser lo que busco.

Para buscar los correos no leídos *de la pestaña Principal* la consulta a realizar es esta::

	is:inbox -category:(updates OR promotions OR social OR forums) is:unread



