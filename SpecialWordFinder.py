from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    def __init__(self, word_file):
        super().__init__(word_file)

    
    
    def get_words(self):
        temp = []
        for line in self.file:
            if '#' not in line.strip() and line.strip() != '':
                temp.append(line.strip())
        return temp