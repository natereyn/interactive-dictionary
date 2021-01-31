# interactive-dictionary
interactive dictionary application that returns definition(s) for a requested word and can attempt to recommend words after a misspelt searches. Written in Python3.


run app.py from terminal, with data.json in the same directory.

all inputs are validated. Valid inputs are:

|Prompt Text    | Valid Inputs  |
| ------------- |:-------------:|
| `Enter a word ("\end" to exit):` | A word to be searched or `\end`|
| `Did you mean "+ str(recommended[0])+"? (Y/N): `| `Y` or `N` |
| `Invalid choice, please choose (Y/N):` |  `Y` or `N` |
| `Which word did you mean? (1-"+str(len(recommended))+", N if none):`|`1, 2 or 3` for the corresponding word, or `N` if none of the words (returns to beginning of program)|
| `Invalid choice, please choose 1-"+str(len(recommended))+", N if none:` |`1, 2 or 3` for the corresponding word, or `N` if none of the words (returns to beginning of program)|

user can either enter a word to search for the definition of or \end to end the application.

once a word has been entered, the definition(s) will be returned if the word is found, or a list of similar options will be presented if no word is found.

if a word was found, the definition(s) is printed and the program restarts.

if a word was not found, the user will be presented with 1-3 recommended words. From there they can enter `1, 2 or 3` to choose one of the recommended words, or `N` if they wish to return to th main menu
