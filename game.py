import random  # for random insertion of the correct answer
import os      # for console clear (os.system())

from wordDictionary import WordDictionary, MultipleChoice


WORDS_FILE = 'dictionary.json'
# skip words that have been correctly guessed
SKIP_CORRECT_WORDS = True
PRINT_EXAMPLE = False


def clearConsole() -> None:
    os.system('cls||clear')


class Stats:
    correct_answers: int = 0
    incorrect_answers: int = 0
    
    correct_words: list = []
    # keeps account of how many times a word have been wrongfully guessed
    # eg. {'succinctly' : 3}
    incorrect_words: dict = {}


class Program:
    words_dictionary: WordDictionary
    
# ------------------
# ----- PUBLIC -----
# ------------------
    
    def __init__(self):
        self.words_dictionary = WordDictionary(WORDS_FILE)
        
    # Start game
    def run(self) -> None:
        while True:
            print()
            print('\tWelcome to my simple vocabulary trainer program!')
            print('\tIt works by giving a word and four possible definitions.')
            print('\tOne is correct and you will simply enter the number of your guess and press enter.')
            print("\tAfterwards the correct answer will appear")
            print()  # newline
            cmd = input(f"Press enter to begin and type 'q' at any time to quit.\n")

            if cmd == "q":
                break

            elif cmd == "":
                self._loop()  # begin game
                self._quit()  # clean exit upon return
                break

# -------------------
# ----- PRIVATE -----
# -------------------

    # Program loop
    def _loop(self) -> None:
        cmd:str = ''
        
        while cmd != 'q':
            clearConsole()

            mc: MultipleChoice = self.words_dictionary.generateMC()

            while SKIP_CORRECT_WORDS and mc.word in Stats.correct_words:
                if len(Stats.correct_words) == len(self.words_dictionary.all_words):
                    input('\n\tAll words have been succesfully guessed.\n\tThanks for playing!\n\nPress enter to quit...')
                    return
                    
                mc = self.words_dictionary.generateMC()  # keep generating

            # get a list of random definitions
            choices: list = list(mc.incorrect_choices)
            # insert correct definition at random index
            choices.insert(random.randint(0, len(mc.incorrect_choices)), mc.definition)

            # print word
            print(mc.word)
            if PRINT_EXAMPLE:
                print('\n\t"' + mc.example + '"')
            print()  # newline

            # print all choices
            for n, i in enumerate(choices):
                print(f' {n+1}) {i}')

            # receive user guess
            print()  # newline
            cmd = input('Guess: ')
            if cmd == 'q': continue  # early exit
            
            # test if guess is a valid integer AND is within range of possible answers
            try: 
                int(cmd)                # valid int
                choices[int(cmd)-1]     # within range
                
            except (ValueError, IndexError):
                input(f'[ERROR] {cmd} is not a valid guess\n Press enter to keep playing...')
                continue

            # evaluate answer
            if choices[int(cmd)-1] == mc.definition:
                print("Correct!")
                Stats.correct_answers += 1
                
                if mc.word not in Stats.correct_words:
                    Stats.correct_words.append(mc.word)
                
            else:
                print(f'Wrong. Correct answer:\n\n{mc.definition}')
                Stats.incorrect_answers += 1
                
                try: Stats.incorrect_words[mc.word] += 1
                except KeyError: Stats.incorrect_words[mc.word] = 1
                    
            input()  # pause and let user continue...
            

    # Clean exit
    def _quit(self) -> None:
        print(f'\n{"="*22}\n{"Score":^22s}\n\n{"Correct:":20s}{Stats.correct_answers:>2}\n{"Incorrect:":20s}{Stats.incorrect_answers:>2}\n{"="*22}\n')
        
        print("Word(s) you got wrong:" if len(Stats.incorrect_words) > 0 else '')
        for w in Stats.incorrect_words:
            print(f'{w+":":20s}{Stats.incorrect_words[w]:>2}')
            
        print()  # newline
