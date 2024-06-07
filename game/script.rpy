define e = Character("Waifu")

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

    # Iniciar el temporizador y mostrar la pantalla "pantalla" deslizándose desde abajo sobre el UI
    $ countdown = 10
    show screen countdown_screen
    show screen pantalla_screen

    # Llamar a la función de temporizador
    call countdown_timer

    # Mostrar el menú de preguntas
    menu:
        "Guardar el teléfono":
            e "Has guardado el teléfono."
        "Seguir viendo el teléfono":
            e "¡Vete a la mierda!"

    return

# Función para el temporizador
label countdown_timer:
    while countdown > 0:
        $ countdown -= 1
        $ renpy.pause(1.0)  # Pausa de 1 segundo entre cada decremento

    # Si el temporizador llega a 0, Waifu dice un texto automáticamente
    if countdown == 0:
        hide screen pantalla_screen
        e "¡Si vas a seguir viendo tu teléfono, me iré, otaku asqueroso!"

    hide screen countdown_screen
    return
