
Este script de python 3 está preparado para exportar partidas de la comunidad umbría y descargarlas en un directorio para su lectura sin necesidad de conectarse a la comunidad. Los usos son mútiples desde backup para los paranoides, lectura para los nostálgicos o para esos másters que quieren reutilizar materiales o se quieren marchar.

El script es feo, poco "pythonico" y puede que no sea muy amable para los no iniciados pero es una versión inicial, ah, tampoco es rápido así que tendrás que esperar al menos unos 2 o 3 minutos a que acabe pero él se encarga de todo.

Requisitos: 

Python 3, BeautifulSoup4

Si tienes instalado pip puedes usar:

pip install mechanize

Dependencias opcionales: PyQt5. Si esta instalado funcionará en una ventana en otro caso en modo texto

Modo de funcionamiento:
Descargar el script y ejecutar python3 descarga.py

El script solicitará los siguientes parámetros:
Usuario de umbria y contraseña:  Solo se utilizan para entrar en umbría, no voy a robar vuestros secretos ;)
Slug de la partida a descargar:  El slug es la cadena que hay justo después de www.comunidad.umbria/partida/[ESTO_ES_EL_SLUG] y suele ser el nombre de la partida con guiones (-) sustituyendo los espacios
Directorio donde guardar la partida en el disco duro: Por ejemplo /home/usuario/umbria/ (el directorio debe existir con anterioridad)

Resultado: 
Se generará en la carpeta destino (especificada en el script), un html por cada escena de la partida y un fichero portada.html. Por otro lado, se crearan carpetas que contienen los estilos y recursos de la página.


Estado del monstruito: 
El monstruito se ha programado en linux y se lanza desde una terminal mediante python descargar.py. Supongo que funcionará igual de bien en MacOS, no probado, y no se ha probado en windows.

No se permite el carácter "/" como parte del nombre de una escena y no se exportan las fichas de los personajes

Que queda por hacer:
descargar las fichas de los personajes
control de excepciones y errores varios, que los usuarios somos muy cenutrios a veces ;)
Que funcione pawa windows
Poner una interfaz gráfica para no tener que preocuparse de toda "la parte técnica"
