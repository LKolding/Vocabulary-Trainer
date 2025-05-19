import json


def importWords(filePath: str) -> dict:
    words: dict

    try:
        with open(filePath) as f: 
            words = json.load(f)
        
    except OSError:
        print(f'Something went wrong when opening file {filePath}. Dictionary has not been be loaded.')
        
    else:
        return words


def exportWords(filename: str, words: dict) -> None:
    """Reads contents of 'filename', adds the new word(s) then rewrites all of them to 'filename.

    Args:
        filename (str): filename of the (json formatted) dictionary of words
        words (dict): new words to be added (assumed to be correctly formatted)
    """
    # get existing dictionary of words
    allWords: dict = importWords(filename)
    
    # add new word(s)
    for w in words:
        allWords[w] = words[w]

    try:
        with open(filename, 'w') as f:
            json.dump(allWords, f, indent=2, sort_keys=True)
            
    except OSError:
        print(f'Could not write to file {filename}. The new words have therefore not been saved.')
