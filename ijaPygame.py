import sys
import pygame as pg

tama = ancho, alto = [800, 500]
ventana = pg.display.set_mode(tama)
pg.display.set_caption("Wall-E")

while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.update()