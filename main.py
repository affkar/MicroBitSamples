def on_button_pressed_a():
    for index in range(4):
        basic.show_icon(IconNames.HAPPY)
        basic.pause(200)
        basic.clear_screen()
        basic.show_icon(IconNames.SILLY)
        basic.pause(200)
        basic.clear_screen()
        basic.show_icon(IconNames.HEART)
        basic.pause(200)
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    images.create_big_image("""
        # . # . # . # . # .
        # # # # # . . . . .
        . # # # . # . . . #
        # . . . # . # # # .
        # # # # # . . . . .
        """).scroll_image(0, 200)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . # . # .
        # . . . #
        # # # # #
        # # # # #
        # # # # #
        """)
    basic.pause(5000)
    basic.clear_screen()
    basic.show_string("HAHA!")
    basic.pause(100)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)
