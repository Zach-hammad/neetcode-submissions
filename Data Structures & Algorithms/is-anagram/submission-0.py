class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        dic2 = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for j in t:
            dic2[j] = dic2.get(j, 0) + 1
        if dic == dic2:
            return True
        return False
                

