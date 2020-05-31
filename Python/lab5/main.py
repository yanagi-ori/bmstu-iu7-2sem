import time
from random import randint

import pygame

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 3000)

FPS = 20
W = 600
H = 600
BLACK = (0, 0, 0)
OBJECTS = ('./astr1.png', './astr2.png', './nyan.png', './123.png')
OBJ_SURF = []  # для хранения готовых машин-поверхностей
motion = 'STOP'
font = pygame.font.Font(pygame.font.match_font('dejavusans'), 36)

# надо установить видео режим до вызова image.load()
sc = pygame.display.set_mode((W, H))

for i in range(len(OBJECTS)):
    OBJ_SURF.append(pygame.image.load(OBJECTS[i]).convert_alpha())


class Car(pygame.sprite.Sprite):
    def __init__(self, x, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.add(group)  # добавляем в группу
        self.speed = randint(1, 2)  # у машин будет разная скорость

    def update(self):
        if self.rect.y < H:
            self.rect.y += self.speed
        else:
            self.kill()


class Car1(pygame.sprite.Sprite):
    def __init__(self, y, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(0, y))
        self.add(group)  # добавляем в группу
        self.speed = randint(1, 2)  # у машин будет разная скорость

    def update(self):
        if self.rect.x < W:
            self.rect.x += self.speed
        else:
            self.kill()


class UserCar(pygame.sprite.Sprite):
    def __init__(self, x, surf):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.rotate(surf, 0)
        self.image.set_colorkey((247, 247, 247))
        self.rect = self.image.get_rect(center=(300, 300))


cars = pygame.sprite.Group()

# добавляем первую машину, которая появляется сразу
Car(randint(1, W), OBJ_SURF[randint(0, 2)], cars)
user_car1 = UserCar(randint(1, W), pygame.image.load('./ufo.png'))

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            break
        elif i.type == pygame.USEREVENT:
            if randint(0, 1) == 1:
                Car(randint(1, W), OBJ_SURF[randint(0, 3)], cars)
            else:
                Car1(randint(1, H), OBJ_SURF[randint(0, 3)], cars)
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = 'LEFT'
            elif i.key == pygame.K_RIGHT:
                motion = 'RIGHT'
            elif i.key == pygame.K_UP:
                motion = 'UP'
            elif i.key == pygame.K_DOWN:
                motion = 'DOWN'
            else:
                motion = 'STOP'

    if motion == 'LEFT':
        user_car1.rect[0] -= 2
    elif motion == 'RIGHT':
        user_car1.rect[0] += 2
    elif motion == 'UP':
        user_car1.rect[1] -= 2
    elif motion == 'DOWN':
        user_car1.rect[1] += 2

    if pygame.sprite.spritecollideany(user_car1, cars) is not None:
        sc.fill(BLACK)
        sc.blit(font.render('Game is over :c', 1, (180, 0, 0)), (W // 3, H // 2))
        pygame.display.update()
        time.sleep(3)
        break
    else:
        sc.fill((65, 74, 76))
        sc.blit(user_car1.image, user_car1.rect)
        cars.draw(sc)
        pygame.display.update()
        cars.update()

    pygame.time.delay(FPS)
