Date: 2008-11-14 05:04
Category: Programación
Guid: http://www.pablocaro.es/%c2%bfcomo-hacer-un-svn-export-con-git/
Title: ¿Cómo hacer un "svn export" con git?

Si tienes que descargarte un árbol git pero sin los metadatos, porque por
ejemplo sólo quieres el código para congerlarlo versionado en el subversion de
tu proyecto, lo más fácil es: git clone {clone-url} rm -rf .gitignore .git

