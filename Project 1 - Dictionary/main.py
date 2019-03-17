import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def define(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len((get_close_matches(w, data.keys()))) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word does not exist, please try again"
        else:
            return "Invalid entry"
    else:
        return "The word does not exist, please try again"

word = input("Define: ")

output = define(word)

if type(output) == list:
    for definition in output:
        print(definition)
else:
    print(output)
