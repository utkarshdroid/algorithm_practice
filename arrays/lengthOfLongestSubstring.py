class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charset = set()
        max_sub = 0
        i,j = 0,0
        while(i<len(s)):
            charset.add(s[i])
            j=i+1
            while( j <len(s)):
                if s[j] in charset:
                    break
                else :
                    charset.add(s[j])
                    j+=1
            i+=1
            max_sub = max(max_sub,len(charset))
            charset = set()
        return max_sub



########################################################
#Optimised  Solution 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charset = set()
        max_sub = 0
        l,r = 0,0
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            max_sub = max(max_sub,len(charset))
        return max_sub

            


        