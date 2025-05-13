
import json
def importWords(filename: str) -> dict:
    words: dict

    with open(filename) as f: 
        words = json.load(f)
        
    return words

def exportWords(words: dict) -> None:
    pass

if __name__=="__main__":
    print('This is a module; not supposed to be executed')
    exit()