import os
from fileIO import exportWords

from game import WORDS_FILE


class Data:
    words_to_be_saved: dict = {}


class UtilFunctions:

    def addWord(word: str, definition: str, example: str) -> None:
        Data.words_to_be_saved[word] = {}
        Data.words_to_be_saved[word]['definition'] = definition
        Data.words_to_be_saved[word]['example'] = example

    def removeWord(word: str) -> bool:
        pass

    def save() -> None:
        if Data.words_to_be_saved:
            exportWords(WORDS_FILE, Data.words_to_be_saved)
            print('Succesfully added word(s):')
            for w in Data.words_to_be_saved:
                print(w)


if __name__=="__main__":
    while True:
        os.system('cls||clear')
        print()
        print('\tType s to view all words currently in the dictionary')
        print('\tType q to save changes and quit')
        print()  # newline
        cmd = input('Do you want to add or remove a word? (a/r)')
        
        # add word
        if cmd == 'a':
            WORD = input('Enter the word: ')
            WORD_DEFINITON = input('Enter the definition: ')
            WORD_EXAMPLE = input('Enter an example: ')
            
            # display the entry for confirmation
            os.system('cls||clear')
            print(f'{WORD}\n{WORD_DEFINITON}\n"{WORD_EXAMPLE}"')
            print()  # newline
            
            # confirm the entry is correct
            cmd2 = input('Save word in dictionary? (y/n)')
            if cmd2 == 'y':
                # store entry in data class
                Data.words_to_be_saved[WORD] = {}
                Data.words_to_be_saved[WORD]['definition'] = WORD_DEFINITON
                Data.words_to_be_saved[WORD]['example'] = WORD_EXAMPLE
            
            elif cmd2 == 'n':
                continue
            
            else:
                print(f'Unknown command: {cmd2}')
                continue
        
        # remove word
        elif cmd == 'r':
            print('this functionality is not added yet')
        
        # print all words in dictionary
        elif cmd == 's':
            print('this functionality is not added yet')
        
        # save and quit
        elif cmd == 'q':
            UtilFunctions.save()
            break
        
        else:
            print(f'Unknown command: "{cmd}"')