
#   Given a non-empty string of lowercase letters and a non-negative integer
#   representing a key, write a function that returns a new string obtained by
#   shifting every letter in the input string by k positions in the alphabet,
#   where k is the key.
#
#   Note that letters should "wrap" around the alphabet; in other words, the
#   letter z shifted by one returns the letter a.
#
#   Sample Input:
#       string = "xyz"
#       key = 2
#   Sample Output:
#       "zab"

# Solution 1
# O(n) time / O(n) space
# n = length of string

def caesarCipherEncryptor(string, key):
    # ord(a) returns ascii value of a (=76)
    # chr(76) returns char value of 76 (=a)
    # ascii + ord(a) % ord(z) - 1 will keep it in the range of [ord('a'), ord('z')]
    baseAscii = ord('a')
    endAscii = ord('z')

    # newKey (26 in this case) = number of characters between 'z' and 'a' in the ascii code, we use
    # use it to loop around that range of characters if key > 26
    newKey = key % (endAscii - baseAscii + 1) 
    
    code = []
    
    for e in string:
        newLetterAscii = (ord(e) + newKey)
        if newLetterAscii <= 122:
            code.append(chr(newLetterAscii))
        else:
            code.append(chr((newLetterAscii + baseAscii - 1) % endAscii))
    
    finalCode = ''.join(code)
   
    return finalCode
    
        
    
# Sample input: "xyz", 2
string = "xyz"
key = 2
print(caesarCipherEncryptor(string, key)) # output: "zab"

