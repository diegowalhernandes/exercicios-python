import pygame
print('''===Desafio 21===
Faça um programa em Python que abra e
reproduza o áudio de um arquivo MP3''')
print('=-'*15)
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("oi.mp3")
pygame.mixer.music.play()
pygame.event.wait()
