import os.path
import json

def checkFileExist(path_vault_references, title):
    path = path_vault_references + title+".md"
    if not os.path.exists(path):
        f = open(path, "w")
        f.close()
        with open ("amountNumber.json", "r")as jsonF:
            data = json.load(jsonF)
        newData = {
            "title": f"{title}",
            "amountRef": 1
        }
        with open("amountNumber.json", "w") as jsonF:
            data["books"].append(newData)
            json.dump(data, jsonF)

def checkHighlightExist(path, highlight):
    #unique identifier should be the timestamp
    exist = False
    currContent = open(path, "r")
    for line in currContent:
        if highlight.timestamp in line.strip():
            exist = True
    return exist


def writeToFile(path_vault_references, list):
    counter = 0
    title = list[0].title
    # index 0 because the list are all the highlights of one book and 0 to get one highlights book title
    path = path_vault_references + title+".md"
    f = open(path, "a")

    with open("amountNumber.json", "r") as jsonF:
        data = json.load(jsonF)['books']
        for i in range(len(data)):
            if data[i]['title'] == title:
                index = i
    # read value of json amountRef to be able to numberize the highlights
    # solution with json due to future added highlights and be able to access the amount of highlights with minimal error handling
    for highlight in list:
        num = data[index]['amountRef']
        if not checkHighlightExist(path, highlight):
            #file structure or its design in obsidian
            f.write(f"#### reference no.{num}\n")
            f.write(f"- {highlight.message}\n")
            f.write(f"- {highlight.timestamp}\n")
            f.write(f"- {highlight.title} - {highlight.author} {highlight.page}\n\n")
            data[index]['amountRef'] += 1
            with open("amountNumber.json", "w") as jsonF:
                json.dump({'books': data}, jsonF, indent=4)
            counter= counter +1
    print(f"{counter} highlights were send to {path}")
    f.close()