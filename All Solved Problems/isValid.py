# https://leetcode.com/problems/valid-parentheses/
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup_dictionary = dict(zip(list(")}]"), list("({[")))
        stack = []

        for i in s:
            if stack and i in ")}]" and stack[-1] == lookup_dictionary[i]:
                stack.pop()
            else:
                stack.append(i)

        return True if len(stack) == 0 else False
