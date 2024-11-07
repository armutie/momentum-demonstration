import pygame

pygame.init()
WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.acceleration = 10
        self.activate = True
        self.color = BLACK
        self.radius = 10
        self.time = 0
        self.vel = 20

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def fall(self, keys):
        if self.activate:
            if self.y + self.radius < HEIGHT:
                self.y += 0.5 * self.acceleration * (self.time/60) ** 2
                self.time += 1
            else:
                self.y = HEIGHT - self.radius

    def jump(self, keys):
        if keys[pygame.K_SPACE]:
            self.activate = False
            self.time = 0
        if not self.activate:

            # self.y += 0.5 * self.acceleration * (self.time / 60) ** 2 - self.vel
            # self.time += 1
            # if (0.5 * self.acceleration * (self.time / 60) ** 2) >= self.vel:
            #     self.activate = True
            #     self.time = 0
            # --------------------------------------------------------------------------
            self.y -= self.vel
            self.vel -= 4
            if self.vel <= 0:
                self.activate = True
                self.vel = 20


def redraw_window(win, main_char):
    win.fill(WHITE)
    main_char.draw(win)


spidey = Player(50, 50)


run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    redraw_window(WIN, spidey)
    spidey.fall(keys)
    spidey.jump(keys)
    pygame.display.update()

pygame.quit()
