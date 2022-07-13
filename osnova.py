import pygame, move
from cannon import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run():

    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Demon Killer")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    move.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        move.events(screen, gun, bullets)
        if stats.run_game:
            gun.updatepos()
            move.update(bg_color, screen, stats, sc, gun, inos, bullets)
            move.update_bullets(screen,stats, sc, inos, bullets)
            move.update_inos(stats, screen,sc, gun, inos, bullets)


run()