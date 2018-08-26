Este script de python 2.7 está preparado para exportar partidas de la comunidad umbría y descargarlas en un directorio para su lectura sin necesidad de conectarse a la comunidad. Los usos son mútiples desde backup para los paranoides, lectura para los nostálgicos o para esos másters que quieren reutilizar materiales o se quieren marchar.

El script es feo, poco "pythonico" y puede que no sea muy amable para los no iniciados pero es una versión inicial, ah, tampoco es rápido así que tendrás que esperar al menos unos 2 o 3 minutos a que acabe pero él se encarga de todo.

Requisitos:
Python 2.7
Tener instalado pip

descargar los paquetes BeautifulSoup y mechanize. (pip install BeautifulSoup, pip install mechanize)

Resultado:
Se generará en la carpeta destino (especificada en el script), un html por cada escena de la partida.

Parámetros a informar:
usuario y contraseña. Solo se utilizan para entrar en umbría, no voy a robar vuestros secretos ;)
slug de la partida: El slug es la cadena que hay justo después de www.comunidad.umbria/partida/[ESTO_ES_EL_SLUG]
ubicacion: Directorio del disco duro donde quieras guardarlo

Estado del monstruito:
El monstruito se ha programado en linux y se lanza desde una terminal mediante python descargar.py. Supongo que funcionará igual de bien en MacOS y no se ha probado en windows.

No se permite el carácter "/" como parte del nombre de una escena
No se exportan las fichas de los personajes

