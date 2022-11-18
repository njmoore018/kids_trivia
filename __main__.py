from func_file import *



def main():

    end_screen = ""
    grade = get_grade()

    file = grade_files[grade]
    lines_text = open(file)
    lines_list = json.load(lines_text)
    line_num = 0
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
            if line_num < len(lines_list) - 1:
                line_num += 1
            else:
                run = False
                end_screen = "YOU WIN!"
                balance.height -= (balance.height - 20)
                balance.y = (HEIGHT // 1.2)

            points += 1
            # money bar goes up  
            balance.height += 20
            balance.y -= 20
        elif answer in answers and answers[answer] != "correct":
            balance.height -= (balance.height - 20)
            balance.y = (HEIGHT // 1.2)
            run = False
            end_screen = "You loose"


        draw_window(question, a_list, points)
    again = play_again(end_screen, points)
    if again:
        main()
    

if __name__ == "__main__":
    main()

pygame.quit()