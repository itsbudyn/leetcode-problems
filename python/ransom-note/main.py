class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        self.noteDict = dict()
        self.magDict = dict()

        self.noteLetters = set(ransomNote)
        self.magLetters = set(magazine)

        for i in self.noteLetters: self.noteDict[i] = ransomNote.count(i)
        for i in self.magLetters: self.magDict[i] = magazine.count(i)

        for i in self.noteLetters:
            if i not in self.magLetters or self.magDict[i] < self.noteDict[i]: return False
        return True