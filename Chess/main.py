from cmath import cos, sin
from xml.dom.minidom import TypeInfo
import pygame as d
import pygame.gfxdraw as gfxd
from os import path
from math import floor, pi, radians, sin, cos, atan
import copy

# TODO make a start menu with PvP (local or distant), PvC, computer analysis, AI trainer, local app for playing on chess.com or lichess or …
# TODO make a menu bar
# TODO add different resolutions (1 big and others are smallered img resolutions ?)
# TODO timed games
# TODO show coordinates on board

# Global variables declaring list
clock = d.time.Clock()
window = d.display.set_mode((800, 800), d.SCALED)
icon = d.image.load("Assets\Icons\WindowIcon.png")
white = d.Color(255,255,255)
light = d.Color(172, 115, 57) # TODO let user customize squares colors (and what else ?)
dark = d.Color(102, 51, 0)
lightblue = d.Color(100, 100, 255)
darkblue = d.Color(40, 40, 100)
lightorange = d.Color(120, 80, 40)
darkorange = d.Color(60, 30, 0)
red = d.Color(150,0,0)
bglist = [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]
for x in ["bp", "wP", "bn", "wN", "bb", "wB", "br", "wR", "bq", "wQ", "bk", "wK"]:
	globals()[x[1]] = d.image.load(path.join('Assets', 'Pieces', x+'.png')).convert_alpha()
all_pieces = [["P","N","B","R","Q","K"], ["p","n","b","r","q","k"]]
testsquarex = 0
testsquarey = 0
possible_squares = []
list = []
pxy = Pxy = (23,18)
nxy = Nxy = (21,18)
bxy = Bxy = kxy = Kxy = (18,18)
rxy = Rxy = (20,18)
qxy = Qxy = (15,18)
start_position = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
game_positions = []
isfinished = False
uncolored = False
arrows_list = []
startartsquare = []

def list_to_str(chess_board):
	"""Turns the list of lists (the chessboard position) given into a FEN string, useful for chess problems"""
	pass

def str_to_list(FEN_string):
	"""Turns the FEN string given into a list of 8 lists with each a length of 8, representing the chessboard"""
	FEN_list = FEN_string.split(" ")
	position_list = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,[0,0],[0,0],[0,0],0], [[0,0],[0,0]]]
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
	if FEN_list[1] == "w":
		position_list[8][0] = 0
	elif FEN_list[1] == "b":
		position_list[8][0] = 1
	if "K" in FEN_list[2]:
		position_list[8][1][0]=1
	if "Q" in FEN_list[2]:
		position_list[8][1][1]=1
	if "k" in FEN_list[2]:
		position_list[8][2][0]=1
	if "q" in FEN_list[2]:
		position_list[8][2][1]=1
	globals()["game_positions"].append(copy.deepcopy([position_list[:8], position_list[8][0]%2, position_list[8][1:4], 1]))
	return position_list

def draw_board(list, possibilities=[], kingmoving = False, startsquarey=-17, startsquarex=-1):
	for y in range(8):
		for x in range(8):
			if (x+y)%2==1:
				d.draw.rect(window, dark, (x*100, y*100, 100, 100))
			else:
				d.draw.rect(window, light, (x*100, y*100, 100, 100))
	kingsquareyx = king_coor(list) if not kingmoving else [startsquarey,startsquarex]
	if ischeck(list, kingsquareyx[0], kingsquareyx[1], list[8][0]%2):
		d.draw.rect(window, red, (kingsquareyx[1]*100, kingsquareyx[0]*100, 100, 100))
		if (kingsquareyx[1]+kingsquareyx[0])%2==1:
			d.draw.circle(window, dark, (kingsquareyx[1]*100+50, kingsquareyx[0]*100+50), 50)
		else:
			d.draw.circle(window, light, (kingsquareyx[1]*100+50, kingsquareyx[0]*100+50), 50)
	if list[8][0]>=1:
		for c in list[9]:
			if (c[0]+c[1])%2==1:
				d.draw.rect(window, darkorange, (c[1]*100, c[0]*100, 100, 100))
			else:
				d.draw.rect(window, lightorange, (c[1]*100, c[0]*100, 100, 100)) 
	for y in range(8):
		for x in range(8):
			if list[y][x]==0:
				pass
			else:
				window.blit(globals()[list[y][x]], (100*x+globals()[list[y][x]+"xy"][0],100*y+globals()[list[y][x]+"xy"][1]))
	for p in possibilities:
		gfxd.filled_circle(window, 100*p[1]+48,100*p[0]+48, 15, (50,50,50,100))
	globals()["bglist"] = [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]

