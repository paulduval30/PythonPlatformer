import sys, random
import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
from pygame.color import *
from pymunk import Vec2d

from World.Ball import Ball
from World.Plateforme import Plateforme
from GraphicsUtil.Camera import Camera
from personnage.Personnage import Personnage


def add_plateforme(space, plateformes, plateforme):
    space.add(plateforme.segment)
    plateformes.append(plateforme)


def add_ball(space, ball, balls):
    space.add(ball.shape, ball.body)
    balls.append(ball)


def draw_ball(screen, ball):
    w, h = pygame.display.get_surface().get_size()
    pygame.draw.circle(screen, pygame.color.THECOLORS["blue"], (int(ball.body.position[0]), int(h - ball.body.position[1])), ball.rayon)


def draw_personnage(screen, personnage):
    w, h = pygame.display.get_surface().get_size()
    x = int(personnage.body.position[0])
    y = int(personnage.body.position[1])
    print(x, y)
    points = [(x, h - y), (x + personnage.size, h - y), (x + personnage.size, h - (y + personnage.size)), (x, h - (y + personnage.size))]
    pygame.draw.polygon(screen, pygame.color.THECOLORS["black"], points)


def draw_plateforme(screen, plateforme):
    w, h = pygame.display.get_surface().get_size()
    points = [(plateforme.x1, h - plateforme.y1), (plateforme.x1 + plateforme.width, h - plateforme.y1),
              ((plateforme.x1 + plateforme.width), h - (plateforme.y1 + plateforme.height)),
              (plateforme.x1, h - (plateforme.y1 + plateforme.height))]
    pygame.draw.polygon(screen, pygame.color.THECOLORS["red"], points)


def main():
    pygame.init()
    camera = Camera(250, 400)
    pygame.key.set_repeat(400,30)
    space = pymunk.Space()
    space.gravity = 0, -900
    screen = pygame.display.set_mode((600, 600), RESIZABLE)
    plateformes = []
    balls = []

    add_plateforme(space, plateformes, Plateforme(0, 40, 100000, 20,space, 1))
    #add_ball(space, Ball(250, 400, 60, 20, 1), balls)
    #add_ball(space, Ball(350, 400, 1, 20, 1), balls)

    personnage = Personnage("", 250.0, 600.0)
    space.add(personnage.body, personnage.shape)
    JUMP_FORCE = 500
    jeu_en_cour = 1
    while jeu_en_cour:
        for event in pygame.event.get():
            if event.type == QUIT:
                jeu_en_cour = 0
            if event.type == KEYDOWN and event.key == K_SPACE:
                print("jump")
                balls[0].body.apply_impulse_at_local_point((0, JUMP_FORCE))
                JUMP_FORCE -= 1
                print(JUMP_FORCE)

        screen.fill((255, 255, 255))
        for plateforme in plateformes:
            draw_plateforme(screen, plateforme)
        for ball in balls:
            draw_ball(screen, ball)
            if int(ball.body.position[1]) < 0:
                space.remove(ball.shape, ball.body)
                balls.remove(ball)
        draw_personnage(screen, personnage)
        space.step(1/60)

        pygame.display.flip()
        pygame.time.Clock().tick(60)


if __name__ == '__main__':
    main()
