import random as random

from Sprites import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = False

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Personnage(self)
        self.all_sprites.add(self.player)
        for plat in PLAT_LIST:
            p = Plateforme(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
            self.last_one = p
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
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

        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top > HEIGHT:
                    plat.kill()

        while len(self.platforms) < 12:
            width = random.randrange(50, 100)
            p = Plateforme(random.randrange(0, WIDTH - width),self.last_one.rect.y - random.randrange(110, 140), width, 20)
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