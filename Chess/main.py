import pygame as d
from os import path
from math import floor
# TODO make a menu bar
# TODO add different resolutions (1 big and others are smallered img resolutions ?)
# Global variables declaring
window = d.display.set_mode((800, 800), d.SCALED)
icon = d.image.load("Assets\Icons\WindowIcon.png")
white = d.Color(255,255,255)
light = d.Color(172, 115, 57) # TODO let user customize squares colors
dark = d.Color(102, 51, 0)
lightblue = d.Color(100, 100, 255)
darkblue = d.Color(40, 40, 100)
for x in ["bp", "wP", "bn", "wN", "bb", "wB", "br", "wR", "bq", "wQ", "bk", "wK"]:
	globals()[x[1]] = d.image.load(path.join('Assets', 'Pieces', x+'.png')).convert_alpha()
possible_pieces = [["P","N","B","R","Q","K"], ["p","n","b","r","q","k"]]
pxy = Pxy = (23,18)
nxy = Nxy = (21,18)
bxy = Bxy = kxy = Kxy = (18,18)
rxy = Rxy = (20,18)
qxy = Qxy = (15,18)

def list_to_str(chess_board):
	"""Turns the list of lists (the chessboard position) given into a FEN string, useful for chess problems"""
	pass

def str_to_list(FEN_string): # TODO str -> list
	"""Turns the FEN string given into a list of 8 lists with each a length of 8, representing the chessboard"""
	FEN_list = FEN_string.split(" ")
	position_list = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,1,0,0,1],[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]]
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

def draw_board(list):
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
				window.blit(globals()[list[y][x]], (100*x+globals()[list[y][x]+"xy"][0],100*y+globals()[list[y][x]+"xy"][1]))

def blit_on_cursor(piece):
	coordinates = (d.mouse.get_pos()[0]-((100-2*globals()[piece+"xy"][0])/2-2), d.mouse.get_pos()[1]-((100-2*globals()[piece+"xy"][1])//2-2))
	window.blit(globals()[piece], coordinates)

def init(FEN_string):
	if "/" in FEN_string:
		list = str_to_list(FEN_string)

	# Init
	d.init()
	window.fill(white)
	d.display.set_icon(icon)
	d.display.set_caption('Chess')
	draw_board(list)
	d.display.update()
	buttons = d.mouse.get_pressed(5)

	running = True
	dragged = False
	while running: # TODO add chess rules
		for event in d.event.get(): #TODO review ifs order, makes it user-friendly with several clicks at a time
			squarey=floor(d.mouse.get_pos()[1]/100)
			squarex=floor(d.mouse.get_pos()[0]/100)

			if (event.type == d.KEYDOWN and event.key == d.K_ESCAPE) or (event.type == d.QUIT): 
				running = False
			
			elif d.mouse.get_pressed(5)[2]==True: #TODO add other colors with right click and alt / ctrl 
				if (squarex+squarey)%2==1: #TODO add mode with mousebuttondown to color only one square
					d.draw.rect(window, darkblue, (squarex*100, squarey*100, 100, 100))
				else:
					d.draw.rect(window, lightblue, (squarex*100, squarey*100, 100, 100))
				if list[squarey][squarex]!=0:
					window.blit(globals()[list[squarey][squarex]], (100*squarex+globals()[list[squarey][squarex]+"xy"][0],100*squarey+globals()[list[squarey][squarex]+"xy"][1]))

			elif buttons[0]==False and d.mouse.get_pressed(5)[0]==True:
				draw_board(list)
				if list[squarey][squarex] in possible_pieces[list[8][0]%2]:
					piece = list[squarey][squarex]
					list[squarey][squarex] = 0
					draw_board(list)
					blit_on_cursor(piece)
					dragged = True
			
			elif event.type == d.MOUSEMOTION and dragged:
				draw_board(list)
				blit_on_cursor(piece)
 
			elif d.mouse.get_pressed(5)[0]==False and dragged:
				list[squarey][squarex] = piece
				draw_board(list)
				end_coordinates = (100*squarex+globals()[piece+"xy"][0],100*squarey+globals()[piece+"xy"][1])
				window.blit(globals()[piece], end_coordinates)
				list[8][0]+=1
				dragged = False

			buttons = d.mouse.get_pressed(5)
			d.display.update()
	d.quit()

def count_combinations(n):
	"""Counts the number of possible move combinations from the beginning of the game after n total moves"""
	pass

def count_positions(n):
	"""Counts the number of possible board positions after n moves"""
	pass

# Start with chess start position
start_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
init(start_position)