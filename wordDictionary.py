from dataclasses import dataclass
import random

from fileIO import importWords


@dataclass(frozen=True)
class MultipleChoice:
    """Immutable dataclass for a multiple choice questionaire"""
    word: str
    definition: str
    example: str
    # collection of definitions
    incorrect_choices: tuple[str]
    

class WordDictionary:
    words_dictionary: dict  # raw contents of the json file
    
    # these two fields below are pre-computed in the constructor
    index_word: dict = {}  # words mapped to their indeces
    word_def: dict = {}    # definitions mapped to their words

# ------------------
# ----- PUBLIC -----
# ------------------

    def __init__(self, filePath: str):
        self.words_dictionary = importWords(filePath)
        for n, w in enumerate(self.words_dictionary):
            self.index_word[n] = w
            self.word_def[w] = self.words_dictionary[w]['definition']
            
    def generateMC(self) -> MultipleChoice:
        word, definition, example = self._getRandomWord()
        return MultipleChoice(word, definition, example, self._getRandomDefs(word))
    
    
# -------------------
# ----- PRIVATE -----
# -------------------
    
    def _getRandomWord(self) -> tuple[str, str, str]:
        """Returns:
            tuple[str, str, str]: word, definition and example"""
        # compute random index
        WORD_NO: int = random.randint(0, len(self.words_dictionary)-1)
        # get word from dictionary using index
        WORD: str = [w for n, w in enumerate(self.words_dictionary) if n == WORD_NO][0]  # [0] converts from list to str
        WORD_DEFINITION: str = self.words_dictionary[WORD]['definition']
        WORD_EXAMPLE: str = self.words_dictionary[WORD]['example']

        return (WORD, WORD_DEFINITION, WORD_EXAMPLE)


    def _getRandomDefs(self, avoid: str, amount: int = 3) -> tuple:
        """
        Generates X random indices, computes them, wraps them in a tuple and returns it. 
        
        Argument 'avoid' is necessary to ensure none of them are of the word to be guessed.

        Args:
            avoid (str): word to be guessed. Necessary for ensuring its definition won't appear twice
            amount (int, optional):  amount of definitions to generate. Defaults to 3.

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
                if self.word_def[self.index_word[random_index]] not in random_definitions and self.index_word[random_index] is not avoid:
                    random_definitions.append(self.word_def[self.index_word[random_index]])
                    completed = True
                    
        return tuple(random_definitions)