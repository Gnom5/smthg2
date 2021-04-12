import sys, pygame, random
class Animal:

    def __init__(self, height, weight, xPos=0, yPos=0, speed=1):
        self.xPos = xPos
        self.yPos = yPos
        self.speed = speed
        self.height = height
        self.weight = weight

    def jump(self):
        print("puff")

    def bark(self):
        print(f"Im {self.height} cm high\n")

    def move(self, horizontalDirection, verticalDirection):
        tmp = horizontalDirection * self.speed
        self.xPos = tmp + self.xPos
        tmp2 = verticalDirection * self.speed
        self.yPos = tmp2 + self.yPos

    rects = []

    def get_rect(self):
        return pygame.rect(self.weight, self.height, self.xPos, self.yPos)


class Cat(Animal):
    def bark(self):
        print(f"Im {self.height} cm high\nMIAUUU")

    def scratch(self, animal):
        animal.weight -= 10

    def get_rect(self):
        return pygame.rect(self.weight, self.height, self.xPos, self.yPos)

color = 0,0,0
obj = Animal(1,1,0,0,1)
screen = pygame.display.set_mode((800,1000))
screen.fill("black")
while 1:
    pygame.display.flip()
    print(obj.xPos, obj.yPos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit()
        if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
            obj.move(1, 0)
        if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
            obj.move(-1, 0)
        if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
            obj.move(0, -1)
        if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
            obj.move(0, 1)



dog = Animal(100, 150)
catty = Cat(50, 20)
dog.jump()
catty.jump()
dog.bark()
catty.bark()