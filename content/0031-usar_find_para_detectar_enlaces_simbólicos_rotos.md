Date: 2008-11-20 11:30
Guid: http://www.pablocaro.es/usar-find-para-detectar-enlaces-simbolicos-rotos/
Tags: 
Categories: Linux, Yaco
Title: Usar find para detectar enlaces simbólicos rotos

`for f in $(find /usr/local/bin -type l); do if [ ! -e "$f" ]; then [echo](htt
p://howto.wikia.com/index.php?title=Echo_command&action=edit&redlink=1) $f;
fi; done`

