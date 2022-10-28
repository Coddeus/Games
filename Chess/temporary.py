# Settings 


# Types

# Frame, tabs, then :

def settings_yesno():
    pass

def settings_dropdown():
	pass

def settings_textinput():
	pass

def settings_picinput():
	pass

def settings_numinput():
	pass

def settings_colorpicker():
	pass

def settings_title():
    pass


"""fav_colors = {
    "color_theme": [["dark"], [d.Color(w/e)]]
    "efzhbfez": [["hbv", "hbfzfhzf"], [d.Color(w/e1), d.Color(w/e2)]]
}"""


#-----------------------------------------------------------------

"""#General
	"remember_settings": True,
	"settings_filepath": "",
	"show_shortcuts": True,
	"color_theme": "dark",
	"share_quote": True,
	"sharedquote_rate": 600,
	"default_settings_tab": 'Latest',
	"validate_before_closing": True,
	"say_quotebye": True,
	"say_goodbye": True,

	# Shortcuts
	"settings": "s",
	"flip": "f",
	"settings_tabs": ["1", "2", "3", "4", "5", "6"],
	"return": "esc",
	"minimize": "m",

	# Display
	"fullscreen": True,
	"preferred_screen": 1,
	"resolution": [0, 0],
	"framerate": 60,

	# Customize
	"show_possible_squares": True,
	"possible_squares_indicator": "disk",
	"possible_squares_color": "grey", # RGB
	"board_scale": [800, 800],
	"white_square_color": "a",
	"black_square_color": "z",
	"white_square_color_alt": "e",
	"black_square_color_alt": "r",
	"white_square_color_ctrl": "t",
	"black_square_color_ctrl": "y",
	"white_square_color_shft": "u",
	"black_square_color_shft": "i",
	"pieces_scale": 80,
	"pieces_png": ["default"]*16, # Different pawns ?!?! Why not :D
	"endofgame_animation": None
	# + Options to play with keyboard, blindfolded

	# ……… (accounts management "link_accounts" "unlink_accounts" …)

	# Contact/Feedback
	# + Contact info
	# + Feedback score (/+ input (/+ form))"""




#  orgsettings[n][m] = [id, name, type, value]
#
orgsettings = [ # Order settings here
	[       # Tab 1
        ["show_shortcuts", "Show shortcut when hovering", "YN", True],
        ["default_settings_tab", "Default Settings Tab", "DD", "Latest"],
        ["validate_before_closing", "Confirm when exiting", "YN", True],
        ["say_goodbye", "Get a goodbye message", "YN", True]
    ],  
    [       # Tab 2

    ],  
    [       # Tab 3

    ],
    [       # Tab 4
	    "show_possible_squares"
    ],
    [       # Tab 5
    
    ],
    [       # Tab 6
    
    ]

] 


settings_types = {
    "YN": settings_yesno(),
    "DD": settings_dropdown(),
    "TI": settings_textinput(),
    "PI": settings_picinput(),
    "NI": settings_numinput(),
    "CP": settings_colorpicker(),
    "TT": settings_title()
} # ADD TITLES TO TIDY UP





