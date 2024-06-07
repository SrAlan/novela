define e = Character("Waifu")

# Definir el personaje p (player) con nombre en color rojo
init python:
    player_name = "amigo"  # Nombre por defecto

label start:
    # Inicializamos la escena con el fondo deseado
    scene fondos

    # Mostramos a "waifu" en el centro de la pantalla
    show waifu at center

    # Waifu pregunta el nombre del jugador
    e "¿Cómo te llamas?"
    $ player_name = renpy.input("Escribe tu nombre:")
    $ player_name = player_name.strip()  # Elimina espacios en blanco extra

    # Si el jugador no introduce un nombre, le asignamos uno por defecto
    if player_name == "":
        $ player_name = "amigo"

    # Redefinimos el personaje p con el nombre del jugador y color rojo
    define p = Character("[player_name]", color="#FF0000")

    # Waifu saluda al jugador por su nombre
    e "Hola, [player_name]."

    # Continuamos con la conversación
    e "Si en verdad me amas pon los datos de tu tarjeta aquí."

   

    # Iniciar el temporizador
    $ countdown = 10
    show screen countdown_screen
 # Mostrar la imagen "pantalla" deslizándose desde abajo
    show pantalla:
        ypos 1000
        linear 1.0 ypos 0
    # Llamar a la función de temporizador
    call countdown_timer

    # Mostrar el menú después de que la imagen se haya deslizado completamente
    menu:
        "Guardar el teléfono":
            e "Has guardado el teléfono."
        "Seguir viendo el teléfono":
            e "vete a la mierda"

    return

# Definir la pantalla del temporizador en la parte superior derecha del área de diálogo
screen countdown_screen:
    text "[countdown]" size 75 color "#FFFFFF" align (0.95, 0.05)  # Tamaño del texto 75, color blanco y centrado en la parte superior derecha del área de diálogo

# Función para el temporizador
label countdown_timer:
    while countdown > 0:
        $ countdown -= 1
        $ renpy.pause(1.0)  # Pausa de 1 segundo entre cada decremento

    # Si el temporizador llega a 0, Waifu dice un texto automáticamente
    if countdown == 0:
        hide pantalla
        e "¡si vas a seguir veindo tu telefono me ire otaku asqueroso"

    hide screen countdown_screen
    return
