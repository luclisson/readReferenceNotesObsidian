from highlightObj import Highlight

def createHighlightsRaw(path_to_highlights):
    print(path_to_highlights)
    with open(path_to_highlights, "r") as file:
        content = file.read().split("-----------------------------------")
    highlightsRaw = []
    for i in content:
        highlightsRaw.append(i.strip())
    highlightsRaw.remove(highlightsRaw[len(highlightsRaw)-1]) #remove random last entry which caused erors
    return highlightsRaw


def getTitle(highlight):
    # check for i == ( due to original highlights structure
    title = ""
    for i in highlight:
        if i == "(":
            break
        title = title + i

    title = title.strip()
    return title

def getAuthor(highlight):
    #pupose of finding braces due to highlight structure
    author = ""
    startIndex = highlight.find("(")  + 1
    endIndex = highlight.find(")")

    x = range(startIndex, endIndex, 1)
    for n in x:
        author = author + highlight[n]

    return author

def getTime(highlight):
    try:
        timeData = highlight.splitlines()
        timeData = timeData[len(timeData)-1][15:]
    except:
        print("error")
        timedata = "error"
    return timeData

def getMessage(highlight):
    string = ""
    #check for splitLines len because it varies regarding the highlights length
    if len(highlight.splitlines())>3:
        data = highlight.splitlines()
        data.pop(0)
        data.pop(len(data)-1)
        for i in range(len(data)):
            string = string + data[i].strip() + " "
    else:
        string = highlight.splitlines()[1]

    index = string.find(":")
    message = string[index + 2:]
    return message

def getPage(highlight):
    #find : inorder to cut text infront of it (due to highlight structure)
    data = highlight.splitlines()[1]
    page = data[data.find("f")+2:data.find(":")]
    return page


def createSortedHighlightList(path_to_highlights):
    path = path_to_highlights
    highlightsRaw = createHighlightsRaw(path)
    # sort by title
    outputList = []
    for i in highlightsRaw:
        highlight = Highlight(getTitle(i), getAuthor(i), getTime(i), getPage(i), getMessage(i))
        if len(outputList) == 0:
            list = []
            list.append(highlight)
            outputList.append(list)
        else:
            titleListExists = False
            for i in range(len(outputList)):
                title = outputList[i][0].title
                if highlight.title == title:
                    outputList[i].append(highlight)
                    titleListExists = True
            if(titleListExists == False):
                list = []
                list.append(highlight)
                outputList.append(list)
    return outputList