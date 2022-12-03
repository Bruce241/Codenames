import random
import time

def get_words(files):
    words = []
    for file in files:
        f = open(file, 'r')
        file_content = f.readlines()
        for line in file_content:
            words.append(line.upper().rstrip())
    game_words = list(random.sample(words, 25))
    return game_words

class Board:
    def __init__(self, words):
        self.words = words
        self.colors = []

        for i in range(13):
            self.colors.append('G')
        for i in range(9):
            self.colors.append('Y')
        for i in range(3):
            self.colors.append('R')
        random.shuffle(self.colors)

        self.guesses = []
    def __str__(self):
        s = ''
        for r in range(5):
            for c in range(5):
                if len(words[r*5+c]) < 6:
                    s += '| {}\t\t'.format(self.words[r*5+c])
                else:
                    s += '| {}\t'.format(self.words[r*5+c])
            s += '|\n'
        s += '\n'
        return s


word_files = ('words/marten.txt',)
words = get_words(word_files)
b = Board(words)
game = True
turn = 0

while game:
    turn += 1
    print('Turn {}:'.format(turn))
    print(b)
    print('Your clue is: clue\n')

    while True:
        guess = input('Guess now (or done): ')
        if guess.lower() == 'done':
            break
        else:
            if guess.upper() in b.words:
                b.guesses.append(guess.upper())
                word_index = b.words.index(guess.upper())
                print(word_index)
                print(b.colors[word_index])
                if (b.colors[word_index] == 'G'):
                    print('Correct!\n')
                    time.sleep(1)
                elif (b.colors[word_index] == 'Y'):
                    print('Civilian word!\n')
                    time.sleep(1)
                    break
                elif (b.colors[word_index] == 'R'):
                    print('Assassin!\n')
                    time.sleep(1)
                    game = False
                    break
