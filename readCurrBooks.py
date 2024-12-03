import json

def readJsonBooks():
    book_list = []
    with open("amountNumber.json", "r") as f:
        data =json.load(f)
    for i in range(len(data['books'])):
        print(f"{data['books'][i]['title']} was found in your highlights file!")
    f.close()