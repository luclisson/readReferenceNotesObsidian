import json
import os


def readJsonBooks():
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_file_dir, "amountNumber.json")

    with open(json_file_path, "r") as f:
        data =json.load(f)
    for i in range(len(data['books'])):
        print(f"{data['books'][i]['title']} was found in your highlights file!")
    f.close()