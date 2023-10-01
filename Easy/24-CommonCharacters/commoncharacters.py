
# Write a function that takes in a non-empty list of non-empty strings and
# returns a list of characters that are common to all strings in the list,
# ignoring multiplicity.
# In other words, if a character appears more than once in all strings, you
# should include it in your output list only once.
# Note that characters should be included in the returned list in the order
# in which they appear in the original list of strings.

# Sample Input:
# words = ["bella", "label", "roller"]
# Sample Output:
# ["e", "l", "l"]

def commonCharacters(strings):

    dict = {}
    res = []
    
    for s in strings:
        for character in set(s): # remove duplicates since we can ignore multiplicity
            if character in dict:
                dict[character] = dict[character] + 1
            else:
                dict[character] = 1

    for key, value in dict.items():
        # check if value is equal to the length of our "strings" input
        if value == len(strings): # it means that the character is present in all strings
            res.append(key) # append the key (alphanumeric letter)

    
    return res


strings = ["abc", "bcd", "cbaccd"]
print(commonCharacters(strings)) # ["b", "c"]