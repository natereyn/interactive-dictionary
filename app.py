import json

##imports dictionary data from json in common directory.
dictionary_data = json.load(open("data.json"))



def getdef(search):
    #fxn to return defns. Returns "Not Found" is word is not found.
    result = dictionary_data.get(search, "Not Found")
    return result

##print(dictionary_data)


## main app loop, infinite with a user input end condition
while True:
    ## take user input, either a word to search for the defn of or the "\end" command
    userinput = input('Enter a word ("\end" to exit): ')
    userinput = userinput.lower()

    # if user enters \end command, loop breaks
    if userinput == "\end":
        print("Thanks for stopping by.")
        break

    # if the word is found, the definitions are returned as a list
    elif getdef(userinput) != "Not Found":
        print("The definition of " + userinput.capitalize() +" is " + str(getdef(userinput)))

    # if the word is not found, app will look for similar words based on similarity ratio. will recommend a (maybe 2-3?) similar word
    # and ask if that is the word the user was looking for with a y/n option. If the user chooses y, the defn of the recomended word 
    # will be displayed. If the user chooses no, they will be asked to search again and the loop will restart.
    elif getdef(userinput) == "Not Found":
        ##To-do similarity ratio and word recommendation, for now just prints not found
        print(getdef(userinput))
        ## if sim_ratio > X%
        ##      did you mean this word y/n?
        ##      if yes
        ##          get recommended word
        ##      else
        ##          Please try another search
        ##          continue
        ## else
        ##      word not found

##to do defn formatting/word capitalization fxn