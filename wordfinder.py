"""Word Finder: finds random words from a dictionary."""
import random 

class WordFinder:
    ...
    def __init__(self, word_file):
        self.word_list = 100
        self.file = open(word_file, 'r')
        self.list = self.get_words()
        self.words_count()

    def get_words(self):
        temp = []
        for line in self.file:
            temp.append(line.strip())
        return temp
        
    def random (self):
        rand =  random.choice(self.list)
        return rand

    def words_count (self):
        print(f'{len(self.list)} words read')


