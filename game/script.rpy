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
    e "adios"

    # Pregunta al jugador que desea preguntar
    e "Ahora puedes hacerme una pregunta."
    menu:
        "¿Eres mujer?":
            p "¿Eres mujer?"
            e "No xd"
        "¿Eres una IA?":
            p "¿Eres una IA?"
            # Movimiento rápido y parpadeo
            show waifu at center:
                linear 0.1 xalign 0.8
                linear 0.1 xalign 0.2
                linear 0.1 xalign 0.8
                linear 0.1 xalign 0.2
                linear 0.1 xalign 0.8
                linear 0.1 xalign 0.2
            show waifu g with dissolve
            hide waifu g with dissolve
            show waifu with dissolve
            hide waifu with dissolve
            show waifu g with dissolve
            e "Sí, soy una IA."

    return
