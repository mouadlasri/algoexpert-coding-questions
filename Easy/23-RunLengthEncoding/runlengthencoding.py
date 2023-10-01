
#   Write a function that takes in a non-empty string and returns its run-length
#   encoding.
#
#   From Wikipedia, "run-length encoding is a form of lossless data compression
#   in which runs of data are stored as a single data value and count, rather
#   than as the original run." For this problem, a run of data is any sequence
#   of consecutive, identical characters. So the run "AAA" would be run-length-
#   encoded as "3A".
#
#   To make things more complicated, however, the input string can contain all
#   sorts of special characters, including numbers. And since encoded data must
#   be decodable, this means that we can't naively run-length-encode long runs.
#   For example, the run "AAAAAAAAAAAA" (12 A's), can't naively be encoded as
#   "12A", since this string can be decoded as either "AAAAAAAAAAAA" or "1AA".
#   Thus, long runs (runs of 10 or more characters) should be encoded in a split
#   fashion; the aforementioned run should be encoded as "9A3A".
#
#   Sample Input:
#     string = "AAAAAAAAAAAAABBCCCCDD"
#
#   Sample Output:
#     "9A4A2B4C2D"

def runLengthEncoding(string):

    encodedString = [] # List of characters that will be returned as a string
    currentRunLength = 1 # Current run length of the character

    for i in range(1, len(string)): # Start at 1 to compare to previous character
        currentCharacter = string[i] # Current character being looked at
        previousCharacter = string[i-1] # Previous character

        if(currentCharacter != previousCharacter or currentRunLength == 9): # If the current character is not the same as the previous character or the current run length is 9
            encodedString.append(str(currentRunLength)) # Append the current run length to the encoded string
            encodedString.append(previousCharacter) # Append the previous character to the encoded string
            currentRunLength = 0 # Reset the current run length, since we are starting a new run of characters

        currentRunLength += 1 # Increment the current run length, since we are still in the same run of characters

    encodedString.append(str(currentRunLength)) # Append the current run length to the encoded string (for the last character)
    encodedString.append(string[len(string) - 1]) # Append the last character to the encoded string, since the for loop does not account for it

    return ''.join(encodedString)
    

inputString = "AAAAAAAAAAAAABBCCCCDD"
print(runLengthEncoding(inputString)) # 9A4A2B4C2D


        