"""
# Settings

def settingsoptions(mousex, mousey):
	global selecteddropdown
	global settings_info
	global prop
	clicked = True if (buttons[0]==False and d.mouse.get_pressed(5)[0]==True) else False

	if selectedtab[0]==0:

		if clicked:
			if selecteddropdown!="":
				prop = dropdowns[selecteddropdown].innitin(mousex, mousey)
			else:
				prop = False, False
		dropdownisselected = False

		if selecteddropdown!="" and prop[0]:
			settings_info[selecteddropdown] = prop[1]
		
		elif 690<=mousex<=1310:

			if 120<=mousey<=170:
				d.draw.rect(window, grey2, (690, 120, 620, 50), 0, 10)
				if clicked and selecteddropdown != "default_settings_tab":
					selecteddropdown = "default_settings_tab"
					dropdownisselected = True

			elif 180<=mousey<=230:
				d.draw.rect(window, grey2, (690, 180, 620, 50), 0, 10)
				if buttons[0]==False and d.mouse.get_pressed(5)[0]==True:
					settings_info["show_shortcuts"] = not settings_info["show_shortcuts"]
			
			elif 240<=mousey<=290:
				d.draw.rect(window, grey2, (690, 240, 620, 50), 0, 10)
				if buttons[0]==False and d.mouse.get_pressed(5)[0]==True:
					settings_info["say_goodbye"] = not settings_info["say_goodbye"]
			
			elif 300<=mousey<=350:
				d.draw.rect(window, grey2, (690, 300, 620, 50), 0, 10)
				if buttons[0]==False and d.mouse.get_pressed(5)[0]==True:
					settings_info["validate_before_closing"] = not settings_info["validate_before_closing"]
		
		if clicked and not dropdownisselected:
			selecteddropdown = ""
		
		window.blit(fonts[1].render("Show shortcut when hovering", True, lightestgrey), (700,190))
		settings_yesno(190, settings_info["show_shortcuts"])
		window.blit(fonts[1].render("Get a goodbye message", True, lightestgrey), (700,250))
		settings_yesno(250, settings_info["say_goodbye"])
		window.blit(fonts[1].render("Confirm exiting", True, lightestgrey), (700,310))
		settings_yesno(310, settings_info["validate_before_closing"])
		window.blit(fonts[1].render("Default Settings Tab", True, lightestgrey), (700,130))
		settings_dropdown(130, "default_settings_tab")

	elif selectedtab[0]==1:
		pass

	elif selectedtab[0]==2:
		pass

	elif selectedtab[0]==3:
		if 690<=mousex<=1310:
			if 120<=mousey<=170:
				d.draw.rect(window, grey2, (690, 120, 620, 50), 0, 10)
				if buttons[0]==False and d.mouse.get_pressed(5)[0]==True:
					settings_info["show_possible_squares"] = not settings_info["show_possible_squares"]
		window.blit(fonts[1].render("Show possible squares", True, lightestgrey), (700,130))
		settings_yesno(130, settings_info["show_possible_squares"])
		
	elif selectedtab[0]==4:
		pass

	elif selectedtab[0]==5:
		pass

def settings_yesno(y, bol):
	if bol==True:
		window.blit(settings_yes, (1250, y+5))
	else:
		window.blit(settings_no, (1250, y+5))

def settings_dropdown(y, parameter):
	global settings_info
	llist = dropdowns[parameter].list
	clicked = True if (buttons[0]==False and d.mouse.get_pressed(5)[0]==True) else False

	if True:
		pass

	if selecteddropdown=="":
		d.draw.rect(window, darkergrey, (1100, y-2, 200, 35), 0, 5)
		window.blit(fonts[0].render(settings_info[parameter], True, lightergrey), (1110,y+2))
		window.blit(dropdown_isclosed, (1275, y+10))

	else:
		d.draw.rect(window, darkergrey, (1100, y-2, 200, 35*len(llist)), 0, 5)
		window.blit(fonts[0].render(settings_info[parameter], True, lightergrey), (1110,y+2))
		window.blit(dropdown_isopen, (1275, y+10))
		dropdownlist = llist[:]
		dropdownlist.remove(settings_info[parameter])
		for i, j in enumerate(dropdownlist, 1):
			window.blit(fonts[0].render(j, True, lightgrey), (1110,y+2+35*i))

def settings_input(y, current):
	pass

def settings_colorpicker(y, current):
	pass

def initsettings(): # Miscellaneous : when op. settings, go to General/latest tab
	global window
	global running
	global display
	global buttons
	global selectedtab
	global settings_info
	global selecteddropdown
	d.display.set_icon(settingsicon)
	d.display.set_caption('Chess - Settings')
	if not settings_info["default_settings_tab"]=='Latest':
		selectedtab[0]=settingstabs.index(settings_info["default_settings_tab"])
	while running and display == "settings":
		for event in d.event.get():

			if event.type == d.QUIT:
				running = False

			elif event.type == d.KEYDOWN and event.key == d.K_ESCAPE:
				display = "local"
			
			elif event.type == d.KEYDOWN and not anythingisselected and event.key in [d.K_1, d.K_2, d.K_3, d.K_4, d.K_5, d.K_6]:

				selectedtab[0] = event.key-49

			mousex, mousey = d.mouse.get_pos()
			draw_frame()
			d.draw.rect(window, darkgrey, (0,0,654,1080), 0, 0)
			d.draw.rect(window, lightgrey, (650,50,8,980), 0, 15)
			
			if 350<=mousex<=650:
				if 100<=mousey<=400:
					for i in range(6):
						if 101+50*i<=mousey<=150+50*i:
							selectedtab[1] = i
							d.draw.rect(window, darkergrey, (360,100+50*i,280,50), 0, 13)
							if d.mouse.get_pressed(5)[0]==True and buttons[0]==False:
								selectedtab[0] = i

			window.blit(fonts[2].render(settingstabs[selectedtab[0]], True, lightestergrey), (750,30))

			for i in range(6):
				if selectedtab[0]==i:
					img = fonts[0].render(settingstabs[i], True, lightestergrey)
				elif selectedtab[1]==i:
					img = fonts[0].render(settingstabs[i], True, lightestgrey)
				else:
					img = fonts[0].render(settingstabs[i], True, lightergrey)
				window.blit(img, (380,110+50*i))
			selectedtab[1]=-1

			settingsoptions(mousex, mousey)

			d.display.update()
			buttons = d.mouse.get_pressed(5)
		clock.tick(60)"""