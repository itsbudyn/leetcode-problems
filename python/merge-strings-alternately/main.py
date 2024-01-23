class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newword = ""
        remainder = ""

        word1_len = len(word1)
        word2_len = len(word2)

        if word1_len > word2_len:
            remainder = word1[word2_len:]
        else:
            remainder = word2[word1_len:]

        for i in range(min(word1_len,word2_len)):
            newword+=word1[i]+word2[i]
            
        return newword + remainder