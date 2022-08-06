class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        # lenth = ''
        # longest = ''
        # longest_odd_num = []
        # for digit in num:
        #     digit = int(digit)
        #     if digit % 2 == 1:
        #         lenth = lenth + str(digit)
        #     else:
        #         if lenth=='':
        #             lenth = 0
        #         if longest == '':
        #             longest = 0
        #         if int(longest) < int(lenth):
        #             longest = lenth
        #             lenth = 0
        # if longest == 0:
        #     return ''
        # return longest
        num = num[::-1]
        for i in num:
            index = num.index(i)
            if int(i)%2==1:
                ret = num[index::]
                ret = ret[::-1]
                return ret
        return ''
solution = Solution()
print(solution.largestOddNumber('352'))

