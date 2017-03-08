from pygame.locals import *
import numpy as np
import pygame

pygame.init()

windowWidth,windowHeight = 800,600

_display_surf = pygame.display.set_mode((windowWidth,windowHeight), pygame.HWSURFACE)
pygame.display.set_caption('Pygame pythonspot.com example')

class Player:
    def __init__(self):
        self.posInic = 1,1
        self.imagen = pygame.image.load("player.png").convert()
        self.imagen = pygame.transform.scale(self.imagen, (18,18))        
        self.rect = pygame.Rect(self.posInic, (20,20))  #tuplas de posicion, tamano
        self.speed = 20

    def moveRight(self):
        self.rect.left += self.speed

    def moveLeft(self):
        self.rect.left -= self.speed

    def moveUp(self):
        self.rect.top -= self.speed

    def moveDown(self):
        self.rect.top += self.speed

    def getPosicion(self):
        return self.rect

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.rect)     

    def pintar(self, ventana):
        ventana.fill((0,0,0), self.rect) 

class Bloque:
    def __init__(self, x,y):         
        self.imagen = pygame.image.load("block.png")
        self.imagen = pygame.transform.scale(self.imagen, (20,20))
        self.rect = pygame.Rect((x, y), (20,20))  #tuplas de posicion, tamano

    def dibujar(self, ventana, rect):
        ventana.blit(self.imagen, rect)  

class Maze:
    def __init__(self):
        self.M = 10 #crear matriz de tamano seteado por usuario
        self.N = 10
        self.maze = (np.random.choice([0, 1], size=(100,), p=[1./3, 2./3]))
        self.listaDeBloques = [] #almacena bloques (paredes)

    def draw(self,display_surf,imagenBloque):
        bx = 1 #no ocupar posicion (0,0) porque ahi aparece el robot :D
        by = 0
        for i in range(0,self.M*self.N -1):
            if self.maze[ bx + (by*self.M) ] == 1:
                bloqueActual = Bloque(bx * 40, by * 40)
                bloqueActual.dibujar(_display_surf, (bx * 40, by * 40))
                # display_surf.blit(imagenBloque,( bx * 40 , by * 40))
                self.listaDeBloques.append(bloqueActual)
            bx = bx + 1
            if bx > self.M-1:
                bx = 0 
                by = by + 1

    def getListaBloques(self):
        return self.listaDeBloques

class App:

    windowWidth = 800
    windowHeight = 600
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.player = Player()
        self.maze = Maze()

    def on_init(self):
        # pygame.init()
        # self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        # pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        # self._image_surf = pygame.image.load("player.png").convert()
        # self._image_surf = pygame.transform.scale(self._image_surf, (18,18))
        # self._block_surf = pygame.image.load("block.png").convert()
        # self._block_surf = pygame.transform.scale(self._block_surf, (20,20))
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass
 
    def on_render(self):
        self.player.dibujar(_display_surf)
        # self._display_surf.fill((0,0,0))
        # self._display_surf.blit(self._image_surf,self.player.getPosicion())
        
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        self.maze.draw(_display_surf, self._block_surf) #dibujar solo una vez el laberinto
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for evento in pygame.event.get(): #pygame.event.pump()
                #keys = pygame.key.get_pressed()
                if evento.type == pygame.KEYDOWN:
                    if (evento.key == pygame.K_RIGHT):
                        self.player.pintar(_display_surf)
                        self.player.moveRight()
 
                    if (evento.key == pygame.K_LEFT):
                        self.player.pintar(_display_surf)
                        self.player.moveLeft()
 
                    if (evento.key == pygame.K_UP):
                        self.player.pintar(_display_surf)
                        self.player.moveUp()
 
                    if (evento.key == pygame.K_DOWN):
                        self.player.pintar(_display_surf)
                        self.player.moveDown()
 
                    if (evento.key == pygame.K_ESCAPE):
                        self._running = False
 
            # self.on_loop()
                self.on_render()
                pygame.display.flip()
        self.on_cleanup()

 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()