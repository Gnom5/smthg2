import sys, pygame, random, time
pygame.init()

size = width, height = 1280, 720
SPEED = 700
black = 0, 0, 0
NORM = 25
FPS = 60
COLORS = [
        "white",
        "blue",
        "green",
        "red",
        "grey",
        "purple"
]
screen = pygame.display.set_mode(size)


def get_rect():
    return pygame.Rect(random.randint(0, width - NORM), random.randint(0, height - NORM), NORM, NORM)


rect = get_rect()

# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
#         if event.type == pygame.KEYDOWN:
#             if pygame.key.get_pressed()[pygame.K_MINUS]:
#                  if rects:
#                      rects.pop()
#             if pygame.key.get_pressed()[pygame.K_ESCAPE]:
#                 sys.exit()
#             if pygame.key.get_pressed()[pygame.K_w]:
#                 pass
#             else:
#                 rects.append(get_rect())
#         if event.type == pygame.KEYUP:
#             print("Key released")
t1 = time.time()
while 1:
    t2 = t1
    t1 = time.time()
    timeDeltaTime = t1 - t2
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit()
        if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
            rect.move_ip(0, -1 * SPEED * timeDeltaTime)
            print("Up")
        if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
            rect.move_ip(0, 1 * SPEED * timeDeltaTime)
            print("Down")
        if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
            rect.move_ip(-1 * SPEED * timeDeltaTime, 0)
            if rect.x <= 0:
                rect.update(width - NORM, rect.y, NORM, NORM)
            print("Left")
        if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
            rect.move_ip(1 * SPEED * timeDeltaTime, 0)
            if rect.x >= width:
                rect.update(0, rect.y, NORM, NORM)
            print("Right")
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            rect.update(0, 0, NORM, NORM)
    if timeDeltaTime < 1/FPS:
        time.sleep(1/FPS - timeDeltaTime)
    screen.fill(black)
    pygame.draw.rect(screen, "yellow", rect)
    pygame.display.flip()

