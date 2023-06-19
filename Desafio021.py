print('Faça um programa que abra e reproduza o audio de um arquivo em mp3.')

import pygame
pygame.init()
pygame.mixer.music.load('audio.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()



