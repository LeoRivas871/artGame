import sys
import pygame
from settings import Settings
from mono import Mono
from art_bullet import Bullet
#hola
class Pang:
    '''Clase general para gestionar los recursos y el comportamiento del juego'''
    def __init__(self):
        '''Inicializa el juego y crea recursos.'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #Ventana de visualización.
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        #Actualiza el ancho y alto de la pantalla.
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Art the clown Game')

        self.mono = Mono(self)


    def run_game(self):
        '''Inicia el bucle principal para el juego.'''
        while True:
            self._check_events()
            self.mono.update() #Actualiza la posición del personaje
            self._update_bullets() #Actualiza las balas
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        #Responde a las pulsaciones de teclas y eventos de ratón.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #Mover al mono
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        '''Responde a las pulsaciones de teclas.'''
        if event.key == pygame.K_RIGHT:
            self.mono.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.mono.moving_left = True
        elif event.key == pygame.K_SPACE and not self.mono.is_jumping:
            #Iniciar el salto si no está ya saltando.
            self.mono.is_jumping = True
            self.mono.vertical_speed = self.mono.jump_speed
        elif event.key == pygame.K_UP:  # Dispara hacia arriba
            self._fire_bullet(0, -1)  # (x_direction, y_direction)
        elif event.key == pygame.K_w and self.mono.moving_right:  # Dispara diagonalmente hacia arriba y a la derecha
            self._fire_bullet(1, -1)
        elif event.key == pygame.K_w and self.mono.moving_left:  # Dispara diagonalmente hacia arriba y a la izquierda
            self._fire_bullet(-1, -1)
        elif event.key == pygame.K_a:
            self.settings.mono_speed *= 2
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        '''Responde a liberaciones de teclas'''
        if event.key == pygame.K_RIGHT:
            self.mono.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.mono.moving_left = False
        elif event.key == pygame.K_a:
            self.settings.mono_speed = 1.5

    def _fire_bullet(self, x_direction, y_direction):
        """Crea una nueva bala y la añade al grupo de balas."""
        if len(self.mono.bullets) < self.settings.bullets_allowed:  # Limita la cantidad de balas en pantalla
            new_bullet = Bullet(self, self.mono, x_direction, y_direction)
            self.mono.bullets.add(new_bullet)

    def _update_bullets(self):
        """Actualiza la posición de las balas y elimina las que salen de la pantalla."""
        self.mono.bullets.update()  # Llama al metodo update de cada bala

        # Elimina las balas que han desaparecido de la pantalla.
        for bullet in self.mono.bullets.copy():  # Itera sobre una copia para evitar errores al modificar la lista
            if bullet.rect.bottom <= 0:  # Si la bala sale por la parte superior
                self.mono.bullets.remove(bullet)  # Elimina la bala

    def _update_screen(self):
        """Actualiza las imágenes en la pantalla y pasa a la nueva pantalla."""
        self.screen.fill(self.settings.bg_color)  # Rellena la pantalla con el color de fondo

        # Dibuja todas las balas
        for bullet in self.mono.bullets.sprites():
            bullet.draw_bullet()

        self.mono.blitme()  # Dibuja al personaje
        pygame.display.flip()  # Hace visible la pantalla dibujada


if __name__ == '__main__':
    pang = Pang()
    pang.run_game()


















