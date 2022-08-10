import pygame as d
from os import path
from math import floor

def list_to_str(chess_board):
	"""Turns the list of lists (the chessboard position) given into a FEN string"""
	pass

def str_to_list(FEN_string):
	"""Turns the FEN string given into a list of 8 lists with each a length of 8, representing the chessboard"""
	FEN_list = FEN_string.split(" ")
	position_list = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
	position_listx = 0
	position_listy = 0
	numbers = ["1","2","3","4","5","6","7","8"]
	for x in FEN_list[0]:
		if (x) == "/":
			position_listx=0
			position_listy+=1
		elif any(x==n for n in numbers):
			x=int(x)
			position_listx+=x
		else:
			position_list[position_listy][position_listx] = x
			position_listx+=1
	return position_list

def draw_board(list, squarex=9, squarey=9):
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
				window.blit(globals()[list[y][x]], (100*x+globals()[list[y][x]+"xy"][0],100*y+globals()[list[y][x]+"xy"][1]))

def init(FEN_string):
	list = str_to_list(FEN_string)

	# Init
	d.init()
	window.fill(white)
	d.display.set_icon(icon)
	d.display.set_caption('Chess')
	draw_board(list)
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
					draw_board(list, squarex, squarey)
					coordinates = (d.mouse.get_pos()[0]-((100-2*globals()[piece+"xy"][0])/2-2), d.mouse.get_pos()[1]-((100-2*globals()[piece+"xy"][1])/2-2))
					window.blit(globals()[piece], coordinates)

			elif event.type == d.MOUSEMOTION and moving:
				draw_board(list, squarex, squarey)
				coordinates = (d.mouse.get_pos()[0]-((100-2*globals()[piece+"xy"][0])/2-2), d.mouse.get_pos()[1]-((100-2*globals()[piece+"xy"][1])//2-2))
				window.blit(globals()[piece], coordinates)   
 
			elif event.type == d.MOUSEBUTTONUP:
				if moving:
					endsquarey=floor(d.mouse.get_pos()[1]/100)
					endsquarex=floor(d.mouse.get_pos()[0]/100)
					draw_board(list, squarex, squarey)
					end_coordinates = (100*endsquarex+globals()[list[squarey][squarex]+"xy"][0],100*endsquarey+globals()[list[squarey][squarex]+"xy"][1])
					window.blit(globals()[piece], end_coordinates)
				moving = False
			
			d.display.update()
	d.quit()

def count_combinations(n):
	"""Counts the number of possible move combinations from the beginning of the game after n total moves"""
	pass

def count_positions(n):
	"""Counts the number of possible board positions after n moves"""
	pass

# Global variables declaring
window = d.display.set_mode((800, 800), d.SCALED)
icon = d.image.load("Assets\Icons\WindowIcon.png")
white = d.Color(255,255,255)
light = d.Color(172, 115, 57)
dark = d.Color(102, 51, 0)
for x in ["bp", "wP", "bn", "wN", "bb", "wB", "br", "wR", "bq", "wQ", "bk", "wK"]:
	globals()[x[1]] = d.image.load(path.join('Assets', 'Pieces', x+'.png')).convert_alpha()
pxy = Pxy = (23,18)
nxy = Nxy = (21,18)
bxy = Bxy = (18,18)
rxy = Rxy = (20,18)
qxy = Qxy = (15,18)
kxy = Kxy = (18,18)

# Start with chess start position
init("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")