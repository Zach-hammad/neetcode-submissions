class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countmap = {}

        for letter in s:
            if letter not in countmap:
                countmap[letter] = 1
            else:
                countmap[letter] += 1
        for letter in t:
            if letter not in countmap:
                return False                
            if letter in countmap:
                countmap[letter] -= 1
        return all(count == 0 for count in countmap.values())
                

