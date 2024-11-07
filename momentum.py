import pygame
from sympy import symbols, Eq, solve

mass_ask = int(input("Mass of Object 1: "))
vel = int(input("Velocity of Object 1: "))
mass2 = int(input("Mass of Object 2: "))
vel2 = int(input("Velocity of Object 2: "))
ask_friction = input("Do you want friction - Yes or No?: ")

pygame.init()
WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

DAFONT = pygame.font.SysFont('comicsans', 20)
second_font = pygame.font.SysFont('comicsans', 20)



class Object:
    def __init__(self, x, y, width, height, mass, velocity):
        self.x = x
        self.y = y
        self.mass = mass
        self.velocity = velocity
        self.width = width
        self.height = height
        self.mass = mass
        self.velocity = velocity

    def border_collide(self):
        if self.x + self.width >= WIDTH or self.x <= 0:
            self.velocity *= -1

    def draw(self):
        pygame.draw.rect(WIN, RED, (self.x, self.y, self.width, self.height))


def collide(first, other):
    if other.x <= first.x + first.width <= other.x + other.width:
        initial_p = first.mass * first.velocity + other.mass * other.velocity
        x, y = symbols('x y')
        eq1 = Eq(initial_p - first.mass * x - other.mass * y, 0)
        initial_ke = 0.5 * first.mass * first.velocity ** 2 + 0.5 * other.mass * other.velocity ** 2
        eq2 = Eq(initial_ke - 0.5 * first.mass * x ** 2 - 0.5 * other.mass * y ** 2, 0)
        sol_dict = solve((eq1, eq2), (x, y))
        first.velocity = sol_dict[0][0]
        other.velocity = sol_dict[0][1]


def friction(rect): # its just a case of learning
    mew = 0.1
    normal = rect.mass * 9.8
    force = mew * normal
    acceleration = force / rect.mass
    if rect.velocity > 0:
        rect.velocity -= acceleration / 60
        if rect.velocity < 0:
            rect.velocity = 0
    elif rect.velocity < 0:
        rect.velocity += acceleration / 60
        if rect.velocity > 0:
            rect.velocity = 0


def redraw_window():
    WIN.fill(WHITE)
    pygame.draw.line(WIN, BLACK, (0, 450), (800, 450))
    rect1.draw()
    rect2.draw()
    text = DAFONT.render(f"Velocity of Object 1: {rect1.velocity}", 1, BLACK)
    text2 = second_font.render(f"Velocity of Object 2: {rect2.velocity}", 1, BLACK)

    WIN.blit(text, (10, 30))
    WIN.blit(text2, (10, 50))


rect1 = Object(50, 450 - mass_ask*10, mass_ask*10, mass_ask*10, mass_ask, vel)
rect2 = Object(700, 450 - mass2*10, mass2*10, mass2*10, mass2, vel2)

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    rect1.x += rect1.velocity
    rect2.x += rect2.velocity
    collide(rect1, rect2)
    rect1.border_collide()
    rect2.border_collide()
    if ask_friction.lower() == 'yes':
        friction(rect1)
        friction(rect2)
    redraw_window()

    pygame.display.update()

