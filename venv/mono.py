import pygame
from pygame.sprite import Sprite

class Mono(Sprite):
    """Clase para representar al personaje (Mono)."""

    def __init__(self, pang):
        """Inicializa el personaje y establece su posición inicial."""
        super().__init__() # Inicializa la clase Sprite
        self.screen = pang.screen
        self.settings = pang.settings
        self.screen_rect = pang.screen.get_rect()

        # Carga la imagen del personaje, la redimensiona y obtiene su rectángulo.
        self.image = pygame.image.load('images/art_png.png')
        self.nuevo_ancho = 100
        self.nuevo_alto = 100
        self.imagen_redimensionada = pygame.transform.scale(self.image, (self.nuevo_ancho, self.nuevo_alto))
        self.rect = self.imagen_redimensionada.get_rect()

        # Coloca al personaje en el centro inferior de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

        # Almacena un valor decimal para la posición horizontal y vertical exacta del personaje.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Banderas de movimiento.
        self.moving_right = False
        self.moving_left = False

        # Configuración del salto.
        self.jump_speed = -15  # Velocidad inicial del salto (negativa para ir hacia arriba).
        self.gravity = 1  # Aceleración de la gravedad.
        self.vertical_speed = 0  # Velocidad vertical actual.
        self.is_jumping = False  # Indica si el personaje está saltando.

        self.bullets = pygame.sprite.Group() # Grupo para almacenar las balas

    def update(self):
        """Actualiza la posición del personaje."""
        # Actualiza la posición horizontal.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.mono_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.mono_speed

        # Actualiza la posición vertical (salto).
        if self.is_jumping:
            self.vertical_speed += self.gravity  # Aplica la gravedad
            self.y += self.vertical_speed  # Actualiza la posición vertical

            # Comprueba si el personaje ha tocado el suelo.
            if self.y >= self.screen_rect.bottom - self.rect.height:
                self.y = self.screen_rect.bottom - self.rect.height
                self.is_jumping = False
                self.vertical_speed = 0

        # Actualiza las posiciones del rectángulo.
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        """Centra al personaje en la pantalla."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Dibuja al personaje en su posición actual."""
        self.screen.blit(self.imagen_redimensionada, self.rect)