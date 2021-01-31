import json
import difflib as dl
from os import O_TEMPORARY

##imports dictionary data from json in common directory.
dictionary_data = json.load(open("data.json"))



def getdef(search):
    #fxn to return defns. Returns "Not Found" is word is not found.
    result = dictionary_data.get(search, "Not Found")
    return result

##todo - format the definition outputs more nicely.


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

    # if the word is not found, app will look for similar words based on similarity ratio. will recommend 3 similar word
    # and ask if that is the word the user was looking for with a y/n option if only 1 world is returned, or 1-3 if 2 or 3 options are returned. If the user chooses y, or, the defn of the recomended word 
    # will be displayed. If the user chooses no, they will be asked to search again and the loop will restart.
    elif getdef(userinput) == "Not Found":
        

        #recommends 3 dictionary words using difflib, can change the number of words returned, and the delta cutoff for similarity
        recommended = dl.get_close_matches(userinput, dictionary_data.keys(), 3, cutoff=0.6)
        
        #prints the list of recommended words
        print(str(len(recommended))+" Recommendation(s) found:")
        count = 0
        for foo in recommended:
            
            temp = recommended[count]
            print(str(count+1)+". "+ temp)
            count +=1

        #conditionals for if there is only one recommended word, changes the commands user and some of the messages printed
        if len(recommended) == 1:
            choice = input("Did you mean "+ str(recommended[0])+"? (Y/N): ")
            while True:
                if choice.lower() == "y":
                    print(getdef(str(recommended[0])))
                    break
                elif choice.lower() == "n":
                    print("The word you're looking for was not found. Please try a new search.")
                    break
                else:
                    choice=input("Invalid choice, please choose (Y/N): ")
        #conditionals for if there is more than 1 recommended word
        else:
            choice=input("Which word did you mean? (1-"+str(len(recommended))+", N if none): ")
            while True:
                try:
                    choice.isnumeric()
                    if int(choice):
                        if int(choice) > 0 and int(choice)<(len(recommended)+1):
                            print(getdef(str(recommended[(int(choice)-1)])))
                            break
                        else:
                            input("Please enter a digit between 1-"+str(len(recommended))+", or N if none of the recomended words match.")
                except ValueError:
                    if str(choice.lower()) == "n":
                        print("The word you're looking for was not found. Please try a new search.")
                        break      

                    else:
                        choice=input("Invalid choice, please choose 1-"+str(len(recommended))+", N if none: ")
