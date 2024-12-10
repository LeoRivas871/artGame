class Settings:
    def __init__(self):
        '''Inicializa las configuraciones estáticas del juego'''
        #Configuración de la pantalla
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)

        '''Mono'''
        #Configuración del mono
        self.mono_vidas = 3
        self.mono_speed = 1.5
        

        #Configuración de disparos del mono
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3