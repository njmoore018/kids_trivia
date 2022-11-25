import pygame
from pygame.locals import *
import json

pygame.init()
fonts = pygame.font.get_fonts()

grade_files = ["questions/grade_k.json","questions/grade_1.json",
    "questions/grade_2.json","questions/grade_3.json","questions/grade_4.json",
    "questions/grade_5.json","questions/grade_6.json","questions/grade_7.json",
    "questions/grade_8.json","questions/grade_9.json","questions/grade_10.json",
    "questions/grade_11.json","questions/grade_12.json",]

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLUE = (150, 200, 255)
BLACK = (0, 0, 0)

pygame.display.set_caption("Kids Trivia")

# Rectangles behind questions.
FIELD_1 = pygame.Rect(((WIDTH / 2) - 350), ((HEIGHT / 2) -150), 300, 150)
FIELD_2 = pygame.Rect(((WIDTH / 2) + 50), ((HEIGHT / 2) - 150), 300, 150)
FIELD_3 = pygame.Rect(((WIDTH / 2) - 350), ((HEIGHT / 2) + 75), 300, 150)
FIELD_4 = pygame.Rect(((WIDTH / 2) + 50), ((HEIGHT / 2) + 75), 300, 150)

# Bar to show money ammount  
balance = pygame.Rect(25, (HEIGHT // 1.2), 10, 20)
money_levels = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 500000, 1000000]

def banner(text, size, color):
    """
    Takes text and size and color, and returns it in a format so it can be shown on screen.
    """
    sysfont = pygame.font.get_default_font()
    font = pygame.font.SysFont(None, 48)
    img = font.render(sysfont, True, BLACK)
    rect = img.get_rect()
    pygame.draw.rect(img, color, rect, 1)

    font1 = pygame.font.SysFont('chalkduster.ttf', size)
    return font1.render(text, True, color)

def get_grade():
    """
    Displays all grade choices and returns the index of the one you click on.
    """
    instructions = banner("Select grade difficulty to begin", 30, BLACK)
    count = 1
    WIN.fill(WHITE)
    done  = False
    grade_list =  [banner("k", 18, BLACK),  banner("1", 18, BLACK),
    banner("2", 18, BLACK),  banner("3", 18, BLACK),  banner("4", 18, BLACK),
    banner("5", 18, BLACK),  banner("6", 18, BLACK),  banner("7", 18, BLACK),
    banner("8", 18, BLACK),  banner("9", 18, BLACK), banner("10", 18, BLACK),
    banner("11", 18, BLACK), banner("12", 18, BLACK)]
    field_list = [pygame.Rect(270, 250, 40, 40), pygame.Rect(300, 250, 40, 40),
    pygame.Rect(0, 250, 40, 40), pygame.Rect(30, 250, 40, 40),
    pygame.Rect(60, 250, 40, 40), pygame.Rect(90, 250, 40, 40),
    pygame.Rect(40, 250, 40, 40), pygame.Rect(40, 250, 40, 40),
    pygame.Rect(140, 250, 40, 40), pygame.Rect(150, 250, 40, 40),
    pygame.Rect(180, 250, 40, 40), pygame.Rect(210, 250, 40, 40),
    pygame.Rect(240, 250, 40, 40),]

    WIN.blit(instructions, ((WIDTH //2) - (instructions.get_width() // 2), 50))
    for i in range(len(field_list)):
            field = field_list[i]
            field.x = count * 60
            pygame.draw.rect(WIN, BLUE, field)
            WIN.blit(grade_list[i], (field.x + 15, field.y + 15))
            count += 1
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for i in range(len(field_list)):
                    field = field_list[i]
                    if field.collidepoint(pos):
                        grade_choice = i
                        done = True
                        return grade_choice

        pygame.display.update()




def draw_window(question, answer_list, points):
    " "
    curr_money = str(money_levels[points])
    min_money = banner("$0", 18, BLACK)
    max_money = banner("$1,000,000", 18, BLACK)
    quest = banner(question, 40, BLACK)
    your_money = banner((f"${curr_money}"), 18, BLACK)

    # Answer options
    a_1 = banner(answer_list[0], 25, BLACK)
    a_2 = banner(answer_list[1], 25, BLACK)
    a_3 = banner(answer_list[2], 25, BLACK)
    a_4 = banner(answer_list[3], 25, BLACK)


    WIN.fill(WHITE)
    
    # Draws question at top of screen
    WIN.blit(quest, ((WIDTH // 2) - (quest.get_width() // 2), 20))
    
    # Draws answers over rectangles
    pygame.draw.rect(WIN, BLUE, FIELD_1)
    WIN.blit(a_1, (FIELD_1.x + (FIELD_1.width // 2) - (a_1.get_width() // 2), (FIELD_1.y + (FIELD_1.height // 2 - (a_1.get_height())))))
    pygame.draw.rect(WIN, BLUE, FIELD_2)
    WIN.blit(a_2, (FIELD_2.x + (FIELD_2.width // 2) - (a_2.get_width() // 2), (FIELD_2.y + (FIELD_2.height // 2 - (a_2.get_height())))))
    pygame.draw.rect(WIN, BLUE, FIELD_3)
    WIN.blit(a_3, (FIELD_3.x + (FIELD_2.width // 2) - (a_3.get_width() // 2), (FIELD_3.y + (FIELD_3.height // 2 - (a_3.get_height())))))
    pygame.draw.rect(WIN, BLUE, FIELD_4)
    WIN.blit(a_4, (FIELD_4.x + (FIELD_2.width // 2) - (a_4.get_width() // 2), (FIELD_4.y + (FIELD_4.height // 2 - (a_4.get_height())))))
    
    # draws $0 and $1000000 with a bar in the middle to show where you are at  
    pygame.draw.rect(WIN, BLACK, balance)
    WIN.blit(min_money, (20, 450))
    WIN.blit(max_money, (20, 50))
    WIN.blit(your_money, (balance.x + balance.width + 10, balance.y))

    pygame.display.update()

def play_again(text, points):
    screen_text = banner(text, 40, BLACK)
    yes = banner("PLAY AGAIN", 18, BLACK)
    no = banner("QUIT", 18, BLACK)
    curr_money = str(money_levels[points])
    your_money = banner((f"End Score: ${curr_money}"), 40, BLACK)
    
    WIN.fill(WHITE)
    WIN.blit(screen_text, ((WIDTH // 2) - (screen_text.get_width() // 2), 20))
    WIN.blit(your_money, ((WIDTH // 2) - (your_money.get_width() // 2), 50))
    pygame.draw.rect(WIN, BLUE, FIELD_1)
    WIN.blit(yes, (FIELD_1.x + (FIELD_1.width // 2) - (yes.get_width() // 2), (FIELD_1.y + (FIELD_1.height // 2 - (yes.get_height())))))
    pygame.draw.rect(WIN, BLUE, FIELD_2)
    WIN.blit(no, (FIELD_2.x + (FIELD_2.width // 2) - (no.get_width() // 2), (FIELD_2.y + (FIELD_2.height // 2 - (no.get_height())))))
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if FIELD_1.collidepoint(pos):
                    done = True
                    answer = True
                    return answer
                elif FIELD_2.collidepoint(pos):
                    done = True
                    answer = False
                    return answer
                


        pygame.display.update()
