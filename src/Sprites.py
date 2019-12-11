import random as random
import pygame
import Settings as set

vec = pygame.math.Vector2


class Personnage(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../res/perso.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (set.PLAYER_SIZE, set.PLAYER_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = (set.WIDTH / 2, set.HEIGHT / 2)
        self.vx = 0
        self.vy = 0
        self.pos = vec(set.WIDTH / 2, set.HEIGHT / 2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.state = "jump"

    def jump(self):
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = set.PLAYER_JUMP

    def update(self):
        self.acc = vec(0, set.PLAYER_GRAV)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.acc.x = set.PLAYER_ACC
        if keys[pygame.K_LEFT]:
            self.acc.x = -set.PLAYER_ACC
        if keys[pygame.K_SPACE]:
            self.jump()
        if self.pos.x < 0:
            self.pos.x = set.WIDTH
        if self.pos.x > set.WIDTH:
            self.pos.x = 0
        self.acc.x -= self.vel.x * set.PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos

        if self.pos.y > set.HEIGHT:
            self.game.playing = False


class Plateforme(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, game):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../res/plateforme.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        power = random.randrange(0, 100)
        if power < 10:
            type = random.randrange(1, 3)
            print(type)
            # if type == 1:
            #     powerup = Spring(x, y - height)
            # elif type == 2:
            #     powerup = RocketBoots(x, y - height)
            # elif type == 3:
            powerup = SlimeBoots(x, y -  height)
            print(powerup)
            game.powerups.add(powerup)
            game.all_sprites.add(powerup)


class Powerup(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.acting = False
        self.image = pygame.Surface((30, 30))
        self.image.fill(set.GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - self.rect.height / 2

    def act(self, player):
        pass


class Spring(Powerup):
    def __init__(self, x, y):
        Powerup.__init__(self, x, y)
        self.time = 0
        self.timeLimit = 10
        self.image = pygame.image.load("../res/spring.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - self.rect.height / 2

    def act(self, player: Personnage):
        if not self.acting:
            return
        if self.time > self.timeLimit:
            self.acting = False
            self.kill()
            return
        player.vel.y = -30
        self.time += 1


class RocketBoots(Powerup):
    def __init__(self, x, y):
        Powerup.__init__(self, x, y)
        self.time = 0
        self.timeLimit = 100
        self.image = pygame.image.load("../res/RocketBoots/rocketBoots1.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 100

    def act(self, player: Personnage):
        if not self.acting:
            return
        if self.time > self.timeLimit:
            print(self.time)
            self.acting = False
            self.kill()
            return
        self.image = pygame.transform.scale(pygame.image.load("../res/RocketBoots/rocketBoots" +
                                                              str((int((self.time/5) % 10)) + 1) + ".png"), (
                                                set.PLAYER_SIZE, set.PLAYER_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = player.pos.x - self.image.get_width() / 2, player.pos.y - self.image.get_height() - \
                                   self.image.get_height() / 2
        player.vel.y = -30
        self.time += 1


class SlimeBoots(Powerup):
    def __init__(self, x, y):
        Powerup.__init__(self, x, y)
        self.time = 0
        self.timeLimit = 300
        # self.image = pygame.image.load("../res/RocketBoots/rocketBoots1.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - 100

    def act(self, player: Personnage):
        if not self.acting:
            return
        if self.time > self.timeLimit:
            print(self.time)
            self.acting = False
            self.kill()
            set.PLAYER_JUMP = -20
            return
        self.image = pygame.transform.scale(pygame.image.load("../res/RocketBoots/rocketBoots" +
                                                              str((int((self.time / 5) % 10)) + 1) + ".png"),
                                            (set.PLAYER_SIZE, set.PLAYER_SIZE))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = player.pos.x - self.image.get_width() / 2, player.pos.y - self.image.get_height() - \
                                   self.image.get_height() / 2
        set.PLAYER_JUMP = -30
        self.time += 1

