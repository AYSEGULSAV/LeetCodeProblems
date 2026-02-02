class Solution(object):
    def longestCommonPrefix(self,strs):
        if not strs:
            return ""
        prefix=strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix=prefix[:-1]
                if prefix=="":
                    return "no match"
            return prefix
sol=Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))
print(sol.longestCommonPrefix(["alık","ali","al"]))
