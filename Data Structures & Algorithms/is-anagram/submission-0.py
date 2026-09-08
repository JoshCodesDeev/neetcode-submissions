class Solution:
    def calcFreq(self, s: str):
        freq = {}
        for char in s:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
            
        return freq

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sFreq = self.calcFreq(s)
        tFreq = self.calcFreq(t)

        for sChar in sFreq.keys():
            if sChar not in tFreq or sFreq[sChar] != tFreq[sChar]:
                return False
        
        for tChar in tFreq.keys():
            if tChar not in sFreq or sFreq[tChar] != tFreq[tChar]:
                return False

        return True


        