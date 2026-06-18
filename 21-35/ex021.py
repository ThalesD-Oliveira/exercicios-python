import pygame
import time

# Inicializa o mixer de áudio
pygame.mixer.init()

# Carrega e toca a música
pygame.mixer.music.load('source/songs/Alex_Valin_-_Lofi.mp3')

# music.play(-1) --> Toca em loop infinito | #pygame.mixer.music.play() --> Toca uma vez
# (0 é o padrão, toca uma vez) (1 toca duas vezes) (2 toca três vezes) (3 toca quatro vezes)
pygame.mixer.music.play(-1)

# Mantém o programa rodando enquanto a música toca
# Se você não fizer isso, o programa vai terminar e a música vai parar imediatamente, ou seja, você não vai ouvir nada
while pygame.mixer.music.get_busy():
    time.sleep(1)
