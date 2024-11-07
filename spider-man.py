import pygame
import math

pygame.init()
WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
G = 10


class Rope:
    def __init__(self, pos1, length):
        self.pos1 = pos1
        self.length = length
        self.end_x = pos1[0]
        self.end_y = pos1[1] + length
        self.angle = 0
        self.vel = 0

    def draw(self, win):
        pygame.draw.line(win, BLACK, self.pos1, (self.end_x, self.end_y), 2)

    def physics(self, time):
        ang_vel = math.sqrt(2*G*100)/self.length
        self.end_x = 150 * math.sin(ang_vel * time/60) + self.pos1[0]
        self.vel = 150 * ang_vel * math.cos(ang_vel * time/60)
        self.end_y = math.sqrt(self.length**2 - (self.end_x - self.pos1[0])**2)

        self.angle = abs(math.asin((self.end_x - self.pos1[0]) / self.length))
        vel_x = self.vel * math.cos(self.angle)
        vel_y = abs(self.vel) * math.sin(self.angle) #((-150*ang_vel**2) * math.sin(2*ang_vel*time)) / (2*math.sqrt(self.length**2 - (150**2)*(math.sin(ang_vel*time))**2 ))
        return vel_x, vel_y

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.time = 0

    def draw(self, win):
        pygame.draw.circle(win, BLACK, (self.x, self.y), self.radius)

    def attach(self, rope):
        self.x = rope.end_x
        self.y = rope.end_y

    def fall(self, velx, vely):
        fall_vel = -G*(self.time/60) + vely
        self.y -= fall_vel
        self.x += velx
        self.time += 1

        if self.y >= HEIGHT:
            self.y = HEIGHT - self.radius


def redraw_window(win, rope, da_ball):
    win.fill(WHITE)
    rope.draw(win)
    da_ball.draw(win)
    pygame.draw.line(win, BLACK, (da_ball.x, da_ball.y), (da_ball.x + vx, da_ball.y), 10)


the_rope = Rope((500, 10), 200)
spidey = Ball(500, 200, 10)
vx, vy = 0, 0
current_time = 0

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        spidey.attach(the_rope)
        vx, vy = the_rope.physics(pygame.time.get_ticks())
        current_time += 1
        spidey.time = 0
    else:
        spidey.fall(vx, vy)
        # print(f"{vx}   {vy}")

    redraw_window(WIN, the_rope, spidey)

    pygame.display.update()
    # print(current_time)

pygame.quit()
