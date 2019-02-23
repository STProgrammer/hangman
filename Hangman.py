import random

def hangman(word):
    wrong = 0
    stages = ["",
              "___________          ",
              "|         |          ",
              "|         |          ",
              "|         0          ",
              "|        /|\         ",
              "|        / \         ",
              "|                    "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    print((" ".join(board)), "\n")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)
        if char in rletters:
            while char in rletters:
                cind = rletters \
                       .index(char)
                board[cind] = char
                rletters[cind] = '$'  
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n"
                .join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0:e]))
        print("You lose! It was {}."
              .format(word))


Word_list = ["cat","dog","city","computer","software","programming","bastard",
             "bitch","president","country","tourist","travel","opportunity",
             "economics","money","finances","inflation","deflation","cost",
             "mathematics","psychology","sociology","history","physics","fish",
             "zebra","elephant","giraffe","domain","doctor","professor","sport",
             "example","Python","universal","follow","random","word","negative",
             "positive","printing","input","output","engineering","astronomy",
             "logic","philosophy","numbers","panel","controls","cards","rat",
             "politics","sick","healthy","wealthy","happy","sad","angry","fat",
             "fit","soccer","rugby","awkward","silence","social","equivalent"
             "code","loop","glitch","bug","compiler","interpreter","virtual"]



a = str()
while a != "q":
    word = random.choice(Word_list)
    hangman(word)
    a = input("press \"q\" to quit, or press any key to continue")

