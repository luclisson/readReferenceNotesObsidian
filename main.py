import os

from readHighlights import createSortedHighlightList
from writeTextFile import checkFileExist
from writeTextFile import writeToFile
from readCurrBooks import readJsonBooks

var1 = os.getenv('VAR1')
var2 = os.getenv('VAR2')
print(var1)
print(var2)


path_vault_references = "/Users/lucliss/Documents/second brain/notes/reference notes/"
path_to_highlights = "/Users/lucliss/Downloads/notes.txt"

def main():
    print(f"path to vault references: {path_vault_references}")
    print(f"path to original highlight source: {path_to_highlights}")
    list = createSortedHighlightList(path_to_highlights)
    for i in range(len(list)):
        checkFileExist(path_vault_references, list[i][0].title)
        writeToFile(path_vault_references, list[i])
    readJsonBooks()


if __name__ == "__main__":
    main()