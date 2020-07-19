input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 4; index++) {
        basic.showIcon(IconNames.Happy)
        basic.pause(200)
        basic.clearScreen()
        basic.showIcon(IconNames.Silly)
        basic.pause(200)
        basic.clearScreen()
        basic.showIcon(IconNames.Heart)
        basic.pause(200)
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.AB, function () {
    radio.setGroup(1)
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . # . # .
        # . . . #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.pause(5000)
    basic.clearScreen()
    basic.showString("HAHA!")
    basic.pause(100)
    basic.clearScreen()
})
