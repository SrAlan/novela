# Importaciones (si las hubiera)

# Definición de personajes
define w_timida = Character("Waifu tímida")
define w_gal = Character("Waifu gal")
define w_feliz = Character("Waifu alegre")
define w_feliz_d = Character("Waifu alegre", image="w_feliz_d")  # Nuevo personaje con imagen diferente



# Definir el personaje p (player) con nombre en color rojo
init python:
    player_name = "amigo"  # Nombre por defecto

# Pantalla personalizada para mostrar la imagen "pantalla" sobre el UI
screen pantalla_screen:
    zorder 200  # Asegura que esté por encima de otros elementos de UI
    add "pantalla" at pantalla_move

# Definir la transformación de la imagen "pantalla"
transform pantalla_move:
    ypos 1000
    linear 1.0 ypos 0

# Transformación para la entrada desde la derecha
transform from_right:
    xalign 1.5
    linear 1.0 xalign 0.5

# Pantalla con botones para sacar y ocultar el teléfono
screen phone_buttons:
    zorder 200  # Asegura que los botones estén también por encima de otros elementos
    hbox:
        align (0.05, 0.05)
        spacing 10
        textbutton "Sacar teléfono" action Function(show_phone)
        textbutton "Ocultar teléfono" action Function(hide_phone)

# Función para mostrar el teléfono
init python:
    def show_phone():
        """
        Función para mostrar la pantalla del teléfono.
        """
        renpy.show_screen("pantalla_screen")

# Función para ocultar el teléfono
init python:
    def hide_phone():
        """
        Función para ocultar la pantalla del teléfono.
        """
        renpy.hide_screen("pantalla_screen")

label start:
    # Mostrar los botones del teléfono
    show screen phone_buttons

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

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

init: ### just setting variables in advance so there are no undefined variable problems
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)]) 
        ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve 
        # ^This is the timer bar.

label questiontime1:
    
    label menu1:
        $ time = 3                                     ### set variable time to 3
        $ timer_range = 3                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'menu1_slow'                    ### set where you want to jump once the timer runs out
        show screen countdown                          ### call and start the timer

        menu:
            "con pito":
                play sound click
                hide screen countdown                  ### stop the timer
                jump just
            "sin pito":
                play sound click
                hide screen countdown                  ### stop the timer
                jump just

    label menu1_slow:
        p "Mr. Abramov? Did you fall asleep, by any chance?"
        jump nueva_escena
     
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

    menu:
        "Bien":
            w_feliz "Me alegro."
        "Mal":
            hide w_feliz  # Ocultar la imagen de w_feliz
            show w_feliz_d at left  # Mostrar la imagen de w_feliz_d a la derecha
            w_feliz_d "Oh, mira ese pájaro."
            
            menu:
                "1. Irse al salón seguro":
                    jump nueva_escena
                "2. Quedarse":
                    w_feliz_d "Está bien, como quieras."

    return

label nueva_escena:
    scene co_lugar01
    p "Ahora estoy aquí."
    "aqui ira una cinematica"
    # Agrega más código aquí para la nueva escena

    # Regresar al menú principal
    return