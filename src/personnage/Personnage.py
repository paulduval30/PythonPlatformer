import pygame
import pymunk


class Personnage:
    def __init__(self, nom, posX, posY):
        self.nom = nom
        self.posX = posX
        self.posY = posY
        self.mass = 1
        self.size = 50
        self.moment = pymunk.moment_for_box(self.mass, (self.size, self.size))
        self.body = pymunk.Body(self.mass, self.moment)
        self.body.position = posX, posY
        self.shape = pymunk.Poly.create_box(self.body, (self.size,self.size))

    def render(self, fenetre):
        fenetre.blit(self.image, (self.posX, self.posY))