Date: 2008-09-11 16:24
Guid: http://www.pablocaro.es/editores-mostrar-los-numeros-de-linea-en-emacs-y-en-jed/
Title: Editores: Mostrar los números de linea en emacs y en jed

Para evitar esos odiosos porcentajes cuandos editas un fichero (¿de verdad le
sirven a alguien?) y poner en su lugar el número de la linea en que te
encuentras dejo aquí la anotación.

  1. En emacs:
    
        ;; ========== Enable Line and Column Numbering ==========
    ;; Show line-number in the mode line
    (line-number-mode 1)
    ;; Show column-number in the mode line
    (column-number-mode 1)

  2. En jed:
    
        LINENUMBERS = 2

