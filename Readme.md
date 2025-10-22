Keylogger educativo en Python

Este proyecto es un programa educativo en Python que captura las teclas presionadas por el usuario y las guarda en un archivo de texto llamado registro.txt.
El programa finaliza la captura cuando se presiona la tecla *.

Descripción

El script utiliza la librería keyboard para detectar eventos del teclado.
Cada vez que el usuario presiona una tecla, su valor se agrega a una lista (escrito).
Cuando se presiona *, el programa termina la captura y guarda todo el texto registrado en un archivo de salida.

Funcionamiento paso a paso

Se importa la librería keyboard.

Se crea una lista vacía llamada escrito para almacenar las teclas presionadas.

La función IKWYD(event): //Esto significa "I Know What You Do"

Obtiene el nombre de la tecla presionada (event.name).

Reemplaza enter y space por un espacio " " para que el texto sea legible.

Agrega la tecla a la lista escrito.

keyboard.on_press(IKWYD) inicia la escucha de eventos de teclado.

keyboard.wait("*") mantiene el programa en ejecución hasta que se presiona *.

Al finalizar, se guarda el contenido capturado en registro.txt y se muestra en consola.