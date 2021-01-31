import json

dictionary_data = json.load(open("data.json"))

def getdef(search):
    result = dictionary_data.get(search, "Not Found")
    return result

##print(dictionary_data)

while True:
    userinput = input('Enter a word ("\end" to exit): ')
    if userinput == "\end":
        break
    elif getdef(userinput) != "Not Found":
        print(getdef(userinput))
    elif getdef(userinput) == "Not Found":
        ##To-do similarity ratio and word recommendation, for now just prints not found
        print(getdef(userinput))
        ## if ratio > X%
        ##  did you mean this y/n?
        ##  if yes
        ##      get recommended
        ##      Please try another search
        ##      break
        ## else
        ##  word not found

