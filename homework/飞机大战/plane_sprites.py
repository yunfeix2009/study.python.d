import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1




class GameSprits(pygame.sprite.Sprite):
    def __init__(self,image_name,speed=1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(GameSprits):
    def __init__(self, is_alt=False):
        image_name = "./images/background.png"
        super().__init__(image_name)
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Hero(GameSprits):

    def __init__(self):
        super().__init__("./images/me1.png", 600)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in (1,2,3):
            bullet = Bullet()
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.y - i*20
            self.bullets.add(bullet)

class Bullet(GameSprits):

    def __init__(self):
        super().__init__("./images/bullet1.png",-10)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

class Enemy(GameSprits):

    def __init__(self):
        super().__init__("./images/enemy1.png",800)
        self.speed = random.randint(1,3)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            print("敌机飞出屏幕...")
            self.kill()


