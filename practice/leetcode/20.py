class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = 0
        square_brackets = 0
        curly_braces = 0
        pre = ''
        ret = True
        for char in s:
            if char == '(':
                parentheses += 1
            elif char == ')':
                if pre=='{' or pre=='[':
                    return False
                parentheses = parentheses - 1
            elif char == '[':
                square_brackets += 1
            elif char == ']':
                if pre=='{' or pre=='(':
                    return False
                square_brackets = square_brackets - 1
            elif char == '{':
                curly_braces += 1
            elif char == '}':
                if pre=='(' or pre=='[':
                    return False
                curly_braces = curly_braces - 1
            if parentheses < 0 or square_brackets < 0 or curly_braces < 0:
                return False
            pre = char
        if parentheses != 0 or square_brackets != 0 or curly_braces != 0:
            ret = False
        return ret

solution = Solution()
print(solution.isValid("([)]"))