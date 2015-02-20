Date: 2008-09-14 13:50
Category: Programación
Guid: http://www.pablocaro.es/error-con-setuptools-y-subversion-15/
Tags: python
Title: Error con setuptools y subversion 1.5

La actual versión de
[setuptools](http://peak.telecommunity.com/DevCenter/setuptools) no se lleva
bien el subversion 1.5 (también el actual en mi ubuntu). Normalmente
acostumbro a usar [virtualenv](http://pypi.python.org/pypi/virtualenv) y me he
encontrado con el error:

    
    
    NameError: global name 'log' is not defined

Ya está arreglado en el desarrollo de setuptools. Una posible solución es:

    
    
    easy_install setuptools==dev06'

[Aquí temos más información](http://groups.google.com/group/linux.debian.bugs.
dist/browse_thread/thread/b5d23c96e328b178/796fd556351da9ca?lnk=rao).

