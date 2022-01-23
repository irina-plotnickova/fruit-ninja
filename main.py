import pygame
import sys
import os
import random
import datetime
import schedule

FPS = 50
PRICE = {'Red_Apple.png': 1,
         'Coconut.png': 1, 'Green_Apple.png': 1, 'Mango.png': 1, 'Pineapple.png': 1, 'Strawberry.png': 1,
         'Watermelon.png': 1, 'Banana.png': 1, 'Kiwi.png': 1, 'Lemon.png': 1, 'Lime.png': 1, 'Orange.png': 1,
         'Pear.png': 1, 'Plum.png': 1}


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Sprites(pygame.sprite.Sprite):
    def __init__(self, im):
        super().__init__(all_sprites)
        self.price = PRICE[im]
        self.image = load_image(im)
        self.flag = False
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(10, 1001)
        self.top = random.randrange(20, 150)
        self.rect.y = 730

    def update(self, *args):
        if self.rect.y <= self.top:
            self.flag = True
        print(self.rect.y)
        if self.flag:
            self.rect = self.rect.move(0, 2)
        else:
            self.rect = self.rect.move(0, -2)


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 546
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 550
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


tile_images = load_image('background.jpg')

tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = tile_images
        self.rect = self.image.get_rect()


def generate_level():
    Tile()


pygame.init()
all_sprites = pygame.sprite.Group()
generate_level()
running = True
pygame.init()
clock = pygame.time.Clock()
size = WIDTH, HEIGHT = 1280, 730
screen = pygame.display.set_mode(size)
start_screen()
fruits = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
data = ['Red_Apple.png', 'Coconut.png','Green_Apple.png', 'Mango.png', 'Pineapple.png', 'Strawberry.png',
        'Watermelon.png', 'Banana.png', 'Kiwi.png', 'Lemon.png', 'Lime.png', 'Orange.png', 'Pear.png',
        'Plum.png']


def job():
    k = random.randrange(2, 5)
    for i in range(k):
        Sprites(data[random.randrange(0, 13)])


schedule.every(5).seconds.do(job)

if __name__ == '__main__':
    while running:
        schedule.run_pending()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pass
        screen.fill('white')
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()