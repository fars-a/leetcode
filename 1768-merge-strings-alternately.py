class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result=""
        index=min(len(word1),len(word2))
        for i in range(index):
            result+=word1[i]
            result+=word2[i]
        result+=word1[index:]
        result+=word2[index:]
        return result
