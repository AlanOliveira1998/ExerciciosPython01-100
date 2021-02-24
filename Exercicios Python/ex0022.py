#Faça um programa que abra e reproduza um arquivo de audio MP3
import pygame
pygame.init()
pygame.mixer.music.load()
pygame.mixer.music.play()
pygame.event.wait()