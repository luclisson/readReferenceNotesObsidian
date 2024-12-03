import sys

from readHighlights import createSortedHighlightList
from writeTextFile import checkFileExist
from writeTextFile import writeToFile
from readCurrBooks import readJsonBooks


path_vault_references = sys.argv[1]
path_to_highlights = sys.argv[2]

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