from Board import chess_board
import pygame as d
import os

def count_combinations(n):
    """Counts the number of possible move combinations from the beginning of the game after n total moves"""
    pass

def count_positions(n):
    """Counts the number of possible board positions after n moves"""
    pass

def draw_board(FEN_string):
    list = chess_board(FEN_string)
    
    running = True
    #let user customize below info in settings
    window = d.display.set_mode((920, 890), d.SCALED)
    icon = d.image.load("Assets\Icons\WindowIcon.png")
    white = d.Color(255,255,255)
    light = d.Color(172, 115, 57)
    dark = d.Color(102, 51, 0)
    p = d.image.load(os.path.join('Assets', 'Pieces','bp.png')).convert_alpha()
    P = d.image.load(os.path.join('Assets', 'Pieces','wP.png')).convert_alpha()
    n = d.image.load(os.path.join('Assets', 'Pieces','bn.png')).convert_alpha()
    N = d.image.load(os.path.join('Assets', 'Pieces','wN.png')).convert_alpha()
    b = d.image.load(os.path.join('Assets', 'Pieces','bb.png')).convert_alpha()
    B = d.image.load(os.path.join('Assets', 'Pieces','wB.png')).convert_alpha()
    r = d.image.load(os.path.join('Assets', 'Pieces','br.png')).convert_alpha()
    R = d.image.load(os.path.join('Assets', 'Pieces','wR.png')).convert_alpha()
    q = d.image.load(os.path.join('Assets', 'Pieces','bq.png')).convert_alpha()
    Q = d.image.load(os.path.join('Assets', 'Pieces','wQ.png')).convert_alpha()
    k = d.image.load(os.path.join('Assets', 'Pieces','bk.png')).convert_alpha()
    K = d.image.load(os.path.join('Assets', 'Pieces','wK.png')).convert_alpha()
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
                d.draw.rect(window, dark, (x*100+60, y*100+30, 100, 100))
            else:
                d.draw.rect(window, light, (x*100+60, y*100+30, 100, 100))
    for y in range(8):
        for x in range(8):
            if list[y][x]==0:
                pass
            else:
                window.blit(locals()[list[y][x]], (100*x+60+locals()[list[y][x]+"xy"][0],100*y+30+locals()[list[y][x]+"xy"][0]))
    d.display.update()

    while running:
        for event in d.event.get():
            if (event.type == d.KEYDOWN and event.key == d.K_ESCAPE) or (event.type == d.QUIT): 
                running = False
        
    
    

draw_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")