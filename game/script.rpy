define w_timida = Character("Waifu tímida")
define w_gal = Character("Waifu gal")
define w_feliz = Character("Waifu alegre")

# Definir el personaje p (player) con nombre en color rojo
init python:
    player_name = "amigo"  # Nombre por defecto

# Definir la pantalla del temporizador en la parte superior derecha del área de diálogo
screen countdown_screen:
    text "[countdown]" size 75 color "#FFFFFF" align (0.95, 0.05)  # Tamaño del texto 75, color blanco y centrado en la parte superior derecha del área de diálogo

# Pantalla personalizada para mostrar la imagen "pantalla" sobre el UI
screen pantalla_screen:
    zorder 100  # Asegura que esté por encima de otros elementos de UI
    add "pantalla" at pantalla_move

# Definir la transformación de la imagen "pantalla"
transform pantalla_move:
    ypos 1000
    linear 1.0 ypos 0

# Transformación para la entrada desde la derecha
transform from_right:
    xalign 1.5
    linear 1.0 xalign 0.5

label start:
    # Escena 1: w_timida en co_entrada
    scene co_entrada
    show w_timida at from_right
    w_timida "Hola, ¿Cómo te llamas?"
    $ player_name = renpy.input("Escribe tu nombre:")
    $ player_name = player_name.strip()  # Elimina espacios en blanco extra

    if player_name == "":
        $ player_name = "amigo"

    define p = Character("[player_name]", color="#FF0000")

    w_timida "Hola, [player_name]."
    
    menu:
        "¡Buenos días!":
            w_timida "jeje"
        "Qué linda estás hoy":
            w_timida "jeje"

    # Transición suave a la escena 2
    scene co_casillas01 with dissolve
    show w_gal at from_right
    w_gal "¡Llegaste temprano!"

    menu:
        "¡Sí! Me caí de la cama":
            w_gal "jeje"
        "Lo raro es que tú llegues temprano, ¿no?":
            w_gal "jeje"

    # Transición suave a la escena 3
    scene co_salon01 with dissolve
    show w_feliz at from_right
    w_feliz "¿Cómo estás?"

    # Iniciar el temporizador y mostrar la pantalla "pantalla" deslizándose desde abajo sobre el UI
    $ countdown = 10
    show screen countdown_screen
    show screen pantalla_screen

    # Llamar a la función de temporizador
    call countdown_timer

    # Mostrar el menú de preguntas
    menu:
        "Guardar el teléfono":
            w_feliz "Has guardado el teléfono."
        "Seguir viendo el teléfono":
            w_feliz "¡Vete a la mierda!"

    return

# Función para el temporizador
label countdown_timer:
    while countdown > 0:
        $ countdown -= 1
        $ renpy.pause(1.0)  # Pausa de 1 segundo entre cada decremento

    if countdown == 0:
        hide screen pantalla_screen
        w_feliz "¡Si vas a seguir viendo tu teléfono, me iré, otaku asqueroso!"

    hide screen countdown_screen
    return
