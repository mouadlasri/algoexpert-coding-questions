
#   You're given a string of available characters and a string representing a
#   document that you need to generate. Write a function that determines if you
#   can generate the document using the available characters. If you can generate
#   the document, your function should return true; otherwise, it should return false.
#   You're only able to generate the document if the frequency of unique
#   characters in the characters string is greater than or equal to the frequency
#   of unique characters in the document string. For example, if you're given
#   characters = "abcabc" and document = "aabbccc" you cannot generate the
#   document because you're missing one c. The document that you need to create
#   may contain any characters, including special characters, capital letters,
#   numbers, and spaces. Note: you can always generate the empty string ("").
#
#   Sample Input:
#   characters = "Bste!hetsi ogEAxpelrt x "
#   document = "AlgoExpert is the Best!"
#
#   Sample Output:
#   true

def generateDocument(characters, document):

    # get all characters in document
    documentCharacters = list(document) # convert to list to be able to remove characters
    charactersCharacters = list(characters) # convert to list to be able to remove characters

    # loop through documentCharaters to check aif they
    for el in charactersCharacters:
        if el in documentCharacters: # if the character is also in documents list, remove it from list
            documentCharacters.remove(el) # remove the character from the list of characters in the document
            
    if(len(documentCharacters) == 0): # if the list is empty, it means that we can generate the document with the characters we have available.
        return True
        
    return False

characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
print(generateDocument(characters, document)) # True
