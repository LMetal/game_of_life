import pygame
import math

# valori da modificare COSTANTI
LATO_AREA = 900
LATO_RETTANGOLI = 20
INPUT_SPEED = 100

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


n_cells = round(pow(LATO_AREA / LATO_RETTANGOLI, 2))
matrix_board = []


for i in range(n_cells):
    matrix_board.append(0)



def n_celle_vive_adiacenti(x, y):
    n_celle_vive = 0
    try:  # sopra sinistra
        if screen.get_at([x - LATO_RETTANGOLI, y - LATO_RETTANGOLI]) == WHITE:
            n_celle_vive += 1
    except:
        pass

    try:  # sopra
        if screen.get_at([x, y - LATO_RETTANGOLI]) == WHITE:
            n_celle_vive += 1
    except:
        pass

    try:  # sopra sinistra
        if screen.get_at([x + LATO_RETTANGOLI, y - LATO_RETTANGOLI]) == WHITE:
            n_celle_vive += 1
    except:
        pass

    try:  # sinistra
        if screen.get_at([x - LATO_RETTANGOLI, y]) == WHITE:
            n_celle_vive += 1
    except:
        pass

    try:  # destra
        if screen.get_at([x + LATO_RETTANGOLI, y]) == WHITE:
            n_celle_vive += 1
    except:
        pass

    try:  # sotto sinistra
        if screen.get_at([x - LATO_RETTANGOLI, y + LATO_RETTANGOLI]) == WHITE:
            n_celle_vive += 1
    except:
        pass

    try:  # sotto
        if screen.get_at([x, y + LATO_RETTANGOLI]) == WHITE:
            n_celle_vive += 1
    except:
        pass

    try:  # sotto destra
        if screen.get_at([x + LATO_RETTANGOLI, y + LATO_RETTANGOLI]) == WHITE:
            n_celle_vive += 1
    except:
        pass

    #print(str(x) + " " + str(y) + " ###### " + str(n_celle_vive))

    return n_celle_vive


def next_board():
    for j in range(round(LATO_AREA / LATO_RETTANGOLI)):  # cicla sulle colonne
        for i in range(round(LATO_AREA / LATO_RETTANGOLI)):  # cicla sulle righe
            x = j * LATO_RETTANGOLI
            y = i * LATO_RETTANGOLI

            # regole
            if screen.get_at([x, y]) == WHITE and n_celle_vive_adiacenti(x, y) < 2:  # cella viva, poche celle
                matrix_board[indice_cella(i, j)] = 0

            elif screen.get_at([x, y]) == WHITE and n_celle_vive_adiacenti(x, y) > 3:  # troppe celle
                matrix_board[indice_cella(i, j)] = 0

            elif n_celle_vive_adiacenti(x, y) == 3:  # giuste
                matrix_board[indice_cella(i, j)] = 1

    #for i in matrix_board:
    #    if i == 0:
            #print("muore")
    #    else:
            #print("vive")

    for j in range(round(LATO_AREA / LATO_RETTANGOLI)):  # cicla sulle colonne
        for i in range(round(LATO_AREA / LATO_RETTANGOLI)):  # cicla sulle righe
            x = j * LATO_RETTANGOLI
            y = i * LATO_RETTANGOLI
            if matrix_board[round(i * (LATO_AREA / LATO_RETTANGOLI) + j)] == 1:
                cells[round(j * (LATO_AREA / LATO_RETTANGOLI) + i)].fill(WHITE)
            else:
                cells[round(j * (LATO_AREA / LATO_RETTANGOLI) + i)].fill(BLACK)


def indice_cella(x_, y_):
    return round(y_ * (LATO_AREA / LATO_RETTANGOLI) + x_)


def change_state_at(x, y, loop):
    print(loop)
    round_x = math.floor((x / LATO_RETTANGOLI))
    round_y = math.floor((y / LATO_RETTANGOLI))

    if screen.get_at([x, y]) == WHITE:    # se la cella cliccata è viva, morta
        cells[indice_cella(round_x, round_y)].fill(BLACK)
        matrix_board[round(round_x*LATO_AREA/LATO_RETTANGOLI) + round_y] = 0


    if screen.get_at([x, y]) == BLACK :  # se la cella cliccata è morta, viva
        cells[indice_cella(round_x, round_y)].fill(WHITE)
        matrix_board[round(round_x*LATO_AREA/LATO_RETTANGOLI) + round_y] = 1

    pygame.time.wait(INPUT_SPEED)



def restart():  # every cell to 
    for j in range(round(LATO_AREA / LATO_RETTANGOLI)):  # cicla sulle colonne
        for i in range(round(LATO_AREA / LATO_RETTANGOLI)):  # cicla sulle righe
            cells[round(j * (LATO_AREA / LATO_RETTANGOLI) + i)].fill(BLACK)
            matrix_board[round(i*LATO_AREA/LATO_RETTANGOLI) + j] = 0
    

if __name__ == "__main__":

    screen = pygame.display.set_mode((LATO_AREA, LATO_AREA))
    pygame.display.set_caption('Game of Life')
    clock = pygame.time.Clock()
    FPS = 60  # Frames per second.

    # for i in range(pygame.display.get_window_size()[0]):
    #   #print(i)

    # DISEGNA BOARD CON CELLE MORTE
    rects = []
    cells = []

    for j in range(round(LATO_AREA / LATO_RETTANGOLI)):  # cicla sulle colonne
        for i in range(round(LATO_AREA / LATO_RETTANGOLI)):  # cicla sulle righe
            rects.append(pygame.Rect((LATO_RETTANGOLI * i, LATO_RETTANGOLI * j), (LATO_RETTANGOLI, LATO_RETTANGOLI)))
            cells.append(pygame.Surface((LATO_RETTANGOLI, LATO_RETTANGOLI)))
            cells[round(j * (LATO_AREA / LATO_RETTANGOLI) + i)].fill(BLACK)

    # ---

    # MAIN GAMELOOP
    while True:
        clock.tick(FPS)

        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

        # D = 100
        # print(pygame.key.get_pressed()[100]) 

        if pressed1:  # modifica board
            x, y = pygame.mouse.get_pos()
            change_state_at(x, y, 0)


                   
        if pygame.key.get_pressed()[100] or pressed3:  # lancia simulazione tasto D
            next_board()
            #pygame.time.wait(200)

        if pressed2: # empty board
            restart()
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.fill(BLACK)
        for i in range(n_cells):
            screen.blit(cells[i], rects[i])
        pygame.display.update()