def blit_on_cursor(piece):
	coordinates = (d.mouse.get_pos()[0]-((100-2*globals()[piece+"xy"][0])/2-2), d.mouse.get_pos()[1]-((100-2*globals()[piece+"xy"][1])//2-2))
	window.blit(globals()[piece], coordinates)

def possible_squares(list,piece,squarey,squarex):
	possible_squares = [] # TODO user choice to show possible squares when piece is clicked or not

	if piece == "P":
		if list[squarey-1][squarex]==0:
			possible_squares.append([squarey-1,squarex])
			if squarey == 6:
				if list[4][squarex]==0:
					possible_squares.append([4,squarex])
		if squarex>=1:
			if list[squarey-1][squarex-1] in all_pieces[1]:
				possible_squares.append([squarey-1,squarex-1])
		if squarex<=6:
			if list[squarey-1][squarex+1] in all_pieces[1]:
				possible_squares.append([squarey-1,squarex+1])
		if list[8][3][0] ==squarey and (list[8][3][1] ==squarex-1 or list[8][3][1] ==squarex+1):
			possible_squares.append([list[8][3][0]-1, list[8][3][1]])
	elif piece == "p":
		if list[squarey+1][squarex]==0:
			possible_squares.append([squarey+1,squarex])
			if squarey == 1:
				if list[3][squarex]==0:
					possible_squares.append([3,squarex])
		if squarex>=1:
			if list[squarey+1][squarex-1] in all_pieces[0]:
				possible_squares.append([squarey+1,squarex-1])
		if squarex<=6:
			if list[squarey+1][squarex+1] in all_pieces[0]:
				possible_squares.append([squarey+1,squarex+1])
		if list[8][3][0] ==squarey and (list[8][3][1] ==squarex-1 or list[8][3][1] ==squarex+1):
			possible_squares.append([list[8][3][0]+1, list[8][3][1]])

	elif piece == "N" or piece == "n":
		conditions = ["squarex>=1 and squarey>=2", "squarex>=2 and squarey>=1", "squarex>=2 and squarey<=6", "squarex>=1 and squarey<=5", "squarex<=6 and squarey<=5", "squarex<=5 and squarey<=6", "squarex<=5 and squarey>=1", "squarex<=6 and squarey>=2"]
		verify_squares = [[squarey-2, squarex-1], [squarey-1, squarex-2], [squarey+1, squarex-2], [squarey+2, squarex-1], [squarey+2, squarex+1], [squarey+1, squarex+2], [squarey-1, squarex+2], [squarey-2, squarex+1]]
		for i in range(8):
			if eval(conditions[i]):
				if list[verify_squares[i][0]][verify_squares[i][1]] not in all_pieces[list[8][0]%2]:
					possible_squares.append([verify_squares[i][0], verify_squares[i][1]])
	
	elif piece == "B" or piece == "b":
		squareyop = ["testsquarey+1", "testsquarey+1", "testsquarey-1", "testsquarey-1"]
		squarexop = ["testsquarex+1", "testsquarex-1", "testsquarex+1", "testsquarex-1"]
		for i, j in zip(squareyop, squarexop):
			testsquarex, testsquarey = squarex, squarey
			keepon = True
			while keepon:
				testsquarey, testsquarex = eval(i), eval(j)
				if testsquarex<=7 and testsquarex>=0 and testsquarey<=7 and testsquarey>=0 and list[testsquarey][testsquarex] not in all_pieces[list[8][0]%2]:
					possible_squares.append([testsquarey, testsquarex])
					if list[testsquarey][testsquarex] in all_pieces[(list[8][0]+1)%2]:
						keepon = False
				else:
					keepon = False
	
	elif piece == "R" or piece == "r":
		squareyop = ["testsquarey+1", "testsquarey", "testsquarey", "testsquarey-1"]
		squarexop = ["testsquarex", "testsquarex-1", "testsquarex+1", "testsquarex"]
		for i, j in zip(squareyop, squarexop):
			testsquarex, testsquarey = squarex, squarey
			keepon = True
			while keepon:
				testsquarey, testsquarex = eval(i), eval(j)
				if testsquarex<=7 and testsquarex>=0 and testsquarey<=7 and testsquarey>=0 and list[testsquarey][testsquarex] not in all_pieces[list[8][0]%2]:
					possible_squares.append([testsquarey, testsquarex])
					if list[testsquarey][testsquarex] in all_pieces[(list[8][0]+1)%2]:
						keepon = False
				else:
					keepon = False
			else:
				keepon = False

	elif piece == "Q" or piece == "q":
		squareyop = ["testsquarey+1", "testsquarey+1", "testsquarey-1", "testsquarey-1", "testsquarey+1", "testsquarey", "testsquarey", "testsquarey-1"]
		squarexop = ["testsquarex+1", "testsquarex-1", "testsquarex+1", "testsquarex-1", "testsquarex", "testsquarex-1", "testsquarex+1", "testsquarex"]
		for i, j in zip(squareyop, squarexop):
			testsquarex, testsquarey = squarex, squarey
			keepon = True
			while keepon:
				testsquarey, testsquarex = eval(i), eval(j)
				if testsquarex<=7 and testsquarex>=0 and testsquarey<=7 and testsquarey>=0 and list[testsquarey][testsquarex] not in all_pieces[list[8][0]%2]:
					possible_squares.append([testsquarey, testsquarex])
					if list[testsquarey][testsquarex] in all_pieces[(list[8][0]+1)%2]:
						keepon = False
				else:
					keepon = False
	
	elif piece == "K" or piece == "k":
		squareyop = ["squarey+1", "squarey+1", "squarey-1", "squarey-1", "squarey+1", "squarey", "squarey", "squarey-1"]
		squarexop = ["squarex+1", "squarex-1", "squarex+1", "squarex-1", "squarex", "squarex-1", "squarex+1", "squarex"]
		for i, j in zip(squareyop, squarexop):
			testsquarey, testsquarex = eval(i), eval(j)
			if testsquarex<=7 and testsquarex>=0 and testsquarey<=7 and testsquarey>=0 and list[testsquarey][testsquarex] not in all_pieces[list[8][0]%2]:
				possible_squares.append([testsquarey, testsquarex])
		if piece == "K":
			if list[8][1][0]==1 and list[7][5]==0 and list[7][6]==0 and not (ischeck(list, 7, 4, 0) or ischeck(list, 7, 5, 0) or ischeck(list, 7, 6, 0)):
				possible_squares.append([squarey, squarex+2])
			if list[8][1][1]==1 and list[7][3]==0 and list[7][2]==0 and list[7][1]==0 and not (ischeck(list, 7, 4, 0) or ischeck(list, 7, 3, 0) or ischeck(list, 7, 2, 0)):
				possible_squares.append([squarey, squarex-2])
		if piece == "k":
			if list[8][2][0]==1 and list[0][5]==0 and list[0][6]==0 and not (ischeck(list, 0, 4, 1) or ischeck(list, 0, 5, 1) or ischeck(list, 0, 6, 1)):
				possible_squares.append([squarey, squarex+2])
			if list[8][2][1]==1 and list[0][3]==0 and list[0][2]==0 and list[0][1]==0 and not (ischeck(list, 0, 4, 1) or ischeck(list, 0, 3, 1) or ischeck(list, 0, 2, 1)):
				possible_squares.append([squarey, squarex-2])
	
	for coor in reversed(possible_squares):
		savecoor = list[coor[0]][coor[1]]
		list[squarey][squarex]=0
		list[coor[0]][coor[1]]=piece
		if ischeck(list, king_coor(list)[0], king_coor(list)[1], list[8][0]%2):
			possible_squares.remove(coor)
		list[squarey][squarex]=piece
		list[coor[0]][coor[1]]=savecoor
	return possible_squares

def king_coor(list): # place of the king which color has to play
	if list[8][0]%2==0:
		king="K"
	else:
		king="k"
	for y in range(8):
		for x in range(8):
			if list[y][x]==king:
				return y, x

def ischeck(list, squarey, squarex, squaredefender):
	ischeck = False
	conditions = ["squarex>=1 and squarey>=2", "squarex>=2 and squarey>=1", "squarex>=2 and squarey<=6", "squarex>=1 and squarey<=5", "squarex<=6 and squarey<=5", "squarex<=5 and squarey<=6", "squarex<=5 and squarey>=1", "squarex<=6 and squarey>=2"]
	verify_squares = [[squarey-2, squarex-1], [squarey-1, squarex-2], [squarey+1, squarex-2], [squarey+2, squarex-1], [squarey+2, squarex+1], [squarey+1, squarex+2], [squarey-1, squarex+2], [squarey-2, squarex+1]]
	for i in range(8):
		if eval(conditions[i]):
			if list[verify_squares[i][0]][verify_squares[i][1]] == all_pieces[(squaredefender+1)%2][1]:
				ischeck = True

	if ischeck == False:

		if squaredefender==0:
			if squarey>=1:
				if squarex>=1:
					if list[squarey-1][squarex-1]=="p":
						ischeck = True
				if squarex<=6:
					if list[squarey-1][squarex+1]=="p":
						ischeck = True
			if ischeck == False:
				ways=0
				squareyop = ["testsquarey+1", "testsquarey+1", "testsquarey-1", "testsquarey-1", "testsquarey+1", "testsquarey", "testsquarey", "testsquarey-1"]
				squarexop = ["testsquarex+1", "testsquarex-1", "testsquarex+1", "testsquarex-1", "testsquarex", "testsquarex-1", "testsquarex+1", "testsquarex"]
				for i, j in zip(squareyop, squarexop):
					testsquarex, testsquarey = squarex, squarey
					keepon = True
					while keepon and ischeck==False:
						testsquarey, testsquarex = eval(i), eval(j)
						if testsquarex<=7 and testsquarex>=0 and testsquarey<=7 and testsquarey>=0:
							if list[testsquarey][testsquarex] in all_pieces[0]:
								keepon = False
							elif list[testsquarey][testsquarex] in all_pieces[1]:
								keepon = False
								if ways<=3:
									if list[testsquarey][testsquarex]=="q" or list[testsquarey][testsquarex]=="b":
										ischeck = True
								else:
									if list[testsquarey][testsquarex]=="q" or list[testsquarey][testsquarex]=="r":
										ischeck = True
						else:
							keepon = False
					ways+=1
				if ischeck == False:
					squareyop = ["squarey+1", "squarey+1", "squarey-1", "squarey-1", "squarey+1", "squarey", "squarey", "squarey-1"]
					squarexop = ["squarex+1", "squarex-1", "squarex+1", "squarex-1", "squarex", "squarex-1", "squarex+1", "squarex"]
					for i, j in zip(squareyop, squarexop):
						testsquarey, testsquarex = eval(i), eval(j)
						if testsquarex<=7 and testsquarex>=0 and testsquarey<=7 and testsquarey>=0 and list[testsquarey][testsquarex]=="k":
							ischeck = True

		elif squaredefender==1:
			if squarey<=6:
				if squarex>=1:
					if list[squarey+1][squarex-1]=="P":
						ischeck = True
				if squarex<=6:
					if list[squarey+1][squarex+1]=="P":
						ischeck = True
			if ischeck == False:
				ways=0
				squareyop = ["testsquarey+1", "testsquarey+1", "testsquarey-1", "testsquarey-1", "testsquarey+1", "testsquarey", "testsquarey", "testsquarey-1"]
				squarexop = ["testsquarex+1", "testsquarex-1", "testsquarex+1", "testsquarex-1", "testsquarex", "testsquarex-1", "testsquarex+1", "testsquarex"]
				for i, j in zip(squareyop, squarexop):
					testsquarex, testsquarey = squarex, squarey
					keepon = True
					while keepon and ischeck==False:
						testsquarey, testsquarex = eval(i), eval(j)
						if testsquarex<=7 and testsquarex>=0 and testsquarey<=7 and testsquarey>=0:
							if list[testsquarey][testsquarex] in all_pieces[1]:
								keepon = False
							elif list[testsquarey][testsquarex] in all_pieces[0]:
								keepon = False
								if ways<=3:
									if list[testsquarey][testsquarex]=="Q" or list[testsquarey][testsquarex]=="B":
										ischeck = True
								else:
									if list[testsquarey][testsquarex]=="Q" or list[testsquarey][testsquarex]=="R":
										ischeck = True
						else:
							keepon = False
					ways+=1
				if ischeck == False:
					squareyop = ["squarey+1", "squarey+1", "squarey-1", "squarey-1", "squarey+1", "squarey", "squarey", "squarey-1"]
					squarexop = ["squarex+1", "squarex-1", "squarex+1", "squarex-1", "squarex", "squarex-1", "squarex+1", "squarex"]
					for i, j in zip(squareyop, squarexop):
						testsquarey, testsquarex = eval(i), eval(j)
						if testsquarex<=7 and testsquarex>=0 and testsquarey<=7 and testsquarey>=0 and list[testsquarey][testsquarex]=="K":
							ischeck = True
	return ischeck

def aftermove(list, piece, squarey, squarex, startsquarey, startsquarex): # TODO handle endgame draws (timed), moves repetition and all promotions
	global game_positions
	global isfinished
	if list[squarey][squarex] in all_pieces[0] or list[squarey][squarex] in all_pieces[1]:
		game_positions=[game_positions[-1]]
	list[squarey][squarex] = piece
	if piece == "p" or piece == "P":
		game_positions=[game_positions[-1]]
		if (piece == "P" and squarey == list[8][3][0]-1 and squarex == list[8][3][1]) or (piece == "p" and squarey == list[8][3][0]+1 and squarex == list[8][3][1]):
			list[list[8][3][0]][list[8][3][1]] = 0
		if squarey == startsquarey-2 or squarey == startsquarey+2:
			list[8][3] = [squarey, squarex]
		else:
			list[8][3] = [-1, -1]
		if "P" in list[0]: 
			list[0][list[0].index("P")]="Q"
		elif "p" in list[7]:
			list[7][list[7].index("p")]="q"
	elif piece == "K":
		if squarey==7 and squarex ==6 and list[8][1][0]==1:
			list[7][7]=0
			list[7][5]="R"
		elif squarey==7 and squarex ==2 and list[8][1][1]==1:
			list[7][0]=0
			list[7][3]="R"
		list[8][1][0], list[8][1][1] = 0, 0
	elif piece == "k":
		if squarey==0 and squarex ==6 and list[8][2][0]==1:
			list[0][7]=0
			list[0][5]="r"
		elif squarey==0 and squarex ==2 and list[8][2][1]==1:
			list[0][0]=0
			list[0][3]="r"
		list[8][2][0], list[8][2][1] = 0, 0
	elif piece == "R" and (list[8][1][0]==1 or list[8][1][1]==1):
		if list[7][7]==0:
			list[8][1][0]=0
		elif list[7][0]==0:
			list[8][1][1]=0
	elif piece == "r" and (list[8][2][0]==1 or list[8][2][1]==1):
		if list[0][7]==0:
			list[8][2][0]=0
		elif list[0][0]==0:
			list[8][2][1]=0
	list[9] = [[startsquarey, startsquarex], [squarey, squarex]]
	addposition = True
	repetition_draw_transformed_list = [list[:8], list[8][0]%2, list[8][1:4], 1]
	for n in range(len(game_positions)):
		if repetition_draw_transformed_list[:3]==game_positions[n][:3]:
			addposition = False
			game_positions[n][3]+=1
			if game_positions[n][3]>=5:
				print("Draw : Repetition !")
				d.display.set_caption('No one\'s game')
				isfinished = True
			break
	if addposition:
		game_positions.append(copy.deepcopy(repetition_draw_transformed_list))
	list[8][0]+=1
	if not canmove(list, list[8][0]%2):
		if ischeck(list, king_coor(list)[0], king_coor(list)[1], list[8][0]%2):
			if list[8][0]%2==0:
				print("Black wins !")
				d.display.set_caption('Black\'s game')
				isfinished = True
			else:
				print("White wins !")
				d.display.set_caption('White\'s game')
				isfinished = True
		else:
			print("Draw : Stalemate !") # TODO animate end of game lost king flip on red square, won king on green, particle stars around ; Draw = 360° kings
			d.display.set_caption('No one\'s game')
			isfinished = True
	if list[8][4]>=50:
		print("Draw : 50 moves rule !")
		d.display.set_caption('No one\'s game')
		isfinished = True

def canmove(list, whotoplay):
	for y in range(8):
		for x in range(8):
			if list[y][x] in all_pieces[whotoplay]:
				if possible_squares(list, list[y][x], y, x)!=[]:
					return True
	return False

def draw_arrow(artsquarey, artsquarex, squarey, squarex): # user choice draw arrows to only on possible squares
	global uncolored
	global list
	global arrows_list
	global startartsquare
	if [artsquarey, artsquarex] != [squarey, squarex]:
		if uncolored == False:
			if globals()["bglist"][artsquarey][artsquarex]==0: #TODO draw arrows
				if (artsquarex+artsquarey)%2==1: # TODO Premoves
					d.draw.rect(window, darkblue, (artsquarex*100, artsquarey*100, 100, 100))
				else:
					d.draw.rect(window, lightblue, (artsquarex*100, artsquarey*100, 100, 100))
				globals()["bglist"][artsquarey][artsquarex]=1
			elif globals()["bglist"][artsquarey][artsquarex]==1:
				if (artsquarex+artsquarey)%2==1:
					d.draw.rect(window, dark, (artsquarex*100, artsquarey*100, 100, 100))
				else:
					d.draw.rect(window, light, (artsquarex*100, artsquarey*100, 100, 100))
				globals()["bglist"][artsquarey][artsquarex]=0
			if list[artsquarey][artsquarex]!=0:
				window.blit(globals()[list[artsquarey][artsquarex]], (100*artsquarex+globals()[list[artsquarey][artsquarex]+"xy"][0],100*artsquarey+globals()[list[artsquarey][artsquarex]+"xy"][1]))
			uncolored = True
			startartsquare = [artsquarey, artsquarex]
		if (startartsquare[0], startartsquare[1], squarey, squarex) not in arrows_list:
			if arrows_list!=[]:
				if arrows_list[-1]==(startartsquare[1], startartsquare[0], artsquarex, artsquarey):
					arrows_list.pop(-1)
			arrows_list.append((startartsquare[1], startartsquare[0], squarex, squarey))
		draw_board(list)
		for tuuuple in arrows_list:
			"""xdiff = tuuuple[2]-tuuuple[0]
			ydiff = tuuuple[3]-tuuuple[1]
			xpixels = 10*(1-cos(atan(ydiff/xdiff)))
			print("x : "+str(xpixels))
			ypixels = 10*(1+sin(atan(ydiff/xdiff)))
			print("y : "+str(ypixels))
			#if xdiff==0:
				
			#elif ydiff==0:

			#else:"""
			gfxd.filled_polygon(window, ((100*tuuuple[0]+38,100*tuuuple[1]+48),(100*tuuuple[0]+58,100*tuuuple[1]+48),(100*tuuuple[2]+58,100*tuuuple[3]+48),(100*tuuuple[2]+38,100*tuuuple[3]+48)), (0,100,0,150))
	
			

def init(FEN_string):
	"""Initializes with a FEN string or a custom-format list from this file"""
	global list
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

	global isfinished
	global uncolored
	global arrows_list
	possibilities = []
	possibilitieson = False
	running = True
	dragged = False
	drawing = False
	while running: # TODO end chess rules
		for event in d.event.get(): #TODO review ifs order, makes it user-friendly with several clicks at a time (customizable)

			squarey=floor(d.mouse.get_pos()[1]/100)
			squarex=floor(d.mouse.get_pos()[0]/100)

			if (event.type == d.KEYDOWN and event.key == d.K_ESCAPE) or (event.type == d.QUIT): 
				running = False
			
			elif buttons[0]==False and d.mouse.get_pressed(5)[0]==True:
				draw_board(list)
				if possibilitieson and [squarey, squarex] in possibilities:
					if piece == "p" or piece == "P" or list[squarey][squarex] in all_pieces[0] or list[squarey][squarex] in all_pieces[0]:
						list[8][4]=0
					else:
						list[8][4]+=1
					list[startsquarey][startsquarex] = 0
					possibilities = []
					possibilitieson = False
					aftermove(list, piece, squarey, squarex, startsquarey, startsquarex)
					draw_board(list, possibilities, True if piece == "k" or piece == "K" else False, startsquarey, startsquarex)
				possibilities = []
				possibilitieson = False
				dragged = False
				drawing = False
				uncolored = False
				arrows_list = []
				if list[squarey][squarex] in all_pieces[list[8][0]%2]:
					startsquarey, startsquarex = squarey, squarex
					piece = list[squarey][squarex]
					if isfinished == False:
						possibilities = possible_squares(list,piece,squarey,squarex)
						possibilitieson = True
					list[squarey][squarex] = 0
					draw_board(list, possibilities, True if piece == "k" or piece == "K" else False, startsquarey, startsquarex)
					blit_on_cursor(piece)
					dragged = True
			
			elif event.type == d.MOUSEMOTION and dragged:
				draw_board(list, possibilities, True if piece == "k" or piece == "K" else False, startsquarey, startsquarex)
				blit_on_cursor(piece)
 
			elif d.mouse.get_pressed(5)[0]==False and dragged:
				if [squarey, squarex] in possibilities:
					if piece == "p" or piece == "P" or list[squarey][squarex] in all_pieces[0] or list[squarey][squarex] in all_pieces[0]:
						list[8][4]=0
					else:
						list[8][4]+=1
					possibilities = []
					possibilitieson = False
					aftermove(list, piece, squarey, squarex, startsquarey, startsquarex)
				else:
					list[startsquarey][startsquarex] = piece
				draw_board(list, possibilities, True if piece == "k" or piece == "K" else False, startsquarey, startsquarex)
				dragged = False


			elif buttons[2]==False and d.mouse.get_pressed(5)[2]==True: # TODO add other colors with right click and alt / ctrl    // custom color
				if dragged:
					list[startsquarey][startsquarex] = piece
					possibilities = []
					possibilitieson = False
					draw_board(list, possibilities, True if piece == "k" or piece == "K" else False, startsquarey, startsquarex)
				dragged = False
				drawing = True
				uncolored = False
				artsquarey, artsquarex = squarey, squarex
				if globals()["bglist"][squarey][squarex]==0: #TODO draw arrows : objects ? -> in order to be removed
					if (squarex+squarey)%2==1: # TODO Premoves
						d.draw.rect(window, darkblue, (squarex*100, squarey*100, 100, 100))
					else:
						d.draw.rect(window, lightblue, (squarex*100, squarey*100, 100, 100))
					globals()["bglist"][squarey][squarex]=1
				elif globals()["bglist"][squarey][squarex]==1:
					if (squarex+squarey)%2==1:
						d.draw.rect(window, dark, (squarex*100, squarey*100, 100, 100))
					else:
						d.draw.rect(window, light, (squarex*100, squarey*100, 100, 100))
					globals()["bglist"][squarey][squarex]=0
				if list[squarey][squarex]!=0:
					window.blit(globals()[list[squarey][squarex]], (100*squarex+globals()[list[squarey][squarex]+"xy"][0],100*squarey+globals()[list[squarey][squarex]+"xy"][1]))
			
			elif event.type == d.MOUSEMOTION and drawing:
				draw_arrow(artsquarey, artsquarex, squarey, squarex)

			elif buttons[2]==True and d.mouse.get_pressed(5)[2]==False: 
				draw_arrow(artsquarey, artsquarex, squarey, squarex)
				drawing = False

			artsquarey, artsquarex = squarey, squarex
			buttons = d.mouse.get_pressed(5)
			d.display.update()
		clock.tick(100)
	d.quit()

def count_combinations(n):
	"""Counts the number of possible move combinations from the beginning of the game after n total moves"""
	pass

def count_positions(n):
	"""Counts the number of possible board positions after n moves"""
	pass

# Start with chess start position
init(start_position)