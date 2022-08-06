class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brakets = {'(':')','[':']','{':'}'}
        from collections import deque
        st = deque()
        for char in s:
            if char in brakets.keys():
                st.append(char)
            else:
                top = st.pop()
                if brakets[top] == char:
                    pass
                else:
                    return False
        if st:
            return False
        else:
            return True
solution = Solution()
print(solution.isValid("()"))