Date: 2006-12-15 14:23
Guid: http://www.pablocaro.es/?p=6
Tags: 
Categories: .net
Title: Siempre la coma como símbolo decimal en un formulario .net

Entre los muchos lenguajes que me ha tocado codificar (únicamente no me
arrepiento de hacerlo en [python](http://www.python.org)) se encuentra .net.
Es una chusquería que me solicitó un cliente. Quería que en un formulario al
pulsar el punto del teclado numérico la entrada fuera una coma (no dependiera
de la configuración de los locales en el windows). Puede llegar a ser muy
útil.

    
    
    /**
    * En este formulario el simbolo decimal del teclado numerico siempre la comma
    */
    protected override bool ProcessCmdKey(ref Message msg, Keys keyData)
    {
    if (keyData == Keys.Decimal)
    {
    SendKeys.Send(",");
    return true;
    }
    return base.ProcessCmdKey(ref msg, keyData);
    
    
    }

