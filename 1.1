import pygame
import math

# valori da modificare
lato_area = 1000
lato_rettagoli = 500
n_cells = round(pow(lato_area / lato_rettagoli, 2))
matrix_next_board = []

for i in range(n_cells):
    matrix_next_board.append("0")

def n_celle_vive_adiacenti(x, y):
    n_celle_vive = 0
    try:  #sopra sinistra
        if screen.get_at([x-lato_rettagoli, y-lato_rettagoli]) == (255, 255, 255, 255):
            n_celle_vive += 1
    except:
        print(n_celle_vive)

    try:  #sopra
        if screen.get_at([x, y-lato_rettagoli]) == (255, 255, 255, 255):
            n_celle_vive += 1
    except:
        print(n_celle_vive)

    try:  #sopra sinistra
        if screen.get_at([x+lato_rettagoli, y-lato_rettagoli]) == (255, 255, 255, 255):
            n_celle_vive += 1
    except:
        print(n_celle_vive)

    try:  #sinistra
        if screen.get_at([x-lato_rettagoli, y]) == (255, 255, 255, 255):
            n_celle_vive += 1
    except:
        print(n_celle_vive)

    try:  #destra
        if screen.get_at([x+lato_rettagoli, y]) == (255, 255, 255, 255):
            n_celle_vive += 1
    except:
        print(n_celle_vive)

    try:  #sotto sinistra
        if screen.get_at([x-lato_rettagoli, y+lato_rettagoli]) == (255, 255, 255, 255):
            n_celle_vive += 1
    except:
        print(n_celle_vive)

    try:  #sotto
        if screen.get_at([x, y+lato_rettagoli]) == (255, 255, 255, 255):
            n_celle_vive += 1
    except:
        print(n_celle_vive)

    try:  #sotto destra
        if screen.get_at([x+lato_rettagoli, y+lato_rettagoli]) == (255, 255, 255, 255):
            n_celle_vive += 1
    except:
        print(n_celle_vive)

    print("########    " + str(n_celle_vive))

    return n_celle_vive


def next_board():
    for j in range(round(lato_area / lato_rettagoli)):  # cicla sulle colonne
        for i in range(round(lato_area / lato_rettagoli)):  # cicla sulle righe
            x = j*lato_rettagoli
            y = i*lato_rettagoli
            if(n_celle_vive_adiacenti(x, y)) < 2:
                print("indice" + str(indice_cella(i, j)))
                matrix_next_board[indice_cella(i, j)] = 0
                print(matrix_next_board)


def indice_cella(x_, y_):
    return round(y_ * (lato_area / lato_rettagoli) + x_)


def change_state_at(x, y):
    round_x = math.floor((x / lato_rettagoli))
    round_y = math.floor((y / lato_rettagoli))

    if screen.get_at([x, y]) == (255, 255, 255, 255):
        cells[indice_cella(round_x, round_y)].fill(BLACK)
    else:
        cells[indice_cella(round_x, round_y)].fill(WHITE)

    pygame.time.wait(200)


if __name__ == "__main__":

    screen = pygame.display.set_mode((lato_area, lato_area))
    pygame.display.set_caption('Life')
    clock = pygame.time.Clock()
    FPS = 60  # Frames per second.

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    # for i in range(pygame.display.get_window_size()[0]):
    #   print(i)

    # DISEGNA BOARD CON CELLE MORTE
    rects = []
    cells = []

    for j in range(round(lato_area / lato_rettagoli)):  # cicla sulle colonne
        for i in range(round(lato_area / lato_rettagoli)):  # cicla sulle righe
            rects.append(pygame.Rect((lato_rettagoli * i, lato_rettagoli * j), (lato_rettagoli, lato_rettagoli)))
            cells.append(pygame.Surface((lato_rettagoli, lato_rettagoli)))
            cells[round(j * (lato_area / lato_rettagoli) + i)].fill(BLACK)

    # ---

    # MAIN GAMELOOP
    while True:
        clock.tick(FPS)

        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

        if pressed1: #modifica board
            x, y = pygame.mouse.get_pos()
            print(x, y)
            change_state_at(x, y)

        if pressed3: #lancia simulazione
            next_board()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.fill(BLACK)
        for i in range(n_cells):
            screen.blit(cells[i], rects[i])
        pygame.display.update()
