from pgzero.actor import Actor
from pgzero.clock import clock
from random import randint
import pgzrun
 
TITLE  = "Coplisci l'alieno!"
WIDTH  = 1200
HEIGHT = 1000
 
messaggio = "Benvenuti!"
colpi     = 0
vite      = 3
game_over = False           
alieno    = Actor("alieno")
 
def draw():
    screen.clear()
    screen.fill((128, 0, 0))
    alieno.draw()
    screen.draw.text(messaggio, center=(400, 40), fontsize=60)
    screen.draw.text(f"Colpi: {colpi}", topleft=(30, 20), fontsize=40)
    screen.draw.text(f"Vite: {vite}",  topright=(WIDTH-30, 20), fontsize=40)
 
    if game_over:
        screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), fontsize=120, color="yellow")
 
def piazza_alieno():
    alieno.x = randint(50, WIDTH-50)
    alieno.y = randint(50, HEIGHT-50)
    alieno.image = "alieno"
 
def on_mouse_down(pos):
    global messaggio, colpi, vite, game_over
    if game_over:          

        return
 
    if alieno.collidepoint(pos):
        messaggio = "Bel colpo!"
        alieno.image = "esplosione"

        colpi += 1

    else:

        messaggio = "Mancato..."

        vite -= 1

        if vite == 0:

            game_over = True

            clock.schedule_unique(ricomincia, 5.0)   # 5 s e si ricomincia
 
def ricomincia():

    global colpi, vite, game_over, messaggio

    colpi     = 0

    vite      = 3

    game_over = False

    messaggio = "Benvenuti!"

    piazza_alieno()
 
piazza_alieno()

clock.schedule_interval(piazza_alieno, 1.0)

pgzrun.go()
 