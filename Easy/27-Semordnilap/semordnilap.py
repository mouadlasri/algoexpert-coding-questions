
#   Write a function that takes in a list of unique strings and returns a list of
#   semordnilap pairs.
#
#   A semordnilap pair is defined as a set of different strings where the reverse
#   of one word is the same as the forward version of the other. For example the
#   words "diaper" and "repaid" are a semordnilap pair, as are the words
#   "palindromes" and "semordnilap".
#
#   The order of the returned pairs and the order of the strings within each pair
#   does not matter.

#   Sample Input:
#   words = ["liver", "dog", "hello", "desserts", "evil", "test", "god", "stressed", "racecar", "palindromes", "semordnilap", "abcd", "live"]
#   Sample Output:
#   [["dog", "god"], ["desserts", "stressed"], ["evil", "live"], ["palindromes", "semordnilap"]]

# Solution:
def semordnilap(words):

    wordsSet = set(words)
    semordnilapPairs = []

    for word in words:
        reverse = word[::-1]
        if reverse in wordsSet and reverse != word: # check if the reverse is in the set and if it is not the same word as the original word (we don't want to add the same word twice)
            semordnilapPairs.append([word, reverse]) # add the pair to the pairs list (we don't need to add the reverse of the word since it will be added in the next iteration)
            wordsSet.remove(word) # remove the word from the set so that we don't add it again in the next iteration (we don't want to add the same word twice)
            wordsSet.remove(reverse) # remove the reverse of the word from the set so that we don't add it again in the next iteration (we don't want to add the same word twice)

    return semordnilapPairs

# time complexity: O(n * m) where n is the length of the words list and m is the length of the longest word in the list 

words = ["liver", "dog", "hello", "desserts", "evil", "test", "god", "stressed", "racecar", "palindromes", "semordnilap", "abcd", "live"]
print(semordnilap(words)) # [["dog", "god"], ["desserts", "stressed"], ["evil", "live"], ["palindromes", "semordnilap"]]




