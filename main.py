def on_button_pressed_a():
    global spieler_x
    spieler_x += richtung
    led.plot(spieler_x, spieler_y)
    if spieler_x == 4:
        spieler_x = 0
        led.plot(spieler_x, spieler_y)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global sprite, spieler_y
    basic.set_led_color(0xff0000)
    basic.clear_screen()
    sprite = 0
    spieler_y = 0
    led.plot(spieler_x, spieler_y)
    basic.set_led_color(0x00ff00)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global richtung
    if richtung == 1:
        richtung = -1
    else:
        richtung = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global spieler_y, spriteY
    spieler_y += richtung
    led.plot(spieler_x, spieler_y)
    if spieler_y == 4:
        spriteY = 0
        led.plot(spieler_x, spieler_y)
input.on_button_pressed(Button.B, on_button_pressed_b)

spriteY = 0
sprite = 0
richtung = 0
spieler_y = 0
spieler_x = 0
basic.set_led_color(0xff0000)
music.play_melody("B A G A G F A C5 ", 200)
spieler_x = 0
spieler_y = 0
richtung = 1
led.plot(spieler_x, spieler_y)
basic.set_led_color(0x00ff00)