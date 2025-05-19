import os
from fileIO import exportWords, importWords

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
            
            # display the new entry for confirmation
            os.system('cls||clear')
            print(f'{WORD}\n{WORD_DEFINITON}\n"{WORD_EXAMPLE}"')
            print()  # newline
            
            # confirm the entry is correct
            cmd2 = input('Save word in dictionary? (y/n)')
            if cmd2 == 'y':
                UtilFunctions.addWord(WORD, WORD_DEFINITON, WORD_EXAMPLE)
            
            else:
                continue
        
        # remove word
        elif cmd == 'r':
            print('[ERROR] This functionality is not added yet\n')
            input('Press enter to continue...')
        
        # print all words in dictionary
        elif cmd == 's':
            words_dict = importWords(WORDS_FILE)
            words_string: str = ''
            for n, w in enumerate(words_dict):
                # add comma and space after each word but the last
                words_string += f'{w}, ' if n is not len(words_dict)-1 else w
                
            print(words_string)
            input()
        
        # save and quit
        elif cmd == 'q':
            UtilFunctions.save()
            break
        
        else:
            print(f'Unknown command: "{cmd}"')