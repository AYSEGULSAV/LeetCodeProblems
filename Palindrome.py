from re import X


class Solution(object):
    def isPalindrome(self, a)->bool:
        """
        :type a: int
        :rtype: bool
        """
        if a<0:
            return False
        orginal=a
        reversed_num=0
        while a>0:
            number= a%10
            reversed_num=reversed_num*10+number
            a//=10

        return orginal==reversed_num
s=Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
