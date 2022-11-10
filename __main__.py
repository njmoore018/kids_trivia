import json
import pygame



def main():
    grade = int(input("Enter grade level (0-12): "))
    grade_files = ["questions/grade_k.json","questions/grade_1.json",
    "questions/grade_2.json","questions/grade_3.json","questions/grade_4.json",
    "questions/grade_5.json","questions/grade_6.json","questions/grade_7.json",
    "questions/grade_8.json","questions/grade_9.json","questions/grade_10.json",
    "questions/grade_11.json","questions/grade_12.json",]
    file = grade_files[grade]

    lines_text = open(file)
    lines_list = json.load(lines_text)


    playing = True
    points = 0
    line_num = 0

    while playing:
        line = lines_list[line_num]
        question = line[0]
        answers = line[1]
        answer_keys = answers.keys()

        pygame

        print(question)
        for i in answer_keys:
            print(i)

        answer = input("answer: ")
        print(answers[answer])
        if answers[answer] == "correct":
            points += 1
        else:
            try_again = input("play again (y/n): ")
            if try_again != 'y':
                playing = False
            else:
                line_num = -1

        line_num += 1


if __name__ == "__main__":
    main()