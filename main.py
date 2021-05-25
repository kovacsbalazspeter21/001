basic.show_leds("""
    # . # . #
    # . # . .
    # # # . #
    # . # . #
    # . # . #
    """)
basic.show_string("")
basic.show_string("Ludwig van Beethoven - Für Elise")
while True:
    led.plot(0, 0)
    led.toggle(0, 0)
    led.unplot(0, 0)
music.set_volume(255)
music.play_tone(659, music.beat(BeatFraction.HALF))
music.play_tone(622, music.beat(BeatFraction.HALF))
music.play_tone(659, music.beat(BeatFraction.HALF))
music.play_tone(622, music.beat(BeatFraction.HALF))
music.play_tone(659, music.beat(BeatFraction.HALF))
music.play_tone(494, music.beat(BeatFraction.HALF))
music.play_tone(587, music.beat(BeatFraction.HALF))
music.play_tone(523, music.beat(BeatFraction.HALF))
music.play_tone(440, music.beat(BeatFraction.WHOLE))
music.play_tone(440, music.beat(BeatFraction.HALF))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.play_tone(440, music.beat(BeatFraction.WHOLE))
music.play_tone(523, music.beat(BeatFraction.HALF))
music.play_tone(659, music.beat(BeatFraction.HALF))
music.play_tone(880, music.beat(BeatFraction.HALF))
music.play_tone(988, music.beat(BeatFraction.WHOLE))
music.play_tone(165, music.beat(BeatFraction.HALF))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.play_tone(415, music.beat(BeatFraction.WHOLE))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.play_tone(415, music.beat(BeatFraction.HALF))
music.play_tone(494, music.beat(BeatFraction.HALF))
music.play_tone(523, music.beat(BeatFraction.WHOLE))
music.play_tone(220, music.beat(BeatFraction.HALF))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.play_tone(440, music.beat(BeatFraction.WHOLE))
music.play_tone(330, music.beat(BeatFraction.HALF))
music.play_tone(659, music.beat(BeatFraction.HALF))
music.play_tone(622, music.beat(BeatFraction.HALF))
music.play_tone(659, music.beat(BeatFraction.HALF))
music.play_tone(622, music.beat(BeatFraction.HALF))
music.play_tone(659, music.beat(BeatFraction.HALF))
music.play_tone(494, music.beat(BeatFraction.HALF))
music.play_tone(587, music.beat(BeatFraction.HALF))
music.play_tone(523, music.beat(BeatFraction.HALF))
music.play_tone(440, music.beat(BeatFraction.WHOLE))

def on_forever():
    pass
basic.forever(on_forever)
