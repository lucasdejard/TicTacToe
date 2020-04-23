import os
init = 9
x1 = " "
x2 = " "
x3 = " "
x4 = " "
x5 = " "
x6 = " "
x7 = " "
x8 = " "
x9 = " "
valid = 0
draw = 0
rep = 0
ans = "y"
listss = [[x1, x2, x3], [x4, x5, x6], [x7, x8, x9]]
select = ""


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def initprt():
    print("""
    T_I_C_T_A_C_T_O_E
    _________        _________
    _|{}|{}|{}|_        _|1|2|3|_
    _|{}|{}|{}|_        _|4|5|6|_
    _|{}|{}|{}|_        _|7|8|9|_
    -|-|-|-|-        -|-|-|-|-
    """"".format(listss[0][0], listss[0][1], listss[0][2], listss[1][0], listss[1][1], listss[1][2], listss[2][0],
                 listss[2][1], listss[2][2]))
    return 0


initprt()

while init > 0:
    initprt()
    'chamada da função'
    if init % 2 != 0:
        while valid == 0:
            print("JOGADOR XXX")
            print("selecione um numero válido para jogar:")
            select = input()
            if select == "1" and listss[0][0] != "X" and listss[0][0] != "O":
                valid = 1
                listss[0][0] = "X"
            if select == "2" and listss[0][1] != "X" and listss[0][1] != "O":
                valid = 1
                listss[0][1] = "X"
            if select == "3" and listss[0][2] != "X" and listss[0][2] != "O":
                valid = 1
                listss[0][2] = "X"
            if select == "4" and listss[1][0] != "X" and listss[1][0] != "O":
                valid = 1
                listss[1][0] = "X"
            if select == "5" and listss[1][1] != "X" and listss[1][1] != "O":
                valid = 1
                listss[1][1] = "X"
            if select == "6" and listss[1][2] != "X" and listss[1][2] != "O":
                valid = 1
                listss[1][2] = "X"
            if select == "7" and listss[2][0] != "X" and listss[2][0] != "O":
                valid = 1
                listss[2][0] = "X"
            if select == "8" and listss[2][1] != "X" and listss[2][1] != "O":
                valid = 1
                listss[2][1] = "X"
            if select == "9" and listss[2][2] != "X" and listss[2][2] != "O":
                valid = 1
                listss[2][2] = "X"
    valid = 0
    if init % 2 == 0:
        while valid == 0:

            '''print("JOGADOR OOO")
            print("selecione um numero válido para jogar:")

            select = input()
            if select == "1" and listss[0][0] != "X" and listss[0][0] != "O":
                valid = 1
                listss[0][0] = "O"
            if select == "2" and listss[0][1] != "X" and listss[0][1] != "O":
                valid = 1
                listss[0][1] = "O"
            if select == "3" and listss[0][2] != "X" and listss[0][2] != "O":
                valid = 1
                listss[0][2] = "O"
            if select == "4" and listss[1][0] != "X" and listss[1][0] != "O":
                valid = 1
                listss[1][0] = "O"
            if select == "5" and listss[1][1] != "X" and listss[1][1] != "O":
                valid = 1
                listss[1][1] = "O"
            if select == "6" and listss[1][2] != "X" and listss[1][2] != "O":
                valid = 1
                listss[1][2] = "O"
            if select == "7" and listss[2][0] != "X" and listss[2][0] != "O":
                valid = 1
                listss[2][0] = "O"
            if select == "8" and listss[2][1] != "X" and listss[2][1] != "O":
                valid = 1
                listss[2][1] = "O"
            if select == "9" and listss[2][2] != "X" and listss[2][2] != "O":
                valid = 1
                listss[2][2] = "O"
            '''
            a, b, c = 0, 0, 0
            d, e, f = 0, 1, 2
            i = 6
            while i > 0:

                while i > 3:
                    i -= 1
                    if valid == 0 and listss[a][d] == listss[c][f] == "O" or\
                            listss[a][d] == listss[b][e] == "O" or listss[c][f] == listss[b][e] == "O":
                        if valid == 0 and listss[a][d] == " ":
                            listss[a][d] = "O"
                            valid = 1
                        if valid == 0 and listss[b][e] == " ":
                            listss[b][e] = "O"
                            valid = 1
                        if valid == 0 and listss[c][f] == " ":
                            listss[c][f] = "O"
                            valid = 1
                    a, b, c = a + 1, b + 1, c + 1
                d, e, f, = 0, 0, 0

                while i > 0:
                    a, b, c = 0, 1, 2
                    i -= 1
                    if valid == 0 and listss[a][d] == listss[c][f] == "O" or\
                            listss[a][d] == listss[b][e] == "O" or listss[c][f] == listss[b][e] == "O":
                        if valid == 0 and listss[a][d] == " ":
                            listss[a][d] = "O"
                            valid = 1
                        if valid == 0 and listss[b][e] == " ":
                            listss[b][e] = "O"
                            valid = 1
                        if valid == 0 and listss[c][f] == " ":
                            listss[c][f] = "O"
                            valid = 1
                    d, e, f = d + 1, e + 1, f + 1

            a, b, c = 0, 0, 0
            d, e, f = 0, 1, 2
            i = 6
            while i > 0:

                while i > 3:
                    i -= 1
                    if valid == 0 and listss[a][d] == listss[c][f] == "X" or \
                            listss[a][d] == listss[b][e] == "X" or listss[c][f] == listss[b][e] == "X":
                        if valid == 0 and listss[a][d] == " ":
                            listss[a][d] = "O"
                            valid = 1
                        if valid == 0 and listss[b][e] == " ":
                            listss[b][e] = "O"
                            valid = 1
                        if valid == 0 and listss[c][f] == " ":
                            listss[c][f] = "O"
                            valid = 1
                    a, b, c = a + 1, b + 1, c + 1
                d, e, f, = 0, 0, 0

                while i > 0:
                    a, b, c = 0, 1, 2
                    i -= 1
                    if valid == 0 and listss[a][d] == listss[c][f] == "O" or \
                            listss[a][d] == listss[b][e] == "O" or listss[c][f] == listss[b][e] == "O":
                        if valid == 0 and listss[a][d] == " ":
                            listss[a][d] = "O"
                            valid = 1
                        if valid == 0 and listss[b][e] == " ":
                            listss[b][e] = "O"
                            valid = 1
                        if valid == 0 and listss[c][f] == " ":
                            listss[c][f] = "O"
                            valid = 1
                    d, e, f = d + 1, e + 1, f + 1

            a, b, c = 0, 0, 0
            d, e, f = 0, 1, 2
            i = 6
            while i > 0:

                while i > 3:
                    i -= 1
                    if valid == 0 and listss[a][d] == listss[c][f] != " " or\
                            listss[a][d] == listss[b][e] != " " or listss[c][f] == listss[b][e] != " ":
                        if valid == 0 and listss[a][d] == " ":
                            listss[a][d] = "O"
                            valid = 1
                        if valid == 0 and listss[b][e] == " ":
                            listss[b][e] = "O"
                            valid = 1
                        if valid == 0 and listss[c][f] == " ":
                            listss[c][f] = "O"
                            valid = 1
                    a, b, c = a + 1, b + 1, c + 1
                d, e, f, = 0, 0, 0

                while i > 0:
                    a, b, c = 0, 1, 2
                    i -= 1
                    if valid == 0 and listss[a][d] == listss[c][f] != " " or\
                            listss[a][d] == listss[b][e] != " " or listss[c][f] == listss[b][e] != " ":
                        if valid == 0 and listss[a][d] == " ":
                            listss[a][d] = "O"
                            valid = 1
                        if valid == 0 and listss[b][e] == " ":
                            listss[b][e] = "O"
                            valid = 1
                        if valid == 0 and listss[c][f] == " ":
                            listss[c][f] = "O"
                            valid = 1
                    d, e, f = d + 1, e + 1, f + 1

            'Diagonal'

            if valid == 0 and listss[0][0] == listss[1][1] != " " or\
                    listss[0][0] == listss[2][2] != " " or listss[2][2] == listss[1][1] != " ":
                if valid == 0 and listss[0][0] == " ":
                    listss[0][0] = "O"
                    valid = 1
                if valid == 0 and listss[1][1] == " ":
                    listss[1][1] = "O"
                    valid = 1
                if valid == 0 and listss[2][2] == " ":
                    listss[2][2] = "O"
                    valid = 1

            if valid == 0 and listss[2][0] == listss[1][1] != " " or\
                    listss[0][2] == listss[2][0] != " " or listss[0][2] == listss[1][1] != " ":
                if valid == 0 and listss[2][0] == " ":
                    listss[2][0] = "O"
                    valid = 1
                if valid == 0 and listss[1][1] == " ":
                    listss[1][1] = "O"
                    valid = 1
                if valid == 0 and listss[0][2] == " ":
                    listss[0][2] = "O"
                    valid = 1

            'centro e lateral'
            if listss[1][1] == " " and valid == 0:
                listss[1][1] = "O"
                valid = 1
            elif valid == 0 and listss[0][0] == " " and (listss[0][1] == "X" or listss[1][0] == "X"):
                listss[0][0] = "O"
                valid = 1
            elif valid == 0 and listss[0][2] == " " and (listss[0][1] == "X" or listss[1][2] == "X"):
                listss[0][2] = "O"
                valid = 1
            elif valid == 0 and listss[2][0] == " " and (listss[2][1] == "X" or listss[1][0] == "X"):
                listss[2][0] = "O"
                valid = 1
            elif valid == 0 and listss[2][2] == " " and (listss[2][1] == "X" or listss[1][2] == "X"):
                listss[2][2] = "O"
                valid = 1
            elif valid == 0 and listss[0][0] == " ":
                listss[0][0] = "O"
                valid = 1
            elif valid == 0 and listss[0][2] == " ":
                listss[0][2] = "O"
                valid = 1
            elif valid == 0 and listss[2][0] == " ":
                listss[2][0] = "O"
                valid = 1
            elif valid == 0 and listss[2][2] == " ":
                listss[2][2] = "O"
                valid = 1
    valid = 0
    a, b, c = 0, 0, 0
    d, e, f = 0, 1, 2
    i = 6
    initprt()
    while i > 0:

        while i > 3:
            i -= 1
            if listss[a][d] == listss[b][e] == listss[c][f] == "X" or\
                    listss[a][d] == listss[b][e] == listss[c][f] == "O":
                print("Parabéns jogador {}{}{} você VENCEU!!!".format(listss[a][d], listss[b][e], listss[c][f]))
                init = 1
                draw = 1
            a, b, c = a+1, b+1, c+1
        d, e, f, = 0, 0, 0

        while i > 0:
            a, b, c = 0, 1, 2
            i -= 1
            if listss[a][d] == listss[b][e] == listss[c][f] == "X" or\
                    listss[a][d] == listss[b][e] == listss[c][f] == "O":
                print("Parabéns jogador {}{}{} você VENCEU!!!".format(listss[a][d], listss[b][e], listss[c][f]))
                init = 1
                draw = 1
            d, e, f = d + 1, e + 1, f + 1

    if listss[0][0] == listss[1][1] == listss[2][2] == "X" or listss[0][0] == listss[1][1] == listss[2][2] == "O":
        print("Parabéns jogador {}{}{} você VENCEU!!!".format(listss[0][0], listss[1][1], listss[2][2]))
        init = 1
        draw = 1

    if listss[2][0] == listss[1][1] == listss[0][2] == "X" or listss[2][0] == listss[1][1] == listss[0][2] == "O":
        print("Parabéns jogador {}{}{} você VENCEU!!!".format(listss[2][0], listss[1][1], listss[0][2]))
        init = 1
        draw = 1
    init -= 1
    if draw == 0 and init == 0:
        print("ITS A DRAW")
    draw = 0
    while init == 0:
        ans = input("Deseja jogar novemente?: [Y/N]")
        if ans == "y":
            init = 9
            listss[0][0], listss[0][1], listss[0][2], listss[1][0], listss[1][1], listss[1][2],\
                listss[2][0], = " ", " ", " ", " ", " ", " ", " "
            listss[2][1], listss[2][2] = " ", " "
        if ans == "n":
            init = -1
