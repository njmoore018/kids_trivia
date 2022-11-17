import json
import pygame



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

def draw_window(question, answer_list):
    " "
    min_money = banner("$0", 18, BLACK)
    max_money = banner("$1,000,000", 18, BLACK)
    quest = banner(question, 40, BLACK)

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

    pygame.display.update()


def main():
    grade = int(input("Enter grade level (0-12): "))

    file = grade_files[grade]
    lines_text = open(file)
    lines_list = json.load(lines_text)
    line_num = 0

    money_levels = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 500000, 1000000]
    points = 0

    run = True

    while run:
        answer = None
        line = lines_list[line_num]
        question = line[0]
        answers = line[1]
        answer_keys = answers.keys()
        a_list = []
        for i in answer_keys:
            a_list.append(i)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if FIELD_1.collidepoint(pos):
                    answer = a_list[0]
                elif FIELD_2.collidepoint(pos):
                    answer = a_list[1]
                elif FIELD_3.collidepoint(pos):
                    answer = a_list[2]
                elif FIELD_4.collidepoint(pos):
                    answer = a_list[3]
        if answer in answers and answers[answer] == "correct":
            # next question
            line_num += 1
            # money bar goes up  
            balance.height += 20
            balance.y -= 20

        draw_window(question, a_list)

if __name__ == "__main__":
    main()
pygame.quit()