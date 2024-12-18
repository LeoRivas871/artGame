import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Clase para gestionar las balas."""

    def __init__(self, pang, mono, x_direction, y_direction):
        """Crea una bala en la posición actual del personaje."""
        super().__init__() # Llama al constructor de la clase padre (Sprite)
        self.screen = pang.screen # Obtiene la superficie de la pantalla del juego
        self.settings = pang.settings # Obtiene la configuración del juego
        self.color = self.settings.bullet_color # Obtiene el color de la bala de la configuración

        # Crea un rectángulo para la bala en la posición (0, 0) y luego establece la posición correcta.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = mono.rect.midtop # Coloca la bala justo encima del personaje

        # Almacena la posición de la bala como un valor decimal para mayor precisión en el movimiento.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        # Guarda la dirección del movimiento de la bala.
        self.x_direction = x_direction
        self.y_direction = y_direction

        # Ajuste para que la bala salga del centro del personaje y no desde arriba.
        self.y -= self.rect.height # Resta la altura de la bala para que salga desde el centro

    def update(self):
        """Mueve la bala en la pantalla."""
        # Actualiza la posición decimal de la bala.
        self.y += self.settings.bullet_speed * self.y_direction
        self.x += self.settings.bullet_speed * self.x_direction

        # Actualiza la posición del rectángulo de la bala con los nuevos valores.
        self.rect.y = self.y
        self.rect.x = self.x

    def draw_bullet(self):
        """Dibuja la bala en la pantalla."""
        pygame.draw.rect(self.screen, self.color, self.rect)