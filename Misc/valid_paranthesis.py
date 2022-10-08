class Solution:
    # find if the input sting is valid paranthesis
    def isValid(self, s: str) -> bool:
        stack = []
        for each_string in s:
            if each_string == "(":
                stack.append(")")
            elif each_string == "{":
                stack.append("}")
            elif each_string == "[":
                stack.append("]")
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != each_string:
                    return False
        if len(stack) == 0:
            return True
        return False

    # find the length of the longest valid paranthesis
    def longestValidParentheses(self, s: str, approach=None) -> int:
        stack = [-1] #initialise first index as -1
        longest_valid = 0
        for i, each_string in enumerate(s):
            if each_string == "(":  # if the string is an empty bracket append the index
                stack.append(i)
            else:
                stack.pop()  # pop the index
                if len(stack) == 0:  # stack can never be empty so just push the currrent index
                    stack.append(i)
                else:
                    #longest valid paranthesis =max(longest,current index-top index)
                    longest_valid = max(longest_valid, i - stack[-1])

        return longest_valid


Soln = Solution()
print(Soln.longestValidParentheses("(()))())(", approach=1))
