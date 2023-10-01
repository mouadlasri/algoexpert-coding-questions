
#   Write a function that takes in a string of lowercase English-alphabet letters
#   and returns the index of the string's first non-repeating character.
#   The first non-repeating character is the first character in a string that
#   occurs only once.
#   If the input string doesn't have any non-repeating characters, your function
#   should return -1.
#
#   Sample Input:
#   string = "abcdcaf"
#
#   Sample Output:
#   1 // The first non-repeating character is "b" and is found at index 1.
#
# Solution:
#   1. Create a dictionary to store the frequency of each character in the string
#   2. Loop through the string and check if the character is in the dictionary
#   3. If it is, increment the value of the key by 1
#   4. If it is not, add the character to the dictionary and set the value to 1
#   5. Loop through the string again and check if the value of the character is 1
#   6. If it is, return the index of the character
#   7. If it is not, return -1
#
# Time Complexity: O(n)

def firstNonRepeatingCharacter(string):
    
        dict = {}
    
        for character in string:
            if character in dict:
                dict[character] = dict[character] + 1
            else:
                dict[character] = 1
    
        for i in range(len(string)):
            if dict[string[i]] == 1:
                return i
    
        return -1
