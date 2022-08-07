def chess_board(FEN_string):
    """Makes the FEN string given a list of 8 lists with each a length of 8, representing the chessboard when printed out"""
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
    if __name__=="__main__":
        print("\n")
        for y in range(8):
            for x in range(8):
                print(position_list[y][x], end="   ")
            print("\n")
        print("\n")
        
        


chess_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")