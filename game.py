import random
import os

from fileIO import importWords

WORDS_FILE = 'dictionary.json'
PRINT_PREFIX = '[*]'


class Stats:
    correct_answers: int = 0
    incorrect_answers: int = 0
    
    correct_words: dict = {}
    incorrect_words: dict = {}


class Program:
    words_dictionary: dict = {}  # words and their definitions and examples
    definition_index: dict = {}  # definitions indexed to their positions
    
    # ------------------
    # ----- PUBLIC -----
    # ------------------
    
    def __init__(self):
        self.words_dictionary = importWords(WORDS_FILE)
        # sort definitions into definition_index
        for n, word in enumerate(self.words_dictionary):
            self.definition_index[n] = self.words_dictionary[word]['definition']
        
    # Start game
    def run(self) -> None:
        while True:
            print()
            print('\tWelcome to my simple vocabulary trainer program!')
            print('\tThe way it works is that you get a word and four possible definitions.')
            print('\tOne is correct and you will simply enter the number of your guess and press enter.')
            print("\tAfterwards the correct answer will appear")
            print()  # newline
            cmd = input(f"{PRINT_PREFIX} Press enter to begin and type 'q' at any time to quit.\n")

            if cmd == "q":
                break

            elif cmd == "":
                self._loop()  # begin game
                self._quit()
                break

            else:
                print(f'{PRINT_PREFIX} Unknown command: "{cmd}"')

    # -------------------
    # ----- PRIVATE -----
    # -------------------

    # Program loop
    def _loop(self) -> None:
        cmd:str = ''
        
        while cmd != 'q':
            # clear console
            os.system('cls || clear')
            # get random word, index of it and its definition
            WORD_NO, WORD, WORD_DEF = self._getRandomWord()
            # get random definitions
            definitions: list[str] = self._getRandomDefs(WORD_NO)
            # insert actual definition at random index
            definitions.insert(random.randint(0, len(definitions)-1), WORD_DEF)

            # print word, an example and the definitions
            print(WORD, '\n\t"', self.words_dictionary[WORD]['example'].strip(), '"')
            print()  # newline
            self._printChoices(definitions)

            # receive user guess
            print()  # newline
            cmd = input('Type your guess: ')
            if cmd == 'q': continue  # early exit
            
            # test if guess is a valid integer AND is within range of possible answers
            try: 
                int(cmd)                 # valid int
                definitions[int(cmd)-1]  # within range
                
            except ValueError: 
                input(f'[ERROR] "{cmd}" is not a valid guess\n Press enter to keep playing...\n')
                continue
            
            except IndexError:
                input(f'[ERROR] "{cmd}" is not a valid guess\n Press enter to keep playing...\n')
                continue


            # evaluate answer
            if definitions[int(cmd)-1] == WORD_DEF:
                print("Correct!")
                Stats.correct_answers += 1
                
                try: Stats.correct_words[WORD] += 1
                except KeyError: Stats.correct_words[WORD] = 1
                
            else:
                print(f'Wrong! Correct answer:\n{WORD_DEF}')
                Stats.incorrect_answers += 1
                
                try: Stats.incorrect_words[WORD] += 1
                except KeyError: Stats.incorrect_words[WORD] = 1
                    
            input()  # pause and let user continue...
            

    # Clean exit
    def _quit(self) -> None:
        print(f'\n{"="*22}\n{"Score":^22s}\n\n{"Correct:":20s}{Stats.correct_answers:>2}\n{"Incorrect:":20s}{Stats.incorrect_answers:>2}\n{"="*22}\n')
        
        print("Word(s) you got wrong:" if len(Stats.incorrect_words) > 0 else '')
        for w in Stats.incorrect_words:
            print(f'{w+":":20s}{Stats.incorrect_words[w]:>2}')
            
        print()  # newline

    # --------------------------
    # ----- Game functions -----
    # --------------------------

    def _getRandomWord(self) -> tuple[int, str, str]:
        """Generates a random index and pulls the word and its definition,
        wraps them in a tuple and returns it.

        Returns:
            tuple[int, str, str]: word index, word and word definition
        """
        # index of the word to be guessed
        WORD_NO: int = random.randint(0, len(self.words_dictionary)-1)
        # word to be gussed
        WORD: str = [w for n, w in enumerate(self.words_dictionary) if n == WORD_NO][0]  # [0] converts from list to str
        # definition of word to be guessed
        WORD_DEF: str = self.definition_index[WORD_NO]
        # return elements
        return (WORD_NO, WORD, WORD_DEF)


    def _getRandomDefs(self, chosen_word_index: int, amount: int = 3) -> list:
        """Generates X random indices (X = amount parameter), computes them,
        wraps them in a list and returns it. chosen_word_index is necessary
        to ensure they aren't the word to be guessed

        Args:
            chosen_word_index (int): Index of word to be guessed. Necessary for ensuring its definition won't appear twice
            amount (int, optional):  Amount of definitions to generate. Defaults to 3.

        Returns:
            list: collection of definitions
        """
        # random words' definitions
        random_definitions: list[str] = []
        # pick random definitions
        while len(random_definitions) < amount:
            completed = False
            while not completed:
                # compute random index
                random_index = random.randint(0, len(self.words_dictionary)-1)
                if self.definition_index[random_index] not in random_definitions and random_index is not chosen_word_index:
                    random_definitions.append(self.definition_index[random_index])
                    completed = True
                    
        return random_definitions


    def _printChoices(self, choices: list[str]) -> None:
        for n, i in enumerate(choices):
            print(f' {n+1}) {i}')
