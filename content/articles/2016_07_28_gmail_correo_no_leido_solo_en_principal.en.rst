Unread Mail in Gmail's Primary Tab
####################################

:date: 2016-07-28 18:00
:tags: linux
:lang: en
:category: Tricks
:slug: gmail_correo_no_leido_solo_en_principal

As always, another reminder note.

If you filter mail in gmail by unread (:code:`is:unread`), you get all unread mail,
which in my case always includes hundreds of notifications, social, promotions, or forums which is usually not what I'm looking for.

To search for unread emails *from the Primary tab* the query to perform is this::

	is:inbox -category:(updates OR promotions OR social OR forums) is:unread



