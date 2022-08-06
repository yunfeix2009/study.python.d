
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        final = ''
        if len(strs) == 1:
            return strs[0]
        for i in range(0, len(strs[0])):
            flag = True
            pre_of_fir = strs[0][i]
            for other_str in strs[1::]:
                if i >= len(other_str):
                    return final
                if pre_of_fir != other_str[i]:
                    return final
            final = final + pre_of_fir
        return ''
solution = Solution()
solution.longestCommonPrefix(['flower', 'flower', 'flower', 'flower'])