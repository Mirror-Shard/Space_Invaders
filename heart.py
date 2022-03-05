import pygame


class Heart(pygame.sprite.Sprite):
    # Класс одного пришельца

    def __init__(self, screen):
        # Инициализируем и задаем начальную позицию
        super(Heart, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/heart.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        # Вывод пришельца на экран
        self.screen.blit(self.image, self.rect)
