#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import pygame
from enum import Enum
import random
import time






class Richtungen(Enum):
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4






fenster_breite = 1295
fenster_höhe = 768

pygame.init()
pygame.display.set_caption("Desinfectuser´s Snake")
fenster = pygame.display.set_mode((fenster_breite, fenster_höhe))

refresh_contoller = pygame.time.Clock()

snake_start_position = [250, 250]
snake_body = [[250, 250],
              [240, 250],
              [230, 250]]
frucht_position = [200, 200]

richtung = Richtungen.RIGHT

global score
score = 0

snake_position = snake_start_position

speed = 10

scale = 20





def handle_keys(richtungs):
    neue_richtung = richtung
    for event in [e for e in pygame.event.get() if e.type == pygame.KEYDOWN]:
        if event.key  == pygame.K_UP and richtung != Richtungen.DOWN:
            neue_richtung = Richtungen.UP
        if event.key  == pygame.K_DOWN and richtung != Richtungen.UP:
            neue_richtung = Richtungen.DOWN
        if event.key  == pygame.K_LEFT and richtung != Richtungen.RIGHT:
            neue_richtung = Richtungen.LEFT
        if event.key  == pygame.K_RIGHT and richtung != Richtungen.LEFT:
            neue_richtung = Richtungen.RIGHT
    return neue_richtung


def bewege_schlange(richtungs_anweisung):
    if richtung ==  Richtungen.UP:
        snake_position[1] -= scale
    if richtung == Richtungen.DOWN:
        snake_position[1] += scale
    if richtung == Richtungen.LEFT:
        snake_position[0] -= scale
    if richtung == Richtungen.RIGHT:
        snake_position[0] += scale
    snake_body.insert(0, list(snake_position))


def erstelle_neue_frucht():
    global frucht_position
    frucht_position = [random.randrange(5, (fenster_breite -3 // scale))*scale,
                       random.randrange(5, (fenster_höhe -3 // scale))*scale]

def früchte_sammeln():
    global score
    if snake_position[0] == frucht_position and snake_position[1] == frucht_position[1]:
        score += 1
        erstelle_neue_frucht()
    else:
        snake_body.pop()

def neuzeichnen_des_Spielfelds():
    fenster.fill(pygame.Color(255, 0, 0))
    for body in snake_body:
        pygame.draw.circle(fenster, pygame.Color(0, 0, 255), (body[0], body[1]), scale / 2)
    pygame.draw.rect(fenster, pygame.Color(0, 0, 0), pygame.Rect(frucht_position[0]-scale/2, frucht_position[1]-scale/2, scale, scale))

def game_over():
    if snake_position[0] < 0 or snake_position[0] > fenster_breite - 10:
        game_over_nachricht()
    if snake_position[1] < 0 or snake_position[1] > fenster_höhe - 10:
        game_over_nachricht()
    for blob in snake_body[1:]:
        if snake_position[0] == blob[0] and snake_position[1] == blob[1]:
            game_over_nachricht()


def game_over_nachricht():
    font = pygame.font.SysFont('Arial Black', 48)
    render = font.render(f"Game Over!"
                         "Score: {score}", True, pygame.Color(0, 0, 0))
    rect = render.get_rect()
    rect.midtop(fenster_breite / 2,  fenster_höhe / 2)
    fenster.blit(render, rect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    exit(0)

def paint_hud():
    font = pygame.font.SysFont("Arial", 24)
    render = font.render(f"Score = {score}", True, pygame.Color(0, 0, 0))
    rect = render.get_rect()
    fenster.blit(render, rect)
    pygame.display.flip()


def spiel_loop():
    while True:
        richtungs_anweisung = handle_keys(richtung)
        bewege_schlange(richtungs_anweisung)
        früchte_sammeln()
        neuzeichnen_des_Spielfelds()
        game_over()
        paint_hud()
        pygame.display.update()
        refresh_contoller.tick(speed)








if __name__ == "__main__":
    spiel_loop()