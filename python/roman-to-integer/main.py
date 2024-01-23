class Solution:
    def romanToInt(self, s: str) -> int:
        numValue = 0
        rnLookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for i in range(len(s) - 1):
            if rnLookup[s[i]] < rnLookup[s[i+1]]:
                numValue -= rnLookup[s[i]]
            else: numValue += rnLookup[s[i]]

        return numValue + rnLookup[s[-1]]