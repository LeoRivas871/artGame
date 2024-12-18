import sys
import pygame
from settings import Settings
from mono import Mono
#hola
class Pang:
    '''Clase general para gestionar los recursos y el comportamiento del juego'''
    def __init__(self):
        '''Inicializa el juego y crea recursos.'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('PANG')

        # Crea una instancia para guardar las estadisticas del juego.
        # Y crea un marcador.
        self.mono = Mono(self)


    def run_game(self):
        '''Inicia el bucle principal para el juego.'''
        while True:
            self._check_events()
            self.mono.update()
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
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        '''Responde a liberaciones de teclas'''
        if event.key == pygame.K_RIGHT:
            self.mono.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.mono.moving_left = False


    def _update_screen(self):
        '''Actualiza las imagenes en la pantalla y cambia a la pantalla nueva.'''
        self.screen.fill(self.settings.bg_color)
        self.mono.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    pang = Pang()
    pang.run_game()


















