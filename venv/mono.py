import pygame
from pygame.sprite import Sprite

class Mono(Sprite):
    def __init__(self,pang):
        super().__init__()
        self.screen = pang.screen
        self.settings = pang.settings
        self.screen_rect = pang.screen.get_rect()

        #Carga la imagen del tirador, lo ajsuta y obtiene su rect
        self.image = pygame.image.load('images/art_png.png')
        self.nuevo_ancho = 100
        self.nuevo_alto = 100
        self.imagen_redimensionada = pygame.transform.scale(self.image, (self.nuevo_ancho, self.nuevo_alto))
        self.rect = self.imagen_redimensionada.get_rect()
        
        #Coloca inicialmente cada nave nueva en el centro de la parte inferior de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

        # Guarda un valor decimal para la posicion horizontal exacta de la nave.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Bandera de movimiento; empieza con una bandera que no se mueve.
        self.moving_right = False
        self.moving_left = False

        # Configuracion de saltos del mono y gravedad
        self.jump_speed = -15  # Velocidad inicial del salto (negativa para ir hacia arriba.).
        self.gravity = 1  # Velocidad de caída (gravedad).
        self.vertical_speed = 0  # Velocidad vertical actual.
        self.is_jumping = False  #Bandera: ¿Esta saltando?.
        
    def update(self):
        '''Actualiza da posición de la nave en función de la bandera de movimiento'''
        # Actualiza el valor x de la nave, no el rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.mono_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.mono_speed

        #Movimiento vertical
        if self.is_jumping:
            self.vertical_speed += self.gravity # Aumentar la velocidad vertical por la gravedad
            self.y += self.vertical_speed #Actualizar la posición vertical.
            #print(f'Salto en progreso. Velocidad vertical: {self.vertical_speed}, Posicion y: {self.y}')

            #Si el personaje toca el suelo, detener el salto.
            if self.y >= self.screen_rect.bottom - self.rect.height:
                self.y = self.screen_rect.bottom - self.rect.height
                self.is_jumping = False
                self.vertical_speed = 0
                #print("El personaje ha aterrizado")

        # Asegurarnos de que no haya sido movido fuera de los límites
        if self.y > self.screen_rect.bottom - self.rect.height:
            self.y = self.screen_rect.bottom - self.rect.height

        #Actualiza las posiciones del rectángulo.
        self.rect.x = self.x
        self.rect.y = self.y
        #print(f"Posición actual - x: {self.x}, y: {self.y}")



    def center_ship(self):
        '''Centra la nave en la pantalla.'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
    def blitme(self):
        '''Dibuja al payaso en su ubicación actual.'''
        self.screen.blit(self.imagen_redimensionada,self.rect)