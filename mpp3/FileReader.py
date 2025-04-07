import os
from unidecode import unidecode

class fileReader:
    def __init__(self, path):
        self.path = path
        self.totalCounter = 0
        self.charsDict = {}
        self.charsPercentDict = {}

    def generateDictionary(self):
        for filename in os.listdir(self.path):
            print(filename)
            full_path = os.path.join(self.path, filename)
            with open(full_path, 'r', encoding='utf-8') as file:
                for line in file:
                    words = [unidecode(word.strip()) for word in line.strip().split()]
                    for word in words:
                        for char in word.lower():
                            if 'a' <= char <= 'z':
                                self.charsDict[char] = self.charsDict.get(char, 0) + 1
                                self.totalCounter += 1
        return self.charsDict

    def generatePercentDict(self):
        if len(self.charsDict) == 0:
            self.generateDictionary()


        for key in self.charsDict:
            self.charsPercentDict[key] = round(self.charsDict[key]/self.totalCounter,4)


