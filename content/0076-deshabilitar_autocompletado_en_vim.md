Date: 2011-06-20 04:42
Guid: http://www.pablocaro.es/?p=295
Title: Deshabilitar autocompletado en vim

Uso poco vim, sólo cuando en servidores no tengo jed. Para pegar texto en el
fichero actual sin que te haga un horrible indentado en cascada:

    
    
    :setlocal noautoindent
    :setlocal nocindent
    :setlocal nosmartindent
    :setlocal indentexpr=

O su equivalente:

    
    
    :setl noai nocin nosi inde=

Referencia: [http://vim.wikia.com/wiki/How_to_stop_auto_indenting
](http://vim.wikia.com/wiki/How_to_stop_auto_indenting)

