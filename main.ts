input.onButtonPressed(Button.A, function () {
    spieler_x += richtung
    led.plot(spieler_x, spieler_y)
    if (spieler_x == 4) {
        spieler_x = 0
        led.plot(spieler_x, spieler_y)
    }
})
input.onGesture(Gesture.Shake, function () {
    basic.setLedColor(0xff0000)
    basic.clearScreen()
    spieler_x = 0
    spieler_y = 0
    led.plot(spieler_x, spieler_y)
    basic.setLedColor(0x00ff00)
})
input.onButtonPressed(Button.AB, function () {
    if (richtung == 1) {
        richtung = -1
    } else {
        richtung = 1
    }
})
input.onButtonPressed(Button.B, function () {
    spieler_y += richtung
    led.plot(spieler_x, spieler_y)
    if (spieler_y == 4) {
        spriteY = 0
        led.plot(spieler_x, spieler_y)
    }
})
let spriteY = 0
let richtung = 0
let spieler_y = 0
let spieler_x = 0
basic.setLedColor(0xff0000)
music.playMelody("B A G A G F A C5 ", 344)
spieler_x = 0
spieler_y = 0
richtung = 1
led.plot(spieler_x, spieler_y)
basic.setLedColor(0x00ff00)
