"""File with all constants"""
import arcade
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
OFFSCREEN_SPACE = 300
SCREEN_TITLE = 'flappybird'

CHARACTER_SCALING = 0.8
PIPE_SCALING = 1
PIPE_SPEED = 2.5
COIN_SCALING = 0.5
GRAVITY = 1

BIRD_MOVEMENT_SPEED = 5
PIPE_GAP = 200
BIRD_X = 160
BIRD_Y= 350
MIN_HEIGHT = 80
MAX_HEIGHT = SCREEN_HEIGHT-100

SOUNDS = {
    "coin": arcade.load_sound(':resources:sounds/coin5.wav'),
    "hit":arcade.load_sound(':resources:sounds/hurt2.wav'),
    "game over":arcade.load_sound(':resources:sounds/gameover3.wav')
}


RULES = ['Aby skoczyć kliknij spację.', 'Za każdą pokonaną przeszkodę dostajesz punkt.',
        'Za każdą zebraną monetę też otrzymujesz punkt.','Co 10 przeszkód poruszasz się coraz szybciej.',
        'Masz 3 życia.']