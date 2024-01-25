import pygame
import sys

def check(mas,sign):
    zeroes = 0
    for row in mas:
        zeroes+=row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
            return sign
    elif mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
            return sign
    if zeroes==0:
        return "Oops, no win"
    return False

pygame.init()
size_block = 150
margin = 20
width = heigth = size_block*3 + margin*4

size_window = (width, heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Tic-Tac-Toe")
img = pygame.image.load('icon.png')
pygame.display.set_icon(img)

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0]*3 for i in range(3)]
query = 0
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block+margin)
            row = y_mouse // (size_block+margin)
            if mas[row][col] == 0:
                if query%2 == 0:
                    mas[row][col] = "x"
                else:
                    mas[row][col] = "o"
                query +=1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0]*3 for i in range(3)]
            query = 0
            screen.fill(black)

    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == "x":
                    color = red
                elif mas[row][col] == "o":
                    color = green
                else:
                    color = white
                x = col*size_block + (col+1)*margin
                y = row*size_block + (row+1)*margin
                pygame.draw.rect(screen, color, (x,y,size_block,size_block))
                if color == red:
                    pygame.draw.line(screen, white, (x+7, y+7), (x+size_block-7, y+size_block-7), 4)
                    pygame.draw.line(screen, white, (x+size_block-7, y+7), (x+7, y+size_block-7), 4)
                elif color == green:
                    pygame.draw.circle(screen, white, (x+size_block//2, y+size_block//2), size_block//2-3, 4)
    if (query-1)%2==0:
        game_over = check(mas,"x")
    else:
        game_over = check(mas,"o")
    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont("arial", 100)
        text1 = font.render(game_over, True, white)
        text_pos = text1.get_rect()
        text_x = screen.get_width()/2 -text_pos.width / 2
        text_y = screen.get_height()/2 -text_pos.height / 2
        screen.blit(text1, [text_x, text_y])

    pygame.display.update()
