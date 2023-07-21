class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        matching_anagrams = []

        for word in word_list:
            if word.lower() != self.word.lower() and sorted(word.lower()) == sorted(self.word.lower()):
                matching_anagrams.append(word)

        return matching_anagrams