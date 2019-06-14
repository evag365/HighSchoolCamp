import pygame

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (222,184,135)
HAIR = (87, 45, 9)
PINK = (255,182,193)
LIPS= (205,92,92)
PI = 3.141592653

# Set the height and width of the screen
size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Shape Set Up")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

ball_pos = 0
ball_change = 1
def draw_stick_figure(screen, x, y):
    pygame.draw.ellipse(screen, RED, [65 + x, 185 + ball_pos + y, 40, 40])
    pygame.draw.circle(screen, HAIR, [200 + x, 80 + y], 70)
    pygame.draw.circle(screen, HAIR, [280 + x , 80 + y], 20)
    pygame.draw.circle(screen, HAIR, [290 + x, 105 + y], 15)
    pygame.draw.circle(screen, HAIR, [295 + x, 125 + y], 13)
    pygame.draw.circle(screen, PINK, [295 + x, 138 + y], 7)
    pygame.draw.circle(screen, PINK, [304 + x, 137 + y], 7)
    pygame.draw.circle(screen, HAIR, [305 + x, 151 + y], 10)
    #Second piece of hair

    pygame.draw.circle(screen, HAIR, [120 + x, 80 + y], 20)
    pygame.draw.circle(screen, HAIR, [105 + x, 105 + y], 15)
    pygame.draw.circle(screen, HAIR, [98 + x, 128 + y], 13)
    pygame.draw.circle(screen, PINK, [103 + x, 137 + y], 7)
    pygame.draw.circle(screen, PINK, [92 + x, 138 + y], 7)
    pygame.draw.circle(screen, HAIR, [92 + x, 151 + y], 10)
    #circlefor face
    pygame.draw.circle(screen, BROWN, [200 + x, 100 + y], 60)
    pygame.draw.arc(screen, LIPS, [175 + x, 90 + y, 50, 45], PI, 0, 5)
    # Draw on the screen a green line from (0,0) to (50, 30)# 5 pixels wide.
    pygame.draw.line(screen, BROWN, [200 + x,101 + y], [200 + x, 300 + y], 5)
    # Draw on the screen a green line from (0,0) to (50, 30)# 5 pixels wide.
    pygame.draw.line(screen, BROWN, [200 + x, 300 + y], [150 + x, 350 + y], 5)
    # RIGHT LEG
    pygame.draw.line(screen, BROWN, [200 + x, 300 + y], [250 + x, 350 + y], 5)
    # ARM LEFT
    pygame.draw.line(screen, BROWN, [200 + x, 200 + y], [95 + x, 180 + y], 5)
    # ARM RIGHT
    pygame.draw.line(screen, BROWN, [200 + x, 201 + y], [295 + x, 180+ y], 5)
    pygame.draw.circle(screen, BLACK, [228 + x, 82 + y], 6)
    pygame.draw.circle(screen, BLACK, [172 + x, 82 + y], 6)
    pygame.draw.polygon(screen, PINK, [[200 + x, 162 + y], [270 + x, 315 + y], [120 + x, 315 + y]], )
    # SHOES
    # Draw an solid ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, BLACK, [240 + x, 345+ y, 35, 15])
    pygame.draw.ellipse(screen, BLACK, [130 + x, 345 + y, 35, 15])

# Loop as long as done == False
while not done:
    ball_pos += ball_change


    if ball_pos > 140:
        ball_change -= 3
    if ball_pos < 0:
        ball_change += 3
    # User did something
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_speed = -3
    if keys[pygame.K_RIGHT]:
        x_speed = 3
    if keys[pygame.K_UP]:
        y_speed = -3
    if keys[pygame.K_DOWN]:
        y_speed = 3

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this

    # Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed

    # Reset x_speed and y_speed for the next frame
    x_speed = 0
    y_speed = 0

    draw_stick_figure(screen, x_coord, y_coord)
    pygame.display.flip()


    clock.tick(60)
    # Be IDLE friendly
    screen.fill(WHITE)
pygame.quit()
