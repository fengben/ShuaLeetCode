class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        beg = 0
        dic = {}
        if s is None:
            return 0
        # m 1
        for i in range(len(s)):
            if s[i] in dic and beg <=dic[s[i]]:# 防止beg往前跑，下面的t
                beg=dic[s[i]]+1
            else:
               ans =max(ans,i-beg+1)
            dic[s[i]] = i
        return ans
if __name__ == '__main__':
    a=Solution().lengthOfLongestSubstring("tmmzuxt")
    print(a)