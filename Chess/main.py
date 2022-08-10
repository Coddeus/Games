from strtoboard import chess_board
import pygame as d
from os import path
from math import floor

def count_combinations(n):
    """Counts the number of possible move combinations from the beginning of the game after n total moves"""
    pass

def count_positions(n):
    """Counts the number of possible board positions after n moves"""
    pass

def draw_board(FEN_string):
    list = chess_board(FEN_string)

    #let user customize below info in settings
    window = d.display.set_mode((800, 800), d.SCALED)
    icon = d.image.load("Assets\Icons\WindowIcon.png")
    white = d.Color(255,255,255)
    light = d.Color(172, 115, 57)
    dark = d.Color(102, 51, 0)
    for x in ["bp", "wP", "bn", "wN", "bb", "wB", "br", "wR", "bq", "wQ", "bk", "wK"]:
        locals()[x[1]] = d.image.load(path.join('Assets', 'Pieces', x+'.png')).convert_alpha()
    pxy = Pxy = (23,18)
    nxy = Nxy = (21,18)
    bxy = Bxy = (18,18)
    rxy = Rxy = (20,18)
    qxy = Qxy = (15,18)
    kxy = Kxy = (18,18)

    d.init()
    window.fill(white)
    d.display.set_icon(icon)
    d.display.set_caption('Chess')
    for y in range(8):
        for x in range(8):
            if (x+y)%2==1:
                d.draw.rect(window, dark, (x*100, y*100, 100, 100))
            else:
                d.draw.rect(window, light, (x*100, y*100, 100, 100))
    for y in range(8):
        for x in range(8):
            if list[y][x]==0:
                pass
            else:
                window.blit(locals()[list[y][x]], (100*x+locals()[list[y][x]+"xy"][0],100*y+locals()[list[y][x]+"xy"][0]))
    d.display.update()

    running = True
    moving = False
    while running:
        for event in d.event.get():
            if (event.type == d.KEYDOWN and event.key == d.K_ESCAPE) or (event.type == d.QUIT): 
                running = False
            elif event.type == d.MOUSEBUTTONDOWN:
                squarey=floor(d.mouse.get_pos()[1]/100)
                squarex=floor(d.mouse.get_pos()[0]/100)
                if list[squarey][squarex]!=0:
                    piece = list[squarey][squarex]
                    moving = True
                    for y in range(8):
                        for x in range(8):
                            if (x+y)%2==1:
                                d.draw.rect(window, dark, (x*100, y*100, 100, 100))
                            else:
                                d.draw.rect(window, light, (x*100, y*100, 100, 100))
                    for y in range(8):
                        for x in range(8):
                            if list[y][x]==0 or (y==squarey and x==squarex):
                                pass
                            else:
                                window.blit(locals()[list[y][x]], (100*x+locals()[list[y][x]+"xy"][0],100*y+locals()[list[y][x]+"xy"][0]))
                    coordinates = (d.mouse.get_pos()[0]-((100-2*locals()[piece+"xy"][0])/2-2), d.mouse.get_pos()[1]-((100-2*locals()[piece+"xy"][1])/2-2))
                    window.blit(locals()[piece], coordinates)  
            elif event.type == d.MOUSEBUTTONUP:
                moving = False
            elif event.type == d.MOUSEMOTION and moving:
                for y in range(8):
                    for x in range(8):
                        if (x+y)%2==1:
                            d.draw.rect(window, dark, (x*100, y*100, 100, 100))
                        else:
                            d.draw.rect(window, light, (x*100, y*100, 100, 100))
                for y in range(8):
                    for x in range(8):
                        if list[y][x]==0 or (y==squarey and x==squarex):
                            pass
                        else:
                            window.blit(locals()[list[y][x]], (100*x+locals()[list[y][x]+"xy"][0],100*y+locals()[list[y][x]+"xy"][0]))
                coordinates = (d.mouse.get_pos()[0]-((100-2*locals()[piece+"xy"][0])/2-2), d.mouse.get_pos()[1]-((100-2*locals()[piece+"xy"][1])//2-2))
                window.blit(locals()[piece], coordinates)  
            d.display.update()
    d.quit()
    
    

draw_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")