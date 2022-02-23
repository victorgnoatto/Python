import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()

pygame.mixer.music.set_volume(0.15)
musica_de_fundo = pygame.mixer.music.load('y2meta.com - naruto shippuden lofi _ konoha peace (128 kbps).mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_stomp.wav')
barulho_colisao.set_volume(0.7)

largura = 640
altura = 480
x = int(largura / 2)
y = int(altura / 2)

x_azul = randint(40, 600)
y_azul = randint(50, 430)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Hokage')
relogio = pygame.time.Clock()

while True:
    relogio.tick(60)
    tela.fill((0, 0, 0,))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x = x - 10
    if pygame.key.get_pressed()[K_d]:
        x = x + 10
    if pygame.key.get_pressed()[K_w]:
        y = y - 10
    if pygame.key.get_pressed()[K_s]:
        y = y + 10

    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))
#    pygame.draw.circle(tela, (0, 0, 255), (300, 260), 40)
#    pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 5)
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)

        barulho_colisao.play()

    pygame.display.update()
