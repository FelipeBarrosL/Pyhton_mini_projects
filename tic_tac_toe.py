from curses.ascii import isdigit
import random as rd
import time
import os

def print_table():
    os.system('cls')
    print("----------------JOGO DA VELHA-------------")
    print(f' {array_game[0][0]} | {array_game[0][1]} | {array_game[0][2]}         -->          1 | 2 | 3 ')
    print('___|___|___        -->         ___|___|___')
    print(f' {array_game[1][0]} | {array_game[1][1]} | {array_game[1][2]}         -->          4 | 5 | 6 ')
    print('___|___|___        -->         ___|___|___')
    print(f' {array_game[2][0]} | {array_game[2][1]} | {array_game[2][2]}         -->          7 | 8 | 9 ')
    print('   |   |           -->            |   |   ')

def new_choice():
    user_entry = input("Digite a próxima posição: ")
    while user_entry.isdigit() == False or int(user_entry) <1 or int(user_entry) >9:
        print("Valor inválido!!!")
        user_entry = input("Digite a próxima posição: ")
    return int(user_entry)

def def_array(pos, user):
    a = 'X'
    if user == True:
        a = '0'
    
    if pos >=1 and pos <=3:
        array_game[0][pos-1] = a
    elif pos >=4 and pos <=6:
        array_game[1][pos-4] = a
    else:
        array_game[2][pos-7] = a

def check_win():
    for i in ['X','0']:
        #Check for horizontal wins
        if array_game[0][0] == array_game[0][1] == array_game[0][2] == i: return i
        elif array_game[1][0] == array_game[1][1] == array_game[1][2] == i: return i
        elif array_game[2][0] == array_game[2][1] == array_game[2][2] == i: return i
        #Check for vertical wins
        elif array_game[0][0] == array_game[1][0] == array_game[2][0] == i: return i
        elif array_game[0][1] == array_game[1][1] == array_game[2][1] == i: return i
        elif array_game[0][2] == array_game[1][2] == array_game[2][2] == i: return i          
        #Check for diagonal wins
        elif array_game[0][0] == array_game[1][1] == array_game[2][2] == i: return i
        elif array_game[0][2] == array_game[1][1] == array_game[2][0] == i: return i
        else: continue
    #No win
    return None

def game(mode):
    print_table()
    #Human play
    x = new_choice()
    while x in positions:
        print("Posição já escolhida! ")
        x = new_choice()
    positions.append(x)
    def_array(x, True)
    print_table()
    win = check_win()
    if win != None: return win
    if len(positions) == 9: 
        win = 'z'
        return win
    
    if mode != 'pc':
        x = new_choice()
        while x in positions:
            print("Posição já escolhida! ")
            x = new_choice()
        positions.append(x)
        def_array(x, False)
        print_table()
        win = check_win()
        if win != None: return win
        
    else:   
        #PC play
        time.sleep(1)
        x = rd.randrange(1,10)
        while x in positions:
            x = rd.randrange(1,10)
        positions.append(x)
        def_array(x, False)
        print_table()
        win = check_win()
        if win != None: return win

play = ''
user_wins = 0
other_wins = 0
draw = 0

while play != 'não':

    array_game = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    win = None
    positions = []
    game_mode = input("Digite PC para jogar contra o computador: ").lower()
        
    while win == None:
        win = game(game_mode)
                        
    if win == '0':
        user_wins += 1
        print("\nJogador 0 ganhou!")
    elif win == 'X':
        other_wins += 1
        print("\nJogador X ganhou!")
    else:
        draw += 1
        print("\nDeu Velha!")

    print(f"Numero de vitorias 0: {user_wins}")
    print(f"Numero de vitorias X: {other_wins}")
    print(f"Numero de empates: {draw}")

    play = input("Deseja jogar novamente? ").lower()


