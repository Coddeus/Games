from Board import chess_board
import pygame as d
import os

def count_combinations(n):
    """Counts the number of possible move combinations from the beginning of the game after n total moves"""

def count_positions(n):
    """Counts the number of possible board positions after n moves"""

def draw_board(FEN_string):
    list = chess_board(FEN_string)
    
    running = True
    window = d.display.set_mode((800, 800))
    icon = d.image.load("Chess\Assets\Icons\WindowIcon.png")
    white = d.Color(255,255,255)
    black = d.Color(0,0,0)
    d.init()
    window.fill(white)
    d.display.set_icon(icon)
    d.display.set_caption('Chess')
    for y in range(8):
        for x in range(8):
            if (x+y)%2==1:
                d.draw.rect(window, black, (x*100, y*100, 100, 100))
    d.display.update()

    while running:
        for event in d.event.get():
            if (event.type == d.KEYDOWN and event.key == d.K_ESCAPE) or (event.type == d.QUIT): 
                running = False
        
    
    

draw_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")