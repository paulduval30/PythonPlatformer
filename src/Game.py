import random as random

from Settings import HEIGHT, WIDTH, BLACK
from Sprites import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((set.WIDTH, set.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()

        self.player = Personnage(self)
        self.all_sprites.add(self.player)

        for plat in set.PLAT_LIST:
            p = Plateforme(*plat, self)
            self.all_sprites.add(p)
            self.platforms.add(p)
            self.last_one = p
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(set.FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
        hits = pygame.sprite.spritecollide(self.player, self.powerups, False)
        if hits:
            hits[0].acting = True
        for power in self.powerups:
            power.act(self.player)
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top > HEIGHT:
                    plat.kill()
            for power in self.powerups:
                power.rect.y += abs(self.player.vel.y)
                if power.rect.top > HEIGHT and power.acting == False:
                    power.kill()

        while len(self.platforms) < 12:
            width = random.randrange(50, 100)
            p = Plateforme(random.randrange(0, WIDTH - width),self.last_one.rect.y - random.randrange(90, 110), width, 20, self)
            self.all_sprites.add(p)
            self.platforms.add(p)
            self.last_one = p

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing :
                    self.playing = False
                self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


g = Game()
g.show_start_screen()

while g.running:
    g.new()
    g.show_go_screen()

pygame.quit()